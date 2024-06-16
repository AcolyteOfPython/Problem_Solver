import flet as ft
from flet import TextAlign
from assets.mathematics import simplification, solve_ation, differentiation, integration, factorisation
from flet_core.control_event import ControlEvent


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    def simplify_expr(e: ControlEvent):
        text.value = simplification(textbox.value)
        page.update()

    def solve_equation(e: ControlEvent):
        text2.value = solve_ation(textbox2.value)
        page.update()

    def calculus_diff(e):
        text3.value = differentiation(textbox3.value)
        page.update()

    def calculus_int(e):
        text3.value = integration(textbox3.value)
        page.update()

    def factorise(e):
        text4.value = factorisation(textbox4.value)
        page.update()

    page.Title = "Mathematics"
    page.VerticalAlignment = ft.MainAxisAlignment.CENTER
    textbox = ft.TextField(value="", text_align=TextAlign.CENTER,
                           width=250, hint_text="Enter expression here please", helper_text="eg, 3x+5x^2-2+3x^2")
    text = ft.Text("")
    button = ft.ElevatedButton(text="Simplify", on_click=simplify_expr)
    textbox2 = ft.TextField(value="", text_align=TextAlign.CENTER,
                            width=250, hint_text="Enter equation here please", helper_text="eg, 3x=5x+2")
    button2 = ft.ElevatedButton(text="Solve", on_click=solve_equation)
    text2 = ft.Text("")
    textbox3 = ft.TextField(value="", text_align=TextAlign.CENTER,
                            width=250, hint_text="Enter expression here please", helper_text="eg, 3x+2")

    buttons = ft.Row(controls=[ft.ElevatedButton(text="Differentiate", on_click=calculus_diff),
                     ft.ElevatedButton(text="Integrate", on_click=calculus_int)],
                     alignment=ft.MainAxisAlignment.CENTER)
    text3 = ft.Text("")
    textbox4 = ft.TextField(value="", text_align=TextAlign.CENTER,
                            width=250, hint_text="Enter expression here please", helper_text="eg, 3x+3y")
    button4 = ft.ElevatedButton(text="Factorise", on_click=factorise)
    text4 = ft.Text("")
    page.add(textbox, button, text, textbox2, button2, text2, textbox3, buttons, text3, textbox4, button4,
             text4)
    page.update()


if __name__ == '__main__':
    ft.app(target=main)
