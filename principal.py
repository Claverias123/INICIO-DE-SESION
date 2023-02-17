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

    #------------- Función del botón ----------------------
    def botónGuardarNombreY (w):
        vVariable=[]
        i=open("archivo.txt", "r")

        for linea in i:
            t = linea.replace("\n","")
            vVariable.append(t)
        

        #Leer datos introducidos por teclado
        if (vVariable.count(tfnombre.value) > 0) and (vVariable.count(tfpassword.value) > 0):
            #Encontrada usu y pass
            
            dlg1=ft.AlertDialog(title=ft.Text("Inicio de sesión correcto"))
            dlg1.open = True                
            page.dialog = dlg1
        
        
        
        else:
            contador=0
            #No se encuentra
            dlg=ft.AlertDialog(title=ft.Text("Inicio de sesión incorrecto"))
            dlg.open = True                
            page.dialog = dlg
            contador=contador+1
            if contador>3:

                dlg3=ft.AlertDialog(title=ft.Text("Usuario bloqueado"))
                dlg3.open = True                
                page.dialog = dlg3        



        page.update()
        
           
        


            

        
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
    
    
 

    
    
    
    page.add(img,contDatos,boton)

ft.app(target=main,assets_dir="Imagenes")