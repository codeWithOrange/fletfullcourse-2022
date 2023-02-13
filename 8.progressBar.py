import flet 
from flet import ProgressBar, Page, colors 
import time

def main(page:Page):
    page.title='progress bar tutorial'
    page.horizontal_alignment='center'
    page.vertical_alignment='center'
    page.bgcolor=colors.BLUE_GREY
    

    p=ProgressBar(
        color=colors.PURPLE_900, 
        bgcolor=colors.YELLOW_100,
        width=200,
        # height=40,
        height=5
        # value=0.8,
    )
    page.add(p)

    for i in range(100):
        p.value=i*0.01
        page.update()
        time.sleep(0.1)





flet.app(target=main, view=flet.FLET_APP)
