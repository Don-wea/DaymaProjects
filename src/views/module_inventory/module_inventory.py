import flet as ft

def moduleInventory():
    return ft.Column(
        controls=[
            ft.Text("Inventory Management", style="headlineLarge"),
            ft.Text("Manage your stock, add new items, update existing items, or check stock levels."),
            ft.ElevatedButton("Add New Item", on_click=lambda _: ft.snack_bar("New item added!")),
            ft.ElevatedButton("Update Item", on_click=lambda _: ft.snack_bar("Item updated!")),
            ft.ElevatedButton("Check Stock Levels", on_click=lambda _: ft.snack_bar("Current stock level is: X")),
        ]
    )
