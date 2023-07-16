<<<<<<< HEAD
import flet 
from flet import Page, Card, colors, Icon,icons, Container, padding,Text,alignment

def main(page:Page):
    page.title='card tutorial'
    page.theme_mode='light'

    card=Card(
        content=Container(
            padding=10,
            content=Text(
                value='this is the world'
                ,
            ),
            bgcolor=colors.WHITE30,
            alignment=alignment.center,
        ),
        elevation=10,
        width=200,
        height=200,
        margin=30,
        
    )
    
    page.add(card)

flet.app(target=main,view=flet.FLET_APP)
=======
import flet 
from flet import Page, Card, colors, Icon,icons, Container, padding,Text,alignment

def main(page:Page):
    page.title='card tutorial'
    page.theme_mode='light'

    card=Card(
        content=Container(
            padding=10,
            content=Text(
                value='this is the world'
                ,
            ),
            bgcolor=colors.WHITE30,
            alignment=alignment.center,
        ),
        elevation=10,
        width=200,
        height=200,
        margin=30,
        
    )
    
    page.add(card)

flet.app(target=main,view=flet.FLET_APP)
>>>>>>> a75473c4fba2b6a32ca9be704bb0091a07c7bd50
