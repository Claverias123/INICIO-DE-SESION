import flet as ft

def main(page: ft.Page):
    page.title = "Inicio de sesión"
       
    #page.vertical_alignment=ft.MainAxisAlignment.CENTER  *****************  para ponerlo en el centro   **************
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.bgcolor=ft.colors.PURPLE_300
    img = ft.Image(src=f"/imagenes/imagenkoi.png",
            width=500,
            height=500,)
            #fit=ft.ImageFit.CONTAIN,)
    

    page.add(img)
    page.update()
   












   
    #----------Fin definiciones de variables----------------

ft.app(target=main,assets_dir="Imagenes")