import flet as ft

version = "0.10"

def create_header(page):
    return ft.Row(
        controls=[
            ft.Image(src="assets/img/logo2.png", width=page.window_width * 0.05, height=page.window_height * 0.05, fit=ft.ImageFit.CONTAIN),
            ft.Text(f"Versión: {version}")
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )