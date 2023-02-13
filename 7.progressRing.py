import flet 
from flet import ProgressRing, colors, Page

def main(page:Page):
    page.title='progressRing tutorial '
    page.horizontal_alignment='center'
    page.vertical_alignment='center'

    p=ProgressRing(
        color=colors.PINK_300,  
        bgcolor=colors.GREEN_800,
        value=0.2, 
        tooltip='this is the progress ring', 
        visible=True,

    )
    page.add(p)

flet.app(target=main, view=flet.FLET_APP)
