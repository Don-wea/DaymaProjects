import flet as ft

def moduleDashboard():
    return ft.Column(
        controls=[
            ft.Text("Dashboard", style="headlineLarge"),
            ft.Text("Welcome to your store management system dashboard."),
            ft.Text("Here you can see quick stats like recent sales, stock alerts, and more."),
        ]
    )
