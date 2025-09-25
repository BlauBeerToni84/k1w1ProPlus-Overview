import reflex as rx
from app.states.settings_state import SettingsState


def settings_view() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2("Settings", class_name="font-['Space_Grotesk'] text-xl font-bold"),
            rx.el.p(
                "Manage your API keys and application settings.",
                class_name="text-gray-400",
            ),
            class_name="p-6 border-b border-gray-800",
        ),
        rx.el.form(
            rx.el.div(
                settings_section(
                    "AI Provider Keys",
                    api_input("gemini", "Google Gemini API Key", "gem"),
                    api_input("grok", "Grok API Key", "cloud"),
                    api_input("cohere", "Cohere Command-R API Key", "message-circle"),
                    api_input("openai", "OpenAI GPT API Key", "brain-circuit"),
                ),
                settings_section(
                    "DevOps Services",
                    api_input("expo", "Expo/EAS Token", "smartphone"),
                    api_input("github", "GitHub PAT", "github"),
                    api_input(
                        "firebase",
                        "Firebase WebConfig (JSON)",
                        "flame",
                        is_textarea=True,
                    ),
                ),
                class_name="space-y-8",
            ),
            rx.el.div(
                rx.el.button(
                    "Save Settings",
                    type="submit",
                    class_name="bg-[#00AEEF] text-black font-semibold px-6 py-3 rounded-lg hover:bg-[#33CFFF] transition-colors shadow-lg shadow-[#00AEEF]/10",
                ),
                class_name="p-6 border-t border-gray-800 mt-8",
            ),
            on_submit=SettingsState.save_settings,
        ),
        class_name="p-6",
    )


def settings_section(title: str, *children) -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            title,
            class_name="font-['Space_Grotesk'] text-lg font-semibold text-white mb-4",
        ),
        rx.el.div(*children, class_name="grid grid-cols-1 md:grid-cols-2 gap-6"),
        class_name="p-6 bg-[#111118] border border-gray-800 rounded-xl",
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
            rx.cond(
                is_textarea,
                rx.el.textarea(
                    name=name,
                    default_value=getattr(SettingsState.api_keys, name),
                    placeholder=f"Enter your {label}",
                    rows=4,
                    class_name="w-full bg-gray-900 border border-gray-700 rounded-lg pl-10 pr-4 py-2 text-sm text-gray-200 placeholder-gray-500 focus:ring-1 focus:ring-[#00AEEF] focus:border-[#00AEEF] outline-none font-['Source_Code_Pro'] resize-none",
                ),
                rx.el.input(
                    name=name,
                    type="password",
                    default_value=getattr(SettingsState.api_keys, name),
                    placeholder=f"Enter your {label}",
                    class_name="w-full bg-gray-900 border border-gray-700 rounded-lg pl-10 pr-4 py-2 text-sm text-gray-200 placeholder-gray-500 focus:ring-1 focus:ring-[#00AEEF] focus:border-[#00AEEF] outline-none",
                ),
            ),
            class_name="relative",
        ),
        class_name="w-full",
    )