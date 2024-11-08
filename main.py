import flet as ft

async def main(page: ft.Page):
    page.add(ft.ElevatedButton(
        content=ft.Text("kalyan ram"),
        on_click=lambda _:print("kalyan")
    ))
ft.app(main)