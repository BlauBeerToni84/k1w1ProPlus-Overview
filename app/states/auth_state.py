import reflex as rx


class AuthState(rx.State):
    is_authenticated: bool = True
    user_email: str = "dev@k1w1.pro"

    @rx.event
    def logout(self):
        self.is_authenticated = False
        return rx.redirect("/")