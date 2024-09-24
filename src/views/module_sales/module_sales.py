import flet as ft
from controllers.snackbar_controller import SnackbarController

class ModuleSales(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        
    def build(self):
        return ft.Column(
            controls=[
                ft.Text("Sales Management", style="headlineLarge"),
                ft.Text("Manage sales, apply discounts, and view recent transactions."),
                ft.ElevatedButton("New Sale", on_click=lambda _: ft.snack_bar("New sale processed!")),
                ft.ElevatedButton("View Recent Sales", on_click=lambda _: ft.snack_bar("Recent sales displayed!")),
            ]
        )
