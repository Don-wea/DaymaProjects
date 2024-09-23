import flet as ft
from views.main_view import main_view
from views.inventory_view import inventory_view
from views.sales_view import sales_view

def main(page: ft.Page):
    page.title = "Store Management System"
    page.window_width = 1000
    page.window_height = 600
    page.theme_mode = ft.ThemeMode.LIGHT

    # Routing for different views
    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(ft.View("/", [main_view(page)]))
        elif page.route == "/inventory":
            page.views.append(ft.View("/inventory", [inventory_view(page)]))
        elif page.route == "/sales":
            page.views.append(ft.View("/sales", [sales_view(page)]))
        page.update()

    # Set the route change handler
    page.on_route_change = route_change

    # Start with the main view
    page.go("/")

if __name__ == "__main__":
    ft.app(target=main)
