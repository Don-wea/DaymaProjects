import flet as ft
from controllers.snackbar_controller import SnackbarController

class ModuleCustomers(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.Column(
            controls=[
                ft.Text("Customer Management", style="headlineLarge"),
                ft.Text("Manage your customers, loyalty programs, and customer details."),
                ft.ElevatedButton("Add New Customer", on_click=lambda _: self.add_new_item()),
                ft.ElevatedButton("View Customer List", on_click=lambda _: self.view_customer_list()),

            ]
        )

    def add_new_item(self):
        #Lógica de añadir cliente
        SnackbarController(self.page).show_snackbar("Hola mundo")


    def view_customer_list(self):
        #Lógica de ver clientes
        SnackbarController(self.page).show_snackbar("Hola mundo 2") #snackbar solo para probar funcionamiento
