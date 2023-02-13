import flet as ft
def main(page: ft.Page):
    page.title = "INICIO DE SESIÓN"
    page.bgcolor=ft.colors.PURPLE_300
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.window_height=500
    page.window_width=500
    page.update()


    tfnombre=ft.TextField(label="Nombre")
    tfpassword=ft.TextField(label="Contraseña")
    colDatos=ft.Column(controls=[tfnombre,tfpassword])
    contDatos=ft.Container(content=colDatos, bgcolor=ft.colors.PURPLE_100,width=100,padding=ft.padding.only(bottom=50))


    txt=ft.Text("Hola")
    page.add(txt,contDatos)


ft.app(target=main)