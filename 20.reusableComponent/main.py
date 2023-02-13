import flet 
from flet import Page, AppBar, Text,UserControl,colors
from customText import CustomText

def main(page:Page):
    page.title='userControl tutorial'
    page.theme_mode='light'

    page.add(
       CustomText(
            value='hello',
            
       ),
       CustomText(
            value='rajraushan',
            
       ),
       CustomText(
            value='bye',
            
       ),
       
        
    )


flet.app(target=main, view=flet.FLET_APP)
