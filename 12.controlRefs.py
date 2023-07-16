import flet 
from flet.ref import Ref
from flet import (
    Page,
    Text,
    colors,
    icons,
    TextField,
    ElevatedButton
)

def main(page:Page):
    page.title='control ref tutorial'
    page.bgcolor=colors.BLUE_ACCENT

    def changeText(e):
        firstname.current.value='hello universe'
        page.update()

    def getText(e):
        print(textfield1.current.value)

    firstname=Ref[Text]()
    textfield1=Ref[TextField]()

    page.add(
        Text(ref=firstname, value='hello world '),
        TextField(ref=textfield1),
        ElevatedButton(text='submit',on_click=getText)
    )

flet.app(target =main, view=flet.FLET_APP)
