import reflex as rx
from typing import Literal


class AuthState(rx.State):
    is_authenticated: bool = False
    user_email: str = ""
    error_message: str = ""
    is_loading: bool = False

    def login(self, form_data: dict):
        self.is_loading = True
        email = form_data["email"]
        password = form_data["password"]
        if password:
            self.is_authenticated = True
            self.user_email = email
            self.error_message = ""
        else:
            self.error_message = "Invalid credentials. Please try again."
        self.is_loading = False

    def signup(self, form_data: dict):
        self.is_loading = True
        email = form_data["email"]
        password = form_data["password"]
        if password:
            self.is_authenticated = True
            self.user_email = email
            self.error_message = ""
        else:
            self.error_message = "Signup failed. Please try again."
        self.is_loading = False

    @rx.event
    def logout(self):
        self.is_authenticated = False
        self.user_email = ""
        yield rx.redirect("/")