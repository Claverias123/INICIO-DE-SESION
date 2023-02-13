import flet as ft
def main(page: ft.Page):
    page.title = "INICIO DE SESIÓN"
    page.bgcolor=ft.colors.PURPLE_300
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.window_height=500
    page.window_width=500
    page.update()
    
    img = ft.Image(src=f"/imagenes/imagenkoi.png",
        width=500,
        height=500,)

    tfnombre=ft.TextField(label="Nombre")
    tfpassword=ft.TextField(label="Contraseña")
    colDatos=ft.Column(controls=[tfnombre,tfpassword])
    contDatos=ft.Container(content=colDatos, bgcolor=ft.colors.PURPLE_300,width=200,padding=ft.padding.only(bottom=100))

    boton=ft.FilledButton("Iniciar sesión",ft.MaterialState.HOVERED: ft.colors.WHITE)
    
    page.add(img,contDatos,boton)


ft.app(target=main,assets_dir="Imagenes")