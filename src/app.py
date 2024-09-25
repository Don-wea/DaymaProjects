import flet as ft
from components.header import create_header
from views.modules import get_module_content
from components.bottom_nav import create_bottom_nav

def main(page: ft.Page):
    ft.AdaptiveControl = True

    # Function to switch between modules
    def switch_module(e):
        selected_module = e.control.data
        content_area.content = get_module_content(selected_module, page)  # Pasar 'page' aquí
        content_area.update()
    
    header = create_header(page)
    
    # Bottom navigation bar
    bottom_nav = create_bottom_nav(switch_module)

    # Initial content area to display the first module (Dashboard)
    content_area = ft.Container(content=get_module_content("dashboard", page), expand=True)

    # Layout with bottom navigation and content area
    mobile_layout = ft.Column(
        controls=[
            ft.Container(
                content=header,
                padding = ft.Padding(top=10,left=0,right=10,bottom=10),
                bgcolor = ft.colors.BLUE,
                border_radius = 100
            ),
            ft.Container(
                content=content_area,
                expand=True,
                padding = 20
            ),
            ft.Container(
                content=bottom_nav,
                padding=20
            )
        ],
        expand=True
    )

    page.theme_mode = ft.ThemeMode.DARK
    page.add(mobile_layout)

ft.app(target=main)