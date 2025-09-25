import reflex as rx
from app.states.auth_state import AuthState


def login_view() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon("bot-message-square", size=48, class_name="text-[#00AEEF]"),
                rx.el.h1(
                    "k1w1ProPlus",
                    class_name="font-['Space_Grotesk'] text-4xl font-bold text-white mt-4",
                ),
                rx.el.p(
                    "Your No-Code DevOps Chat & Build Manager",
                    class_name="text-gray-400 mt-2",
                ),
                class_name="text-center mb-8",
            ),
            rx.el.form(
                rx.el.div(
                    auth_input("email", "Email Address", "mail", type="email"),
                    auth_input("password", "Password", "lock", type="password"),
                    class_name="space-y-4",
                ),
                rx.cond(
                    AuthState.error_message != "",
                    rx.el.div(
                        rx.icon("flag_triangle_right", size=16, class_name="mr-2"),
                        rx.el.p(AuthState.error_message, class_name="text-sm"),
                        class_name="flex items-center text-red-400 bg-red-500/10 p-3 rounded-lg mt-4",
                    ),
                    rx.fragment(),
                ),
                rx.el.div(
                    rx.el.button(
                        rx.cond(
                            AuthState.is_loading,
                            rx.icon("loader-circle", class_name="animate-spin"),
                            "Sign In",
                        ),
                        type="submit",
                        disabled=AuthState.is_loading,
                        on_click=AuthState.login,
                        class_name="w-full bg-[#00AEEF] text-black font-semibold px-6 py-3 rounded-lg hover:bg-[#33CFFF] transition-colors shadow-lg shadow-[#00AEEF]/10 disabled:bg-gray-600 disabled:cursor-not-allowed",
                    ),
                    rx.el.button(
                        "Sign Up",
                        on_click=AuthState.signup,
                        disabled=AuthState.is_loading,
                        class_name="w-full text-center text-gray-400 hover:text-white transition-colors py-2",
                    ),
                    class_name="mt-6 space-y-2",
                ),
            ),
            class_name="w-full max-w-md bg-[#111118] border border-gray-800 rounded-2xl p-8 shadow-2xl shadow-black/50",
        ),
        class_name="fixed inset-0 bg-[#0A0A0F] flex items-center justify-center z-50 p-4",
    )


def auth_input(
    name: str, label: str, icon_name: str, type: str = "text"
) -> rx.Component:
    return rx.el.div(
        rx.el.label(label, class_name="block text-sm font-medium text-gray-300 mb-2"),
        rx.el.div(
            rx.icon(
                icon_name,
                class_name="absolute left-3 top-1/2 -translate-y-1/2 text-gray-500",
                size=20,
            ),
            rx.el.input(
                name=name,
                type=type,
                placeholder=f"Enter your {label.lower()}",
                class_name="w-full bg-gray-900 border border-gray-700 rounded-lg pl-10 pr-4 py-2 text-sm text-gray-200 placeholder-gray-500 focus:ring-1 focus:ring-[#00AEEF] focus:border-[#00AEEF] outline-none",
            ),
            class_name="relative",
        ),
    )