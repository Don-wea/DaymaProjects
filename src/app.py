import flet as ft
from views.modules import get_module_content

def main(page: ft.Page):

    ft.AdaptiveControl=True
    # Function to switch between modules
    def switch_module(e):
        selected_module = e.control.data
        content_area.content = get_module_content(selected_module)
        content_area.update()

    # Bottom navigation bar
    bottom_nav = ft.Row(
        controls=[
            ft.IconButton(icon=ft.icons.DASHBOARD, on_click=switch_module, data="dashboard", tooltip="Dashboard"),
            ft.IconButton(icon=ft.icons.INVENTORY, on_click=switch_module, data="inventory", tooltip="Inventory"),
            ft.IconButton(icon=ft.icons.SELL, on_click=switch_module, data="sales", tooltip="Sales"),
            ft.IconButton(icon=ft.icons.PEOPLE, on_click=switch_module, data="customers", tooltip="Customers"),
            ft.IconButton(icon=ft.icons.SETTINGS, on_click=switch_module, data="settings", tooltip="Settings"),
        ],
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        expand=True
    )

    # Initial content area to display the first module (Dashboard)
    content_area = ft.Container(content=get_module_content("dashboard"), expand=True)

    # Layout with bottom navigation and content area
    mobile_layout = ft.Column(
        controls=[
            content_area,
            bottom_nav,
        ],
        expand=True
    )

    page.add(mobile_layout)

ft.app(target=main)
