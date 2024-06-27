import flet as ft
import glob
import os
        

class PastProject(ft.Container):  
    def __init__(self, page:ft.Page,alignment: ft.Alignment | None = None,):
        super().__init__()
        self.page = page


        # self.alignment=ft.alignment.center
        self.pastproject_list = glob.glob('projects/*')
        past_project = []
        for project in self.pastproject_list:
            rect = []
            
            rect = ft.Container(
                ft.ElevatedButton(
                    content=ft.Column(
                        controls=[
                            ft.Text(value=project.split("\\")[-1], size=20),
                            ft.Text(value="path : "+project, size=10)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.MainAxisAlignment.START,
                        spacing=5,
                    ),
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)),
                    on_click=self.on_click_past_project,
                    width=5000
                ),
                alignment=ft.alignment.center_left,
                bgcolor=ft.colors.GREY,
                height=50,
            )
            rect.data=project

            if rect != []:
                past_project.append(rect)
            
        # print(self.pastproject_list)
        self.past_project = ft.Container(
            content=ft.Column(
                controls=past_project,
                scroll=ft.ScrollMode.HIDDEN,
            ),
            alignment=ft.alignment.top_center,
        )
        
        
        self.content = ft.Column(
            controls=[
                ft.TextField(value="",hint_text="過去のプロジェクトを検索", on_change=self.filter_project),
                self.past_project
            ],
        )
    
    def on_click_past_project(self, e):
        path = os.path.abspath(e.control.data)
        # print(path)
        self.page.client_storage.set("project_path",path)
        # print(self.page.client_storage.get("project_path"))
        self.page.go("/Page_Project")
        pass


    def filter_project(self, e):
        pass

