import flet as ft
from controllers.snackbar_controller import SnackbarController

class ModuleSettings(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page  # Almacena la instancia de page

    def build(self):
        return ft.Column(
            controls=[
                ft.Text("Settings", style="headlineLarge"),
                ft.Text("Configure system preferences, taxes, and user management."),
                ft.ElevatedButton("Change Preferences", on_click=lambda _: ft.snack_bar("Preferences updated!")),
                ft.ElevatedButton("Manage Users", on_click=lambda _: ft.snack_bar("User management opened!")),
                ft.ElevatedButton("Cambiar tema", on_click=lambda _: self.theme_changed())  # Cambiar el tema
            ]
        )

    def theme_changed(self):
        # Usa self.page para acceder a la instancia de page
        if self.page.theme_mode == ft.ThemeMode.LIGHT:
            self.page.theme_mode = ft.ThemeMode.DARK
        else:
            self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.update()