import flet as ft
def main(page: ft.Page):
    page.title = "Images Example"
    page.bgcolor=ft.colors.PURPLE_100
    page.padding = 50
    page.update()
ft.app(target=main)