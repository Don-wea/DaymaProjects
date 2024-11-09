import flet as ft
from controllers.snackbar_controller import SnackbarController as SBC

class ModuleSales(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        
    def build(self):
        return ft.Column(
            controls=[
                ft.Text("Gestor de Ventas", style="headlineLarge"),
                ft.Text("Cree ventas y verifique las que ya se han hecho."),
                ft.ElevatedButton("Agregar producto a la Venta", on_click=self.enter_product_by_id),
                ft.ElevatedButton("Ver ventas recientes", on_click=lambda _: SBC(self.page).show_snackbar("Recent sales displayed!")),
            ]
        )
        
        
        
    # Ventana en donde se pueda ver la camara para leer qr y devolver la informacion
    def qr_reader(self):
        pass
    
    # Conectar con un carrito de compra
    def add_sale_product(self, id, ammount):
        
        product = {
            "id": int(id),
            "ammount": ammount
        }
        
        print(product)
        
        pass
    
    
    
    def close_dialog(e, dialog):
            dialog.open = False
            e.page.update()
            
        
    def enter_product_by_id(self, e):
        
        product_id = ft.TextField(label="Ingrese ID", keyboard_type="number")
        qr_button  = ft.ElevatedButton("Escanear QR", on_click=lambda _: self.qr_reader)
        amount_product = ft.TextField(label="Ingrese cantidad", keyboard_type="number")

        dialog = ft.AlertDialog(
            title=ft.Text("Venta"),
            content=ft.Column(
                controls=[
                    product_id,
                    qr_button,
                    amount_product
                ]
            ),
            actions=[
                ft.TextButton("Agregar", on_click=lambda _: self.add_sale_product(product_id.value, amount_product.value)),
                ft.TextButton("Cancelar", on_click=lambda _: self.close_dialog(dialog))
            ]
        )

        e.page.dialog = dialog
        dialog.open = True
        e.page.update()
