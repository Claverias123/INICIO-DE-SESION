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
    def botónGuardarNombreY ():
        vNombre=[]
        f=open("Equipos.txt", "r")

        linea = f.readline()
        vNombre = linea.split(sep=";")
            

        f.close()
        return vNombre
    page.update()                           
  


    #----------------- variables----------------------
    img = ft.Image(src=f"/imagenes/imagenkoi.png",
                    width=500,
                    height=500)

    boton=ft.FilledButton("Iniciar sesión")
    tfnombre=ft.TextField(label="Nombre")
    tfpassword=ft.TextField(label="Contraseña", password= True ,can_reveal_password= True, width=500)
    colDatos=ft.Column(controls=[tfnombre,tfpassword])
    contDatos=ft.Container(content=colDatos, bgcolor=ft.colors.PURPLE_300,width=200,padding=ft.padding.only(bottom=100)) 
 
    
    
    
    page.add(img,contDatos,boton)

ft.app(target=main,assets_dir="Imagenes")