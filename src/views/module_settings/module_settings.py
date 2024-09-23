import flet as ft

def moduleSettings():
    return ft.Column(
        controls=[
            ft.Text("Settings", style="headlineLarge"),
            ft.Text("Configure system preferences, taxes, and user management."),
            ft.ElevatedButton("Change Preferences", on_click=lambda _: ft.snack_bar("Preferences updated!")),
            ft.ElevatedButton("Manage Users", on_click=lambda _: ft.snack_bar("User management opened!")),
        ]
    )
