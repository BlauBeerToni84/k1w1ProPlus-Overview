import reflex as rx
from app.components.main_layout import main_layout


def index() -> rx.Component:
    return main_layout()


app = rx.App(
    theme=rx.theme(
        appearance="light", has_background=True, radius="large", accent_color="cyan"
    ),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;700&family=Source+Code+Pro:wght@400;500&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index)