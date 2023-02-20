import flet as ft
import time

def main(page: ft.Page):
    #------------------ Diseño de la página-----------------------
    page.title = "INICIO DE SESIÓN"
    page.bgcolor=ft.colors.PURPLE_300
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.window_height=850
    page.window_width=500
    page.update()
    cont = ft.TextField(value=1)
    #------------- fin del diseño de página ---------------

    #--------- función notificación usu y contr correcta-----------

    #------------- Función del botón ----------------------
    def botónGuardarNombreY (w):
        vVariable=[]
        contador = cont.value
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
            
            #No se encuentra
            if contador==1:
                dlg=ft.AlertDialog(title=ft.Text("Inicio de sesión incorrecto"))
                dlg.open = True                
                page.dialog = dlg
                contador=contador+1
            elif contador==2:
                    dlg2=ft.AlertDialog(title=ft.Text("Inicio de sesión incorrecto"))
                    dlg2.open = True                
                    page.dialog = dlg2
                    contador=contador+1
            elif contador==3:
                dlg3=ft.AlertDialog(title=ft.Text("Usuario bloqueado"))
                dlg3.open = True                
                page.dialog = dlg3
                page.update()
                time.sleep(3)
                page.window_close()      

            cont.value=contador


        page.update()
        
           
        


            

        
    page.update()                           
  



    #----------------- variables----------------------
    img = ft.Image(src=f"/imagenes/imagenkoi.png",
                    width=500,
                    height=500)

    #-----------requisitos de la contraseña----------------
    text_contra= ft.Text("\n \n \n  Requisitos de la contraseña: \n 1- Debe contener al menos 10 letras, incluyendo una mayúscula. \n 2- Debe contener al menos tres números. \n 3- Debe contener al menos un símbolo tal como ($).",size=13)
    
    #----------- fin de los requisitos---------------
    boton=ft.FilledButton("Iniciar sesión")
    tfnombre=ft.TextField(label="Nombre")
    tfpassword=ft.TextField(label="Contraseña")
    colDatos=ft.Column(controls=[tfnombre,tfpassword])

    row=ft.Row(controls=[(colDatos),(text_contra)])
    
    contDatos=ft.Container(content=row,width=200,padding=ft.padding.only(bottom=10)) 
    
 

    
    page.add(img,contDatos,boton)

ft.app(target=main,assets_dir="Imagenes")