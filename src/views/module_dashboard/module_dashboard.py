import flet as ft
from controllers.snackbar_controller import SnackbarController

class ModuleDashboard(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.Column(
            controls=[
                ft.Text("Dashboard", style="headlineLarge"),
                ft.Text("Welcome to your store management system dashboard."),
                ft.Text("Here you can see quick stats like recent sales, stock alerts, and more."),
            ]
        )