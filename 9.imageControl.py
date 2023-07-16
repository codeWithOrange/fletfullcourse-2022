import flet 
from flet import Image, Page, Container, border, colors,border_radius

def main(page:Page):
    page.title='image control tutorial'
    page.bgcolor='bluegrey'
    page.scroll='always'

    c=Container(
        content=Image(
        src='images/redrose.jpg',
        opacity=1,
        tooltip='this is the image', 
        visible=True,
        # width=500,
        # height=500,
        fit='cover',
        border_radius=border_radius.only(topLeft=10,bottomRight=10)

        ), 
        # border=border.all(width=5,color=colors.RED_800
        
        # )
    )

    page.add(c)



    


flet.app(target=main,assets_dir='assets', view=flet.FLET_APP)
