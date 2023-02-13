from utils.imports import *
import re
from utils.controls import (
    CustomText,CustomCard,CustomTextField,CustomElevatedButton
)
from utils.database import (
    auth,database
)
from models import UserModel
class Authentication:
    def __init__(self,page:Page):
        self.page=page

        # important variables 
        self.email_regex=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        # register
        self.username_ref=Ref[TextField]()
        self.register_email_ref=Ref[TextField]()
        self.register_password_ref=Ref[TextField]()

        #login
        self.login_email_ref=Ref[TextField]()
        self.login_password_ref=Ref[TextField]()

        # register validation bool 
        self.isusername_valid=False
        self.is_register_email_valid=False
        self.is_register_pass_valid=False

        # login valid bool 
        self.is_login_email_valid=False
        self.is_login_pass_valid=False


    def logout(self):
        try:
            self.page.client_storage.remove('auth-token')
            self.page.go('/login')
            self.page.update()
        except Exception as e:
            print(e)


    def register(self,e):
        username=self.username_ref.current.value
        email=self.register_email_ref.current.value
        password=self.register_password_ref.current.value
        print(username,email,password)

        # validate signup form
        if len(username)<=6:
            self.username_ref.current.error_text='username must be greater than or equal to 6 '
            self.isusername_valid=False
            self.username_ref.current.update()

        else:
            self.username_ref.current.error_text=None
            self.isusername_valid=True
            self.username_ref.current.update()
        if re.fullmatch(self.email_regex,str(email)):
            self.register_email_ref.current.error_text=None
            self.is_register_email_valid=True
            self.register_email_ref.current.update()

        else:
            self.register_email_ref.current.error_text='please enter valid email'
            self.is_register_email_valid=False
            self.register_email_ref.current.update()

        if len(password)<=6:
            self.register_password_ref.current.error_text='password length must be greater or equal to 6'
            self.is_register_pass_valid=False
            self.register_password_ref.current.update()

        else:
            self.register_password_ref.current.error_text=None
            self.is_register_pass_valid=True
            self.register_password_ref.current.update()

        if self.isusername_valid and self.is_register_email_valid and self.is_register_pass_valid:
            self.user=auth.create_user_with_email_and_password(email,password)
            self.userId=self.user['localId']
            if self.user:
                try:
                    self.userModel=UserModel(
                        userId=self.userId,
                        username=username,
                        email=email,
                        password=password,
                    )
                    database.child('users').child(self.userId).set(self.userModel.toMap())

                    self.page.snack_bar=SnackBar(
                        content=CustomText(
                            text='Account created successfully'
                        )
                    )
                    self.page.snack_bar.open=True
                    self.page.go('/login')
                    self.page.update()
                except Exception as e:
                    print(e)
                    
        else:
            print("signup form is not validated")


        

     



    def login(self,e):
        email=self.login_email_ref.current.value
        password=self.login_password_ref.current.value

        print(email,password)


        if re.fullmatch(self.email_regex,email):
            self.login_email_ref.current.error_text=None
            self.is_login_email_valid=True
            self.login_email_ref.current.update()

        else:
            self.login_email_ref.current.error_text='please enter valid email'
            self.is_login_email_valid=False
            self.login_email_ref.current.update()

        if len(password)<=6:
            self.login_password_ref.current.error_text='password must be greater than or equal to 6'
            self.is_login_pass_valid=False
            self.login_password_ref.current.update()
        else:
            self.login_password_ref.current.error_text=None
            self.is_login_pass_valid=True
            self.login_password_ref.current.update()

        if self.is_login_email_valid and self.is_login_pass_valid:
            print('login form is validated ')
            try:
                self.loginUser=auth.sign_in_with_email_and_password(email,password)
                refreshToken=self.loginUser['refreshToken']
                self.page.client_storage.set('auth-token',refreshToken)
                self.page.snack_bar=SnackBar(
                    content=CustomText(
                        'logged in successfully'
                    )
                )
                self.page.go('/mainpage')
                self.page.snack_bar.open=True
                self.page.update()
            except Exception as e:
                print(e)
                self.page.snack_bar=SnackBar(
                    content=CustomText(
                        text=str(e)
                    )
                )
                self.page.snack_bar.open=True
                self.page.update()






        else:
            print('login form is not validated')


        
            






    def signup_view(self):
        return View(
            '/',
            controls=[
                Container(
                    alignment=alignment.center,
                    content=CustomText(
                        'Authentication project',
                        size=30,
                        color='blue',
                    )
                ),
                Container(
                    alignment=alignment.center,
                    content=CustomCard(
                        width=500,
                        content=Column(
                            controls=[
                                Container(
                                    alignment=alignment.center,
                                    content=CustomText(
                                        'Sign Up',
                                        size=15,
                                        color='orange',
                                    )
                                ),
                                CustomTextField(
                                    
                                    hint_text='Username',
                                    prefix_icon=flet.icons.PERSON_OUTLINE,
                                    ref=self.username_ref,
                                ),
                                CustomTextField(
                                    hint_text='Email',
                                    prefix_icon=flet.icons.EMAIL_OUTLINED,
                                    ref=self.register_email_ref,
                                ),
                                CustomTextField(
                                    hint_text='Password',
                                    prefix_icon=flet.icons.LOCK_OUTLINE,
                                    isPassword=True,
                                    ref=self.register_password_ref

                                ),
                                CustomElevatedButton(
                                    'Sign Up',
                                    bgcolor='blue',
                                    color='white',
                                    onTap=self.register
                                ),
                               Row(
                                
                                controls=[
                                    CustomText(
                                        'Already Have an Account?'
                                    ),
                                    TextButton(
                                        'Login',
                                        on_click=lambda e:e.page.go('/login')
                                    )

                                ],
                                alignment='center'
                               )

                            ]
                        )
                    )
                )

            ]
        )

    def login_view(self):
        return View(
            '/login',
            controls=[
                Container(
                    alignment=alignment.center,
                    content=CustomText(
                        'Authentication project',
                        size=30,
                        color='blue',
                    )
                ),
                Container(
                    alignment=alignment.center,
                    content=CustomCard(
                        width=500,
                        content=Column(
                            controls=[
                                Container(
                                    alignment=alignment.center,
                                    content=CustomText(
                                        'Login',
                                        color='orange',
                                    )
                                ),
                
                                CustomTextField(
                                    hint_text='Email',
                                    prefix_icon=flet.icons.EMAIL_OUTLINED,
                                    ref=self.login_email_ref,
                                ),
                                CustomTextField(
                                    hint_text='Password',
                                    prefix_icon=flet.icons.LOCK_OUTLINE,
                                    isPassword=True,
                                    ref=self.login_password_ref
                                ),
                                CustomElevatedButton(
                                    'Login',
                                    bgcolor='blue',
                                    color='white',
                                    onTap=self.login,
                                ),
                               Row(
                                
                                controls=[
                                    CustomText(
                                        'Don\'t Have an Account?'
                                    ),
                                    TextButton(
                                        'Register',
                                        on_click=lambda e:e.page.go('/')
                                    )

                                ],
                                alignment='center'
                               )

                            ]
                        )
                    )
                )

            ]
        )
    
class MainPage:
    def __init__(self,page:Page):
        self.page=page
        self.authentication=Authentication(self.page)


    def logout(self,e):
        self.authentication.logout()


    def view(self):

        token=self.page.client_storage.get('auth-token')
        currentUser=auth.refresh(token)
        idToken=currentUser['idToken']
        accountInfo=auth.get_account_info(idToken)
        print('accountInfo',accountInfo)
        currentUser=database.child('users').child(accountInfo['users'][0]['localId']).get()
        currentUserModel=UserModel.fromMap(currentUser.val())

        return View(
            '/mainpage',
            appbar=AppBar(
                title=CustomText(currentUserModel.username),
                actions=[
                    IconButton(icon=flet.icons.LOGOUT,icon_color='red',on_click=self.logout)
                ]
            ),
            controls=[
                CustomText(
                    str(currentUserModel.toMap())
                ),
                CustomText(
                    str(database.get(token).val())
                )
            ]
        )