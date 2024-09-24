import flet as ft

def create_bottom_nav(switch_module):
    return ft.Row(
        controls=[
            ft.Column([
                ft.IconButton(icon=ft.icons.DASHBOARD, on_click=switch_module, data="dashboard", tooltip="Dashboard"),
                ft.Text("Dashboard", size=12)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
            ft.Column([
                ft.IconButton(icon=ft.icons.INVENTORY, on_click=switch_module, data="inventory", tooltip="Inventory"),
                ft.Text("Inventory", size=12)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
            ft.Column([
                ft.IconButton(icon=ft.icons.SELL, on_click=switch_module, data="sales", tooltip="Sales"),
                ft.Text("Sales", size=12)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
            ft.Column([
                ft.IconButton(icon=ft.icons.PEOPLE, on_click=switch_module, data="customers", tooltip="Customers"),
                ft.Text("Customers", size=12)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
            ft.Column([
                ft.IconButton(icon=ft.icons.SETTINGS, on_click=switch_module, data="settings", tooltip="Settings"),
                ft.Text("Settings", size=12)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
        ],
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
    )
