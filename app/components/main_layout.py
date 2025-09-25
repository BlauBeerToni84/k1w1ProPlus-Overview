import reflex as rx
from app.components.sidebar import sidebar
from app.components.chat_view import chat_view
from app.components.settings_view import settings_view
from app.components.onboarding_view import onboarding_view
from app.components.login_view import login_view
from app.states.base_state import State
from app.states.settings_state import SettingsState
from app.states.auth_state import AuthState


def main_layout() -> rx.Component:
    return rx.el.main(
        rx.cond(
            AuthState.is_authenticated,
            rx.el.div(
                rx.el.div(
                    sidebar(),
                    rx.el.div(
                        rx.match(
                            State.active_view,
                            ("chat", chat_view()),
                            ("settings", settings_view()),
                            rx.el.div("Unknown View"),
                        ),
                        class_name="flex-1 h-screen overflow-y-auto",
                    ),
                    class_name="flex flex-row bg-[#0A0A0F]",
                ),
                rx.cond(
                    SettingsState.show_onboarding, onboarding_view(), rx.fragment()
                ),
            ),
            login_view(),
        ),
        class_name="font-['Inter'] text-white",
    )