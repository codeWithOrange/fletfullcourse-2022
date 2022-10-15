import flet 
from flet import Icon,icons,Page,Column,colors

def main(page:Page):
    page.title='flet icons tutorial'
    page.horizontal_alignment='center'
    page.vertical_alignment='center'
    page.bgcolor=colors.BLACK87

    c=Column(
        controls=[
            Icon(name=icons.ACCOUNT_BOX,size=40,color=colors.ORANGE_800,opacity=0.9,tooltip='this is add a photo icon',visible=True)

        ]
    )

    page.add(c)


flet.app(target=main,view=flet.FLET_APP)
