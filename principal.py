import flet as ft

def main(page: ft.Page):
    #------------------ Diseño de la página-----------------------
    page.title = "INICIO DE SESIÓN"
    page.bgcolor=ft.colors.PURPLE_300
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.window_height=850
    page.window_width=500
    page.update()
    #------------- fin del diseño de página ---------------

    #--------- función notificación usu y contr correcta-----------
    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()

    #------------- Función del botón ----------------------
    def botónGuardarNombreY (w):
        vVariable=[]
        i=open("archivo.txt", "r")

        for linea in i:
            t = linea.replace("\n","")
            vVariable.append(t)
        print (vVariable)

        if colDatos==vVariable:
            vVariable=[]
        print(open_dlg)


            

        
    page.update()                           
  



    #----------------- variables----------------------
    img = ft.Image(src=f"/imagenes/imagenkoi.png",
                    width=500,
                    height=500)

    boton=ft.FilledButton("Iniciar sesión", on_click=botónGuardarNombreY)
    tfnombre=ft.TextField(label="Nombre")
    tfpassword=ft.TextField(label="Contraseña", password= True ,can_reveal_password= True, width=500)
    colDatos=ft.Column(controls=[tfnombre,tfpassword])
    contDatos=ft.Container(content=colDatos, bgcolor=ft.colors.PURPLE_300,width=200,padding=ft.padding.only(bottom=100)) 
    dlg=ft.AlertDialog(title=ft.Text("Inicio de sesión correcto"))
 

    
    
    
    page.add(img,contDatos,boton)

ft.app(target=main,assets_dir="Imagenes")