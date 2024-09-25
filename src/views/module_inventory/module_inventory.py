import flet as ft
import json
import os
from controllers.snackbar_controller import SnackbarController as SBC


class ModuleInventory(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.Column(
            controls=[
                ft.Text("Gestor de Inventario", style="headlineLarge"),
                ft.Text("Apartado destinado a gestionar la base de datos.\nAquí puede modificar el stock y agregar items inexistentes"),
                ft.ElevatedButton("Agregar Nuevo Item", on_click=self.add_new_item),
                ft.ElevatedButton("Actualizar Item", on_click=lambda _: SBC(self.page).show_snackbar("Actualizando Item...")),
                ft.ElevatedButton("Revisar stock", on_click=lambda _: SBC(self.page).show_snackbar("Revisando Stock...")),
            ]
        )
    
    
    # Function to save the new product information to a JSON file
    def save_product(self, product_data):
        # Define the JSON file path
        file_path = "data/items/products.json"
        
        # Check if the file already exists
        if os.path.exists(file_path):
            # Read existing data
            with open(file_path, "r") as file:
                products = json.load(file)
        else:
            products = []

        # Append the new product
        products.append(product_data)

        # Write the updated product list back to the JSON file
        with open(file_path, "w+") as file:
            json.dump(products, file, indent=4)
            
    def close_dialog(e, dialog):
            dialog.open = False
            e.page.update()  # Refresh the page to show the dialog

    # Function to handle the add new item button click
    def add_new_item(self, e):
        # Create input fields
        product_id_field = ft.TextField(label="Enter Product ID", keyboard_type="number")
        product_name_field = ft.TextField(label="Enter Product Name")
        category_field = ft.TextField(label="Enter Category")
        description_field = ft.TextField(label="Enter Description")
        
        # Create a dialog for user input
        dialog = ft.AlertDialog(
            title=ft.Text("Agregando Nuevo Item"),  # Corrected: title should be a Text control
            content=ft.Column(
                controls=[
                    product_id_field,
                    product_name_field,
                    category_field,
                    description_field
                ]
            ),
            actions=[
                ft.TextButton("Submit", on_click=lambda _: self.save_and_confirm(product_id_field.value, product_name_field.value, category_field.value, description_field.value, dialog)),
                ft.TextButton("Cancel", on_click=lambda _: self.close_dialog(dialog)),
            ],
        )

        # Show the dialog
        e.page.dialog = dialog  # Use the 'dialog' property to open it
        dialog.open = True
        e.page.update()  # Refresh the page to show the dialog

    # Function to save product and show confirmation message
    def save_and_confirm(self, product_id, product_name, category, description, dialog):
        # Create a product dictionary
        new_product = {
            "id": int(product_id),
            "name": product_name,
            "category": category,
            "description": description
        }

        # Save the product to a JSON file
        self.save_product(new_product)
        
        # Show confirmation message
        SBC(self.page).show_snackbar("Item añadido yeiii yipi lol")
        
        # Close the dialog
        self.close_dialog(dialog)
