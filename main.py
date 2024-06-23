from components.page_home import Home
from components.page_project import Project
from components.page_createproject import CreateProject
from components.page_userapp import UserApp
from components.page_signapp import SignApp

import flet as ft


def main(page: ft.Page):
    # Define the UI components
    page.title = "Neural Network Designer"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.theme_mode = "light"

    def route_change(handler):
        t_route = ft.TemplateRoute(handler.route)
        
        if t_route.match("/Page_UserApp"):
            page.views.clear()
            page.views.append(UserApp(page))
        elif t_route.match("/Page_SignApp"):
            page.views.append(SignApp(page))
        elif t_route.match("/Page_Home"):
            page.views.clear()
            page.views.append(Home(page))
        elif t_route.match("/Page_Project"):
            page.views.clear()
            page.views.append(Project(page))
        elif t_route.match("/Page_CreateProject"):
            page.views.append(CreateProject(page))
        page.update()

    def view_pop(handler):
        page.views.pop()  # 1つ前に戻る
        page.go("/back")

    # 戻る時のロジック設定
    page.on_view_pop = view_pop

    # ルート変更時のロジック設定
    page.on_route_change = route_change

    # page.go("/Page_UserApp")
    page.go("/Page_Home")

# Start the app
# ft.app(target=main, port=8550)
# ft.app(target=main, port=8550, view=ft.WEB_BROWSER)