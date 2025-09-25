import reflex as rx
from typing import TypedDict, Literal
import asyncio


class Message(TypedDict):
    id: int
    author: Literal["user", "ai"]
    type: Literal["text", "code", "log", "error", "build_status"]
    content: str
    collapsible: bool
    language: str | None
    filename: str | None


class BuildStatus(TypedDict):
    status: Literal["Pending", "Running", "OK", "Fail"]
    progress: int
    eta: str


class ChatState(rx.State):
    active_view: Literal["chat", "settings"] = "chat"
    messages: list[Message] = [
        {
            "id": 1,
            "author": "ai",
            "type": "text",
            "content": "Welcome to k1w1ProPlus! Select a project or create a new one to get started.",
            "collapsible": False,
            "language": None,
            "filename": None,
        }
    ]
    chat_input: str = ""
    is_processing: bool = False
    build_info: BuildStatus = {"status": "Pending", "progress": 0, "eta": "N/A"}

    @rx.event(background=True)
    async def handle_submit(self, form_data: dict):
        message_text = form_data["chat_input"]
        if not message_text or self.is_processing:
            return
        async with self:
            self.is_processing = True
            self.chat_input = ""
            self.messages.append(
                {
                    "id": len(self.messages) + 1,
                    "author": "user",
                    "type": "text",
                    "content": message_text,
                    "collapsible": False,
                    "language": None,
                    "filename": None,
                }
            )
        yield
        await asyncio.sleep(1)
        if "start build" in message_text.lower():
            yield ChatState.run_build_simulation
        elif "show code" in message_text.lower():
            async with self:
                self.messages.append(
                    {
                        "id": len(self.messages) + 1,
                        "author": "ai",
                        "type": "code",
                        "content": """import reflex as rx

class State(rx.State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

def index():
    return rx.el.div(
        rx.el.h1("Welcome to Reflex!"),
        rx.el.p(f"Count: {State.count}"),
        rx.el.button("Increment", on_click=State.increment),
        rx.el.button("Decrement", on_click=State.decrement),
    )
""",
                        "collapsible": True,
                        "language": "python",
                        "filename": "app/app.py",
                    }
                )
        else:
            async with self:
                self.messages.append(
                    {
                        "id": len(self.messages) + 1,
                        "author": "ai",
                        "type": "text",
                        "content": f"I received your command: '{message_text}'. I am not yet configured to handle this. Try 'start build' or 'show code'.",
                        "collapsible": False,
                        "language": None,
                        "filename": None,
                    }
                )
        async with self:
            self.is_processing = False

    @rx.event(background=True)
    async def run_build_simulation(self):
        steps = [
            ("Pending", 0, "10m 0s"),
            ("Running", 10, "9m 15s"),
            ("Running", 25, "7m 30s"),
            ("Running", 50, "5m 0s"),
            ("Running", 75, "2m 30s"),
            ("Running", 90, "0m 45s"),
            ("OK", 100, "0m 0s"),
        ]
        log_messages = [
            "[INFO] Starting Expo Application Services build...",
            "[INFO] Authenticating with EAS...",
            "[INFO] Creating build context...",
            "[WARN] Found deprecated 'expo-cli' setting. Please upgrade.",
            "[INFO] Uploading project files to EAS Storage...",
            "[INFO] Build queued. Waiting for a free build worker...",
            "[INFO] Build worker assigned. Starting build process...",
            "[LOG] > npm install",
            "[LOG] > prebuild",
            "[LOG] > expo prebuild --platform android --template bare-minimum",
            "[LOG] Creating native project directories (./android, ./ios)",
            "[LOG] > Build successful!",
            "[INFO] APK is available for download.",
        ]
        async with self:
            self.messages.append(
                {
                    "id": len(self.messages) + 1,
                    "author": "ai",
                    "type": "build_status",
                    "content": "",
                    "collapsible": False,
                    "language": None,
                    "filename": None,
                }
            )
        for status, progress, eta in steps:
            async with self:
                self.build_info = {"status": status, "progress": progress, "eta": eta}
                if progress > 0 and progress < 100 and log_messages:
                    self.messages.append(
                        {
                            "id": len(self.messages) + 1,
                            "author": "ai",
                            "type": "log",
                            "content": log_messages.pop(0),
                            "collapsible": False,
                            "language": None,
                            "filename": None,
                        }
                    )
            yield
            await asyncio.sleep(1.5)
        async with self:
            self.messages.append(
                {
                    "id": len(self.messages) + 1,
                    "author": "ai",
                    "type": "text",
                    "content": "Build finished! You can download the APK now.",
                    "collapsible": False,
                    "language": None,
                    "filename": None,
                }
            )
            self.is_processing = False

    def copy_to_clipboard(self, text: str):
        return rx.set_clipboard(text)

    def set_active_view(self, view: str):
        self.active_view = view