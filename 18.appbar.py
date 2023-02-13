import flet 
from flet import Page, AppBar, Text, Icon,icons, colors,IconButton


def main(page:Page):
    page.title='appbar tutorial'
    # page.bgcolor=colors.PINK_100
    page.theme_mode='light'
    page.appbar=AppBar(
        leading=Icon(
            name=icons.PERSON,
            size=50,
        ),
        title=Text(
            value='first page',

        ),
        # bgcolor=colors.ORANGE,
        leading_width=100,
        center_title=True,
        # color=colors.TEAL,
        elevation=40,
        actions=[
            IconButton(
                icon=icons.SETTINGS,

            ),
            IconButton(
                icon=icons.LOGOUT,
            ),
        
        ],
        toolbar_height=100,


        
    )

    page.update()

flet.app(target=main, view=flet.FLET_APP)
