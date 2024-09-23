import flet as ft
from views.inventory_view import inventory_view
from views.sales_view import sales_view

def main_view(page: ft.Page):
    # Main view UI components
    welcome_text = ft.Text("Welcome to the Store Management System", size=24)
    
    inventory_button = ft.ElevatedButton(
        text="Manage Inventory",
        on_click=lambda e: page.go("/inventory")
    )
    
    sales_button = ft.ElevatedButton(
        text="View Sales",
        on_click=lambda e: page.go("/sales")
    )

    return ft.Column(
        [
            welcome_text,
            inventory_button,
            sales_button
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

# Routing for different views
def route_change(page):
    if page.route == "/":
        page.views.clear()
        page.views.append(ft.View("/", [main_view(page)]))
    elif page.route == "/inventory":
        page.views.append(ft.View("/inventory", [inventory_view(page)]))
    elif page.route == "/sales":
        page.views.append(ft.View("/sales", [sales_view(page)]))
    page.update()
