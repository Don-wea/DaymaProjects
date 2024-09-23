import flet as ft

def moduleSales():
    return ft.Column(
        controls=[
            ft.Text("Sales Management", style="headlineLarge"),
            ft.Text("Manage sales, apply discounts, and view recent transactions."),
            ft.ElevatedButton("New Sale", on_click=lambda _: ft.snack_bar("New sale processed!")),
            ft.ElevatedButton("View Recent Sales", on_click=lambda _: ft.snack_bar("Recent sales displayed!")),
        ]
    )
