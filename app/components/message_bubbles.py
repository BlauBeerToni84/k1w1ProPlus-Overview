import reflex as rx
from app.states.chat_state import ChatState


def user_message(content: str) -> rx.Component:
    return rx.el.div(
        rx.el.p(content, class_name="text-white"),
        class_name="self-end max-w-2xl bg-gradient-to-r from-[#00AEEF] to-[#33CFFF] text-black px-4 py-3 rounded-2xl rounded-br-md shadow-lg",
    )


def ai_message(content: str) -> rx.Component:
    return rx.el.div(
        rx.icon("bot", size=24, class_name="text-[#33CFFF] flex-shrink-0"),
        rx.el.p(content, class_name="text-gray-300"),
        class_name="self-start flex gap-4 items-start max-w-3xl",
    )


def log_message(content: str) -> rx.Component:
    return rx.el.div(
        rx.el.p(content, class_name="font-['Source_Code_Pro'] text-sm text-gray-400"),
        class_name="self-start flex gap-4 items-start max-w-3xl ml-10",
    )


def code_message(message: dict) -> rx.Component:
    return rx.el.div(
        rx.icon("bot", size=24, class_name="text-[#33CFFF] flex-shrink-0 mt-2"),
        rx.el.details(
            rx.el.summary(
                rx.el.div(
                    rx.icon("file-code-2", size=16),
                    rx.el.p(message["filename"], class_name="font-semibold"),
                    class_name="flex items-center gap-2",
                ),
                rx.el.div(
                    rx.el.span(
                        message["language"],
                        class_name="text-xs font-medium bg-[#00AEEF]/20 text-[#33CFFF] px-2 py-1 rounded-md",
                    ),
                    rx.icon(
                        "chevron-down",
                        class_name="group-open:rotate-180 transition-transform",
                        size=20,
                    ),
                    class_name="flex items-center gap-4",
                ),
                class_name="flex items-center justify-between p-3 bg-gray-900/50 rounded-t-lg cursor-pointer list-none group",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.button(
                        rx.icon("copy", size=16),
                        "Copy",
                        on_click=lambda: ChatState.copy_to_clipboard(
                            message["content"]
                        ),
                        class_name="flex items-center gap-2 text-xs text-gray-400 hover:text-white px-3 py-1.5 bg-gray-800/50 rounded-md transition-colors",
                    ),
                    class_name="absolute top-2 right-2 opacity-50 hover:opacity-100 transition-opacity",
                ),
                rx.code_block(
                    message["content"],
                    language=message["language"],
                    theme="onedark",
                    custom_style={
                        "padding": "1.25rem",
                        "borderRadius": "0 0 0.5rem 0.5rem",
                        "backgroundColor": "#18181C",
                    },
                ),
                class_name="relative",
            ),
            class_name="border border-gray-700 rounded-lg shadow-md w-full max-w-2xl bg-[#1C1C22]",
            open=True,
        ),
        class_name="self-start flex gap-4 items-start w-full",
    )


def build_status_message() -> rx.Component:
    status_colors = {
        "Pending": "text-yellow-400",
        "Running": "text-[#33CFFF]",
        "OK": "text-green-400",
        "Fail": "text-red-400",
    }
    status_icon = {
        "Pending": rx.icon("loader-circle", class_name="animate-spin"),
        "Running": rx.icon("loader-circle", class_name="animate-spin"),
        "OK": rx.icon("check_check"),
        "Fail": rx.icon("circle_x"),
    }
    current_status = ChatState.build_info["status"]
    return rx.el.div(
        rx.icon("square_terminal", size=24, class_name="text-[#33CFFF] flex-shrink-0"),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.match(current_status, *status_icon.items()),
                    rx.el.h3(
                        f"Build Status: {current_status}",
                        class_name=f"font-['Space_Grotesk'] font-bold text-lg {status_colors.get(current_status, 'text-gray-400')}",
                    ),
                    class_name="flex items-center gap-3",
                ),
                rx.el.p(
                    f"ETA: {ChatState.build_info['eta']}",
                    class_name="text-sm text-gray-400 font-['Source_Code_Pro']",
                ),
                class_name="flex items-center justify-between",
            ),
            rx.el.div(
                rx.el.div(
                    class_name="bg-[#00AEEF] h-2 rounded-full transition-all duration-500",
                    style={"width": f"{ChatState.build_info['progress']}%"},
                ),
                class_name="w-full bg-gray-700 rounded-full h-2",
            ),
            rx.el.p(
                f"{ChatState.build_info['progress']}% Complete",
                class_name="text-right text-sm text-gray-400 mt-2",
            ),
            class_name="flex-1 space-y-3 p-4 border border-gray-700 rounded-lg bg-gray-900/50",
        ),
        class_name="self-start flex gap-4 items-start w-full",
    )