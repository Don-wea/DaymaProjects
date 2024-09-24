import flet as ft

class SnackbarController:
    def __init__(self, page: ft.Page):
        self.page = page

    def show_snackbar(self, text, duration=2000):
        self.page.snack_bar = ft.SnackBar(
            content=ft.Text(text),
            duration=duration,
        )
        self.page.snack_bar.open = True
        self.page.update()