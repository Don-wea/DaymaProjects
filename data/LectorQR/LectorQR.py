import flet as ft
import cv2
from pyzbar.pyzbar import decode

def scan_qr_or_barcode():
    """Captura y decodifica un QR o código de barras desde la cámara."""
    cap = cv2.VideoCapture(0)  
    while True:
        ret, frame = cap.read()
        if not ret:
            break

       
        decoded_objects = decode(frame)
        for obj in decoded_objects:
            cap.release()
            cv2.destroyAllWindows()
            return obj.data.decode("utf-8")  

        cv2.imshow("Escaneando... Presiona 'q' para salir.", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return None

def main(page: ft.Page):
    def on_scan_click(e):
        result = scan_qr_or_barcode()
        if result:
            result_text.value = f"Resultado: {result}"
        else:
            result_text.value = "No se detectó ningún código."
        page.update()


    page.title = "Lector de QR y Códigos de Barras"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

   
    scan_button = ft.ElevatedButton("Escanear Código", on_click=on_scan_click)
    result_text = ft.Text("Esperando escaneo...", size=20)

    page.add(
        ft.Column(
            [
                ft.Text("Lector de QR y Códigos de Barras", size=30, weight="bold", text_align="center"),
                scan_button,
                result_text,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
