import reflex as rx
from app.states.chat_state import ChatState
from app.states.project_state import ProjectState
from app.components.message_bubbles import (
    user_message,
    ai_message,
    code_message,
    log_message,
    build_status_message,
)


def chat_view() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2(
                ProjectState.current_project.name,
                class_name="font-['Space_Grotesk'] text-xl font-bold",
            ),
            class_name="p-6 border-b border-gray-800 sticky top-0 bg-[#0A0A0F]/80 backdrop-blur-md z-10",
        ),
        rx.el.div(
            rx.foreach(ChatState.messages, render_message),
            class_name="flex-1 p-6 space-y-8",
        ),
        rx.el.div(
            rx.el.form(
                rx.el.input(
                    name="chat_input",
                    placeholder="Ask AI to do something... e.g., 'start build'",
                    key=ChatState.chat_input,
                    disabled=ChatState.is_processing,
                    class_name="w-full bg-transparent text-white placeholder-gray-500 outline-none px-4 py-3 rounded-full border border-gray-700 focus:ring-2 focus:ring-[#00AEEF]/50 focus:border-[#00AEEF]",
                    default_value=ChatState.chat_input,
                ),
                rx.el.button(
                    rx.cond(
                        ChatState.is_processing,
                        rx.icon("loader-circle", class_name="animate-spin", size=20),
                        rx.icon("arrow-up", size=20),
                    ),
                    type="submit",
                    disabled=ChatState.is_processing,
                    class_name="absolute right-3 top-1/2 -translate-y-1/2 bg-[#00AEEF] text-black p-2 rounded-full hover:bg-[#33CFFF] transition-colors disabled:bg-gray-600 disabled:cursor-not-allowed",
                ),
                on_submit=ChatState.handle_submit,
                reset_on_submit=True,
                class_name="relative w-full",
            ),
            class_name="p-6 border-t border-gray-800 sticky bottom-0 bg-[#0A0A0F]",
        ),
        class_name="h-full flex flex-col",
    )


def render_message(message: dict) -> rx.Component:
    return rx.match(
        message["type"],
        ("user", user_message(message["content"])),
        ("text", ai_message(message["content"])),
        ("code", code_message(message)),
        ("log", log_message(message["content"])),
        ("build_status", build_status_message()),
        ("error", ai_message(f"Error: {message['content']}")),
        rx.el.div(f"Unknown message type: {message['type']}"),
    )