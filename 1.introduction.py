import flet 
from flet import Text,Page,colors,padding

def main(page:Page):
    page.title='introduction app'
    page.bgcolor=colors.AMBER
    # page.padding=padding.only(left=40,top=40)
    page.horizontal_alignment='center'
    page.vertical_alignment='center'
    page.scroll='hidden'
    print(page.session_id)
    print(page.platform)
    for i in range(100):
        t=Text(value='hello world')
        page.add(t)

    

flet.app(target=main,view=flet.FLET_APP );





