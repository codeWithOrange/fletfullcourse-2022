from utils.imports import *
from pages import (
    Authentication,MainPage
)
class Software:
    def __init__(self,page:Page):
        self.page=page

        # pages instance/objects
        self.authentication=Authentication(
            self.page
        )
        self.mainpage=MainPage(self.page)

    def route_change(self,route):
        if self.page.route=='/':
            self.page.views.append(
                self.authentication.signup_view()
            )
        elif self.page.route=='/login':
            self.page.views.append(
                self.authentication.login_view()
            )
        elif self.page.route=='/mainpage':
            self.page.views.clear()
            self.page.views.append(
                self.mainpage.view()
            )
        else:
            self.page.add(
                Text(
                    'no page found'
                )
            )

        self.page.update()

    def pop_view(self,route):
        self.page.views.pop()
        top_view=self.page.views[-1]
        self.page.go(top_view.route)
        self.page.update()

    


def main(page:Page):
    page.title='Authentication project with firebase'
    page.theme_mode='light'
    page.padding=0

    refresh_token:str=page.client_storage.get('auth-token')
    if refresh_token:
        page.go('/mainpage')
        page.update()
    else:
        page.go('/')
        page.update()

    
    # instance of software class
    soft=Software(page=page)
    page.on_route_change=soft.route_change
    page.on_view_pop=soft.pop_view
    page.go(page.route)



if __name__=='__main__':
    flet.app(target=main,view=flet.FLET_APP)
