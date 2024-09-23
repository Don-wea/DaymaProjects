import flet as ft
from controllers.sales_controller import get_sales_data

def sales_view(page: ft.Page):
    # Fetch sales data
    sales_data = get_sales_data()

    # Create a table to display sales
    table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Date")),
            ft.DataColumn(ft.Text("Total Sale")),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(sale["date"])),
                    ft.DataCell(ft.Text(f"${sale['total']}")),
                ]
            ) for sale in sales_data
        ]
    )

    return ft.Column(
        [
            ft.Text("Sales Overview", size=20),
            table,
            ft.ElevatedButton(text="Back to Home", on_click=lambda e: page.go("/")),
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.START,
    )
