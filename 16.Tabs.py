<<<<<<< HEAD
import flet 
from flet import Page, Text, icons, Icon, Tabs,Container,Tab

def main(page:Page):
    page.title='tabs tutorial'
    page.bgcolor='bluegrey'

    def tab_change(e:flet.Event):
        print('tab change')
        print(e.data)
        

    tab=Tabs(
        selected_index=1,
        animation_duration=100,
        on_change=tab_change,
        tabs=[
            Tab(
                text='tab1',
                content=Text(
                    value='this is the tab1',
                    color='black'
                )
            ),
            Tab(
                # text='tab2',
                tab_content=Icon(
                    name=icons.PERSON,
                ),
                content=Text(
                    value='this is the tab 2'
                )
            ),
            Tab(
                text='Tab3',
                icon=icons.FAVORITE,
                content=Text(
                    value='this is the tab3'
                )
            ),

        ]
    )
    page.add(tab)




flet.app(target=main, view=flet.FLET_APP)
=======
import flet 
from flet import Page, Text, icons, Icon, Tabs,Container,Tab

def main(page:Page):
    page.title='tabs tutorial'
    page.bgcolor='bluegrey'

    def tab_change(e:flet.Event):
        print('tab change')
        print(e.data)
        

    tab=Tabs(
        selected_index=1,
        animation_duration=100,
        on_change=tab_change,
        tabs=[
            Tab(
                text='tab1',
                content=Text(
                    value='this is the tab1',
                    color='black'
                )
            ),
            Tab(
                # text='tab2',
                tab_content=Icon(
                    name=icons.PERSON,
                ),
                content=Text(
                    value='this is the tab 2'
                )
            ),
            Tab(
                text='Tab3',
                icon=icons.FAVORITE,
                content=Text(
                    value='this is the tab3'
                )
            ),

        ]
    )
    page.add(tab)




flet.app(target=main, view=flet.FLET_APP)
>>>>>>> a75473c4fba2b6a32ca9be704bb0091a07c7bd50
