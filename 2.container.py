
from turtle import color
import flet 
from flet import (
    Container, Text, Page,colors,alignment,padding,border_radius,LinearGradient,
    border,
    margin, 
)

def hello(e):
    print(e)
    print('this is container')


def main(page:Page):
    page.title='container'
    page.padding=0
    page.bgcolor=colors.CYAN_400
    # page.vertical_alignment='center'
    # page.horizontal_alignment='center'

    c=Container(
        content=Text(
            value='hello this',
            color='blue',
            size=40,
        ),
        # bgcolor=colors.RED_400,
        width=200,
        height=200,
     
        # alignment=alignment.center,
        # padding=padding.symmetric(horizontal=50,vertical=50),
        padding=padding.only(top=50,left=50),
        ink=True,
        visible=True,
        border_radius=10,
        # border_radius=border_radius.only(topLeft=20,bottomRight=20),
        # border_radius=border_radius.all(value=20),
        on_click=lambda e:hello(e),
        # on_hover=lambda e:hello(e),
        # on_long_press=lambda e:hello(e)
        gradient=LinearGradient(
            tile_mode='mirror',
            begin=alignment.bottom_right,
            end=alignment.top_right,
            # stops=[
            #     0.1, 
            #     0.2, 
            #     0.3, 
            #     0.5,
            #     0.4
            # ],
            colors=[
                'blue',
                'red', 
                'purple', 
                'pink',
                'lightblue'
            ],
           
        ),
        # border=border.all(width=5,color=colors.DEEP_PURPLE_ACCENT_200
        # )
        border=border.only(top=border.BorderSide(width=10,color=colors.TEAL_100),left=border.BorderSide(width=3,color=colors.AMBER)),
        margin=margin.only(top=20,left=20),
        tooltip='this is container it shows you hello this in their center'

    )

    page.add(c)


flet.app(target=main, view=flet.FLET_APP)