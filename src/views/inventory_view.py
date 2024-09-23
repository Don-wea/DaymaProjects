import flet as ft
from controllers.inventory_controller import get_inventory_data

def inventory_view(page: ft.Page):
    # Fetch inventory data
    inventory_data = get_inventory_data()

    # Create a table to display inventory
    table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Item Name")),
            ft.DataColumn(ft.Text("Stock")),
            ft.DataColumn(ft.Text("Price")),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(item["name"])),
                    ft.DataCell(ft.Text(str(item["stock"]))),
                    ft.DataCell(ft.Text(f"${item['price']}")),
                ]
            ) for item in inventory_data
        ]
    )

    return ft.Column(
        [
            ft.Text("Inventory Management", size=20),
            table,
            ft.ElevatedButton(text="Back to Home", on_click=lambda e: page.go("/")),
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.START,
    )
