import reflex as rx
from typing import TypedDict
import datetime


class Project(TypedDict):
    id: str
    name: str
    last_opened: str


class ProjectState(rx.State):
    projects: list[Project] = [
        {"id": "proj_1", "name": "k1w1-pro-plus-app", "last_opened": "2 hours ago"},
        {"id": "proj_2", "name": "personal-website", "last_opened": "1 day ago"},
        {"id": "proj_3", "name": "data-pipeline-job", "last_opened": "3 days ago"},
    ]
    current_project_id: str = ""
    project_search_query: str = ""

    @rx.var
    def current_project(self) -> Project | None:
        if not self.current_project_id:
            return {"id": "", "name": "No Project Selected", "last_opened": ""}
        for p in self.projects:
            if p["id"] == self.current_project_id:
                return p
        return None

    @rx.var
    def filtered_projects(self) -> list[Project]:
        if not self.project_search_query:
            return self.projects
        return [
            p
            for p in self.projects
            if self.project_search_query.lower() in p["name"].lower()
        ]

    def select_project(self, project_id: str):
        self.current_project_id = project_id

    def create_project(self):
        new_id = f"proj_{len(self.projects) + 1}"
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_project = {
            "id": new_id,
            "name": f"New Project {len(self.projects) + 1}",
            "last_opened": "Just now",
        }
        self.projects.append(new_project)
        self.current_project_id = new_id