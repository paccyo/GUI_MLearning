from components._common.appheader import AppHeader
import flet as ft
import glob


class SignIn(ft.View):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page
        self.route = "/Page_SignIn"
        
        self.username = ""
        self.password = ""

        self.accounts = [s.split("\\")[-1][:-7] for s in glob.glob('accounts/*.paccyo')]  

        self.input_username = ft.TextField(label="user name", border=ft.InputBorder.UNDERLINE, hint_text="enter username" ,width=300, on_change=self.on_change_username)
        self.input_password = ft.TextField(label="password", border=ft.InputBorder.UNDERLINE, hint_text="enter password" ,width=300, on_change=self.on_change_password, password=True)
        self.error_username = ft.Text(value="",size=10,color=ft.colors.RED)
        self.error_password = ft.Text(value="",size=10,color=ft.colors.RED)

        self.user_app = ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text(value="User Login",size=20),
                    height=50,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.AMBER
                ),
                ft.Container(
                    content=self.input_username,
                    height=70,
                    alignment=ft.alignment.bottom_center,
                ),
                ft.Container(
                    content=self.error_username,
                    height=15,
                    alignment=ft.alignment.top_right,
                    padding=ft.padding.only(right=30)
                ),
                ft.Container(
                    content=self.input_password,
                    height=70,
                    alignment=ft.alignment.bottom_center,
                ),
                ft.Container(
                    content=self.error_password,
                    height=15,
                    alignment=ft.alignment.top_right,
                    padding=ft.padding.only(right=30)
                ),
                ft.Container(
                    content=ft.TextButton(text="sign up",
                                          on_click=self.on_click_sign_up),
                    height=40,
                    alignment=ft.Alignment(0.8, 1),
                ),
                ft.Container(
                    content=ft.CupertinoFilledButton(
                        content=ft.Text("Sign in"),
                        opacity_on_click=0.3,
                        on_click=self.on_click_sign_in,
                    ),
                    alignment=ft.alignment.bottom_center,
                ),
                ft.Container(
                    content=ft.Container(
                        content=ft.Row(
                            controls=[
                            ft.Text(value="  Google",color=ft.colors.BLACK),
                            ft.Container(content=ft.Image(src="packages\image\google_image.png",fit=ft.ImageFit.CONTAIN),width=30, height=30, border_radius=30)
                            ],
                        ),
                        width=100,
                        height=50,
                        bgcolor=ft.colors.WHITE,
                        border=ft.border.all(1, ft.colors.BLACK),
                        on_click=lambda e: print("Google Aouth clicked!"),
            
                    ),
                    height=90,
                    alignment=ft.alignment.center,
                )
            ],
        )

        self.controls = [
            AppHeader(self.page,title="ML/DS InterFace",bgcolor=ft.colors.LIME),
            ft.Container(
                content=ft.Container(
                    content=self.user_app,
                    border=ft.border.all(1, ft.colors.BLACK),
                    alignment=ft.Alignment(0,-1),
                    width=350,
                    height=475
                ),
                alignment=ft.Alignment(0,0),
                expand=True
            )
        ]

    def on_change_username(self, e):
        self.username = e.control.value

    def on_change_password(self, e):
        if len(self.password) < len(e.control.value):
            self.password = self.password+e.control.value[-1]
        elif len(e.control.value) < len(self.password):
            self.password = self.password[:-1]


    def on_click_sign_in(self, e):
        print(self.accounts)
        if self.username in self.accounts:
            with open("accounts/"+self.username+".paccyo","r",encoding="utf-8") as f:
                password = f.read()
            print(password,self.password)
            if self.password == password:
                self.page.go("/Page_MainMenu")
            else:
                self.error_password.value = "Different Pasword"
                self.error_password.update()
            self.error_username.value = ""
            self.error_username.update()
        else:
            self.error_username.value = "No account"
            self.error_password.value = ""
            self.error_username.update()
            self.error_password.update()
            

    def on_click_sign_up(self, e):
        self.page.go("/Page_SignUp")

