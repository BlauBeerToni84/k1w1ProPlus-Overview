import reflex as rx
from pydantic import BaseModel
from typing import Literal
import logging
from app.states.auth_state import AuthState


class APIKeys(BaseModel):
    gemini: str = ""
    grok: str = ""
    cohere: str = ""
    openai: str = ""
    expo: str = ""
    github: str = ""
    firebase: str = ""


class SettingsState(rx.State):
    settings_json: str = rx.LocalStorage(name="k1w1_pro_plus_settings_v2")
    active_provider: Literal["Gemini", "Grok", "Cohere", "OpenAI"] = "Gemini"

    @rx.var
    def show_onboarding(self) -> bool:
        return not self.settings_json

    @rx.var
    def api_keys(self) -> APIKeys:
        if self.settings_json:
            try:
                return APIKeys.model_validate_json(self.settings_json)
            except Exception as e:
                logging.exception(f"Error validating settings JSON: {e}")
                return APIKeys()
        return APIKeys()

    @rx.event
    def save_settings(self, form_data: dict):
        current_settings = self.api_keys
        filtered_form_data = {
            k: v for k, v in form_data.items() if v and k != "chat_input"
        }
        new_keys = APIKeys(**filtered_form_data)
        self.settings_json = new_keys.model_dump_json()
        yield rx.toast("Settings saved successfully!")

    @rx.event
    def close_onboarding(self, form_data: dict):
        yield SettingsState.save_settings(form_data)