import flet as ft
import json
import os
from controllers.snackbar_controller import SnackbarController


class ModuleInventory(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.Column(
            controls=[
                ft.Text("Inventory Management", style="headlineLarge"),
                ft.Text("Manage your stock, add new items, update existing items, or check stock levels."),
                ft.ElevatedButton("Add New Item", on_click=self.add_new_item),
                ft.ElevatedButton("Update Item", on_click=lambda _: ft.snack_bar("Item updated!")),
                ft.ElevatedButton("Check Stock Levels", on_click=lambda _: ft.snack_bar("Current stock level is: X")),
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
        with open(file_path, "w") as file:
            json.dump(products, file, indent=4)

    # Function to handle the add new item button click
    def add_new_item(self, e):
        # Create input fields
        product_id_field = ft.TextField(label="Enter Product ID", keyboard_type="number")
        product_name_field = ft.TextField(label="Enter Product Name")
        category_field = ft.TextField(label="Enter Category")
        description_field = ft.TextField(label="Enter Description")

        # Create a dialog for user input
        dialog = ft.AlertDialog(
            title=ft.Text("Add New Item"),  # Corrected: title should be a Text control
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
                ft.TextButton("Cancel", on_click=lambda _: dialog.close()),
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
        ft.snack_bar("New item added!", duration=2)
        
        # Close the dialog
        dialog.close()
