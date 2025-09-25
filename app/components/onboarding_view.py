import reflex as rx
from app.states.settings_state import SettingsState


def onboarding_view() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Welcome to k1w1ProPlus",
                    class_name="font-['Space_Grotesk'] text-2xl font-bold text-white",
                ),
                rx.el.p(
                    "Let's get your environment set up. Please enter your API keys below. You can change these later in the settings.",
                    class_name="text-gray-400 mt-2 mb-6",
                ),
            ),
            rx.el.form(
                rx.el.div(
                    settings_section(
                        "AI Provider Keys",
                        api_input("gemini", "Google Gemini API Key", "gem"),
                        api_input("openai", "OpenAI GPT API Key", "brain-circuit"),
                    ),
                    settings_section(
                        "DevOps Services",
                        api_input("expo", "Expo/EAS Token", "smartphone"),
                        api_input("github", "GitHub PAT", "github"),
                    ),
                    class_name="space-y-6",
                ),
                rx.el.div(
                    rx.el.button(
                        "Get Started",
                        type="submit",
                        class_name="w-full bg-[#00AEEF] text-black font-semibold px-6 py-3 rounded-lg hover:bg-[#33CFFF] transition-colors shadow-lg shadow-[#00AEEF]/10",
                    ),
                    class_name="mt-8",
                ),
                on_submit=SettingsState.close_onboarding,
            ),
            class_name="w-full max-w-4xl bg-[#111118] border border-gray-800 rounded-2xl p-8 shadow-2xl shadow-black/50",
        ),
        class_name="fixed inset-0 bg-black/80 backdrop-blur-sm flex items-center justify-center z-50 p-4",
    )


def settings_section(title: str, *children) -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            title,
            class_name="font-['Space_Grotesk'] text-lg font-semibold text-white mb-4",
        ),
        rx.el.div(*children, class_name="grid grid-cols-1 md:grid-cols-2 gap-6"),
    )


def api_input(
    name: str, label: str, icon_name: str, is_textarea: bool = False
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
                type="password",
                default_value=getattr(SettingsState.api_keys, name),
                placeholder=f"Enter your {label}",
                class_name="w-full bg-gray-900 border border-gray-700 rounded-lg pl-10 pr-4 py-2 text-sm text-gray-200 placeholder-gray-500 focus:ring-1 focus:ring-[#00AEEF] focus:border-[#00AEEF] outline-none",
            ),
            class_name="relative",
        ),
        class_name="w-full",
    )