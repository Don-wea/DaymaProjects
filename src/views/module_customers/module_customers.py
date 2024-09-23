import flet as ft

def moduleCustomers():
    return ft.Column(
        controls=[
            ft.Text("Customer Management", style="headlineLarge"),
            ft.Text("Manage your customers, loyalty programs, and customer details."),
            ft.ElevatedButton("Add New Customer", on_click=lambda _: ft.snack_bar("Customer added!")),
            ft.ElevatedButton("View Customer List", on_click=lambda _: ft.snack_bar("Displaying customer list...")),
        ]
    )
