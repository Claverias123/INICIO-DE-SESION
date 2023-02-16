import flet as ft

def main(page: ft.Page):
    #------------------ Diseño de la página-----------------------
    page.title = "INICIO DE SESIÓN"
    page.bgcolor=ft.colors.PURPLE_300
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.window_height=500
    page.window_width=500
    page.update()
    #------------- fin del diseño de página ---------------

    #------------- Función del botón ---------------------
    
  


    #----------------- variables----------------------
    img = ft.Image(src=f"/imagenes/imagenkoi.png",
                    width=500,
                    height=500)

    #-----------requisitos de la contraseña----------------
    text_contra= ft.Text("\n \n \n  Requisitos de la contraseña: \n 1- Debe cintener al menos 10 letras, incluyendo una mayúscula. \n 2- Debe contener al menos tres números. \n 3- Debe contener al menos un símbolo tal como ($).",size=13)
    
    #----------- fin de los requisitos---------------
    boton=ft.FilledButton("Iniciar sesión")
    tfnombre=ft.TextField(label="Nombre")
    tfpassword=ft.TextField(label="Contraseña")
    colDatos=ft.Column(controls=[tfnombre,tfpassword])
    contDatos=ft.Container(content=colDatos, bgcolor=ft.colors.PURPLE_300,width=200,padding=ft.padding.only(bottom=10)) 
    row=ft.Row(controls=[(contDatos),(text_contra)],)
    
    
    
    page.add(img,row,boton)

ft.app(target=main,assets_dir="Imagenes")