import flet 
from flet import Column, Text, Container, colors ,Page,alignment,border
def main(page:Page):
    page.title='column tutorial'
    page.padding=0
    page.horizontal_alignment='center'
    page.bgcolor=colors.LIGHT_GREEN_900

    c1=Container(
        content=Column(
        controls=[
            Container(
                content=Text(value='first child'),
                bgcolor=colors.BROWN_700,
                width=100,
                height=100,
                alignment=alignment.center

            ),
            Container(
                content=Text(value='first child'),
                bgcolor=colors.BROWN_700,
                width=100,
                height=100,
                alignment=alignment.center

            ),
            Container(
                content=Text(value='first child'),
                bgcolor=colors.BROWN_700,
                width=100,
                height=100,
                alignment=alignment.center ,
    

            ),
            Container(
                content=Text(value='first child'),
                bgcolor=colors.BROWN_700,
                width=100,
                height=100,
                alignment=alignment.center

            ),
            Container(
                content=Text(value='first child'),
                bgcolor=colors.BROWN_700,
                width=100,
                height=100,
                alignment=alignment.center

            ),
            Container(
                content=Text(value='first child'),
                bgcolor=colors.BROWN_700,
                width=100,
                height=100,
                alignment=alignment.center

            ),

        ]
        ,
        spacing=1,
        alignment='spaceEvenly',
        # expand=True,
        # horizontal_alignment='center',
        width=600,
        height=400,
        # wrap=True,
        scroll=True,
        auto_scroll=True,
        run_spacing=3,
     
    ),
    border=border.all(width=5),
    # expand=True,

    )


    page.add(c1)

flet.app(target=main,view=flet.FLET_APP)