import reflex as rx
from app.components.sidebar import sidebar
from app.components.chat_view import chat_view
from app.components.settings_view import settings_view
from app.components.onboarding_view import onboarding_view
from app.states.chat_state import ChatState
from app.states.settings_state import SettingsState


def main_layout() -> rx.Component:
    return rx.el.main(
        rx.cond(
            SettingsState.show_onboarding,
            onboarding_view(),
            rx.el.div(
                sidebar(),
                rx.el.div(
                    rx.match(
                        ChatState.active_view,
                        ("chat", chat_view()),
                        ("settings", settings_view()),
                        rx.el.div("Unknown View"),
                    ),
                    class_name="flex-1 h-screen overflow-y-auto",
                ),
                class_name="flex flex-row bg-[#0A0A0F] h-screen",
            ),
        ),
        class_name="font-['Inter'] text-white bg-[#0A0A0F]",
    )