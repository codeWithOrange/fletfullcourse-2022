import flet 
from flet import Page, Text, Container, Row,colors,border

def main(page:Page):
    page.title='row control tutorial'
    page.padding=0
    page.vertical_alignment='center'
    rowContainer=Container(
        content=Row(
        controls=[
            Container(
                content=Text(value='first child'),
                width=100,
                height=80,
                bgcolor=colors.RED_800

            ),
            Container(
                content=Text(value='second child'),
                width=100,
                height=50,
                bgcolor=colors.RED_800

            ),
            # Container(
            #     content=Text(value='third child'),
            #     width=100,
            #     height=100,
            #     bgcolor=colors.RED_800

            # ),
            # Container(
            #     content=Text(value='fourth child'),
            #     width=100,
            #     height=100,
            #     bgcolor=colors.RED_800

            # ),

        ],
        # wrap=True,
        # scroll='always',
        spacing=3,
        run_spacing=3,
        # alignment='spaceAround',
        width=500,
        height=500,
        vertical_alignment='center',
       


        
    ),
    border=border.all(width=3)
    
    )
    page.add(rowContainer)


flet.app(target=main)