import flet as ft

def main(page: ft.Page):
    page.title = "Inicio de sesión"
       
    
    img = ft.Image(src=f"Inicioimagen.jpg",
            width=100,
            height=100,
            fit=ft.ImageFit.CONTAIN,)
    images = ft.Row(expand=1, wrap=False, scroll="always")

    page.add(img, images)
   
   












   
    #----------Fin definiciones de variables----------------

ft.app(target=main)