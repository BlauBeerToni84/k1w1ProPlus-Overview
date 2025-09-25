import reflex as rx
from app.states.chat_state import ChatState
from app.states.project_state import ProjectState
from app.states.auth_state import AuthState


def sidebar() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("bot-message-square", size=32, class_name="text-[#00AEEF]"),
            rx.el.h1(
                "k1w1ProPlus",
                class_name="font-['Space_Grotesk'] text-2xl font-bold text-white",
            ),
            class_name="flex items-center gap-3 p-6 border-b border-gray-800",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "Projects",
                        class_name="font-['Space_Grotesk'] text-sm font-semibold uppercase text-gray-500 px-4 pt-4 pb-2",
                    ),
                    rx.el.button(
                        rx.icon("plus", size=16),
                        "New Project",
                        on_click=ProjectState.create_project,
                        class_name="text-xs flex items-center gap-2 text-gray-400 hover:text-white transition-colors",
                    ),
                    class_name="flex justify-between items-center",
                ),
                rx.el.input(
                    placeholder="Search projects...",
                    on_change=ProjectState.set_project_search_query,
                    class_name="mx-4 my-2 w-[calc(100%-2rem)] bg-gray-900 border border-gray-700 rounded-lg px-3 py-2 text-sm placeholder-gray-500 focus:ring-1 focus:ring-[#00AEEF] focus:border-[#00AEEF] outline-none",
                ),
                rx.el.div(
                    rx.foreach(ProjectState.filtered_projects, project_item),
                    class_name="flex flex-col gap-1 px-4 overflow-y-auto",
                ),
                class_name="flex-1 flex flex-col",
            )
        ),
        rx.el.div(
            rx.el.div(
                rx.el.button(
                    rx.icon("message-circle", size=20),
                    "Chat",
                    on_click=lambda: ChatState.set_active_view("chat"),
                    class_name=rx.cond(
                        ChatState.active_view == "chat",
                        "flex items-center gap-3 w-full text-left px-4 py-3 rounded-lg bg-[#00AEEF]/10 text-[#33CFFF] font-semibold",
                        "flex items-center gap-3 w-full text-left px-4 py-3 rounded-lg text-gray-400 hover:bg-gray-800/50 hover:text-white transition-colors",
                    ),
                ),
                rx.el.button(
                    rx.icon("settings", size=20),
                    "Settings",
                    on_click=lambda: ChatState.set_active_view("settings"),
                    class_name=rx.cond(
                        ChatState.active_view == "settings",
                        "flex items-center gap-3 w-full text-left px-4 py-3 rounded-lg bg-[#00AEEF]/10 text-[#33CFFF] font-semibold",
                        "flex items-center gap-3 w-full text-left px-4 py-3 rounded-lg text-gray-400 hover:bg-gray-800/50 hover:text-white transition-colors",
                    ),
                ),
                class_name="flex flex-col gap-2 p-4 border-t border-gray-800",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        AuthState.user_email,
                        class_name="font-semibold text-white text-sm truncate",
                    ),
                    rx.el.p("Online", class_name="text-xs text-green-400"),
                    class_name="flex-1 min-w-0",
                ),
                class_name="p-4 border-t border-gray-800 flex items-center gap-4",
            ),
        ),
        class_name="w-80 h-screen bg-[#111118] border-r border-gray-800 flex flex-col",
    )


def project_item(project: dict) -> rx.Component:
    return rx.el.button(
        rx.el.div(
            rx.el.p(project["name"], class_name="font-medium text-sm truncate"),
            rx.el.p(project["last_opened"], class_name="text-xs text-gray-500"),
            class_name="flex-1 text-left",
        ),
        class_name=rx.cond(
            ProjectState.current_project_id == project["id"],
            "w-full flex items-center p-2 rounded-md bg-gray-700/50 text-white",
            "w-full flex items-center p-2 rounded-md text-gray-400 hover:bg-gray-800/50 hover:text-white transition-colors",
        ),
        on_click=lambda: ProjectState.select_project(project["id"]),
    )