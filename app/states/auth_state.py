import reflex as rx


class AuthState(rx.State):
    is_authenticated: bool = True
    user_email: str = "dev@k1w1.pro"