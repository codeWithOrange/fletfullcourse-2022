<<<<<<< HEAD
import flet 
from flet import (
    Page, 
    Container, 
    Column, 
    colors, 
    icons,
    ElevatedButton,
    Row,
    Icon,
    Text,
    ButtonStyle,
    buttons,
    FilledButton,
    FilledTonalButton,
    OutlinedButton,
    TextButton,
    IconButton
)

def main(page:Page):
    page.title='all buttons tutorial'
    page.bgcolor=colors.GREEN_ACCENT_200
    page.horizontal_alignment='center'
    page.scroll='auto'
    

    def hover(e):
        print('hover')
    def click(e):
        print('clicked')
    def long_press(e):
        print('long press')


    selected=False
    def selection(e):
        f1.selected=not f1.selected
        page.update()

      



    f=FilledTonalButton(
                text='filled tonal button',
                icon=icons.PERSON,
                style=ButtonStyle(

                    color={
                        '':colors.BLACK12,
                        'hovered':colors.RED_600,
                    },
                    bgcolor=colors.INDIGO_ACCENT_400,
                )
                
            )

    f1=IconButton(
                icon=icons.ACCOUNT_CIRCLE_ROUNDED,
                icon_color=colors.AMBER_700,
                selected_icon=icons.PERCENT_OUTLINED,
                selected_icon_color=colors.PINK_600,
                icon_size=50,
               
                on_click=selection,

            )


    c=Column(
        controls=[
            #! elevated button
            ElevatedButton(
                # text='Elevated button',
                # color=colors.BLACK, 
                # bgcolor=colors.BLUE_500, 
                tooltip='this is the button',
                elevation=10, 
                disabled=True,
                # icon=icons.PERSON,
                # icon_color=colors.DEEP_ORANGE_500,
                # opacity=0.5,
                # autofocus=True,

                on_click=click, 
                on_long_press=long_press,
                on_hover=hover,
                content=Row(
                    controls=[
                        Icon(
                            name=icons.PEDAL_BIKE,
                            color=colors.PINK_100,
                        ),
                        Text(
                            value='Elevated button', 

                        )
                        , 
                        Icon(
                            name=icons.FLUTTER_DASH,
                        ), 
                        
                    ], 
                    alignment='spaceAround',
                


                ), 
              
                # style=ButtonStyle(
                #     shape=buttons.RoundedRectangleBorder(radius=10),
                # )
                # style=ButtonStyle(
                #     shape=buttons.BeveledRectangleBorder(radius=10),
                # )
            
                # style=ButtonStyle(
                #     shape=buttons.CircleBorder(),
                   
                # )
                style=ButtonStyle(
                    shape=buttons.CountinuosRectangleBorder(radius=10),
                    # color={
                    #     'disabled':colors.RED_400,
                    # }
                   
                )







            ), 
            #! Filled button
            FilledButton(
                text='Filled button',
                icon=icons.PERCENT,
            ),
            OutlinedButton(
                text='Outlined Button',
                icon=icons.FLUTTER_DASH,

            ),
            
            #! Text Button
            TextButton(
                text='Text Button',
            ),
            f,
            f,
            f1,
            

        ]
    )
    page.add(c)


flet.app(target=main, view=flet.FLET_APP)

=======
import flet 
from flet import (
    Page, 
    Container, 
    Column, 
    colors, 
    icons,
    ElevatedButton,
    Row,
    Icon,
    Text,
    ButtonStyle,
    buttons,
    FilledButton,
    FilledTonalButton,
    OutlinedButton,
    TextButton,
    IconButton
)

def main(page:Page):
    page.title='all buttons tutorial'
    page.bgcolor=colors.GREEN_ACCENT_200
    page.horizontal_alignment='center'
    page.scroll='auto'
    

    def hover(e):
        print('hover')
    def click(e):
        print('clicked')
    def long_press(e):
        print('long press')


    selected=False
    def selection(e):
        f1.selected=not f1.selected
        page.update()

      



    f=FilledTonalButton(
                text='filled tonal button',
                icon=icons.PERSON,
                style=ButtonStyle(

                    color={
                        '':colors.BLACK12,
                        'hovered':colors.RED_600,
                    },
                    bgcolor=colors.INDIGO_ACCENT_400,
                )
                
            )

    f1=IconButton(
                icon=icons.ACCOUNT_CIRCLE_ROUNDED,
                icon_color=colors.AMBER_700,
                selected_icon=icons.PERCENT_OUTLINED,
                selected_icon_color=colors.PINK_600,
                icon_size=50,
               
                on_click=selection,

            )


    c=Column(
        controls=[
            #! elevated button
            ElevatedButton(
                # text='Elevated button',
                # color=colors.BLACK, 
                # bgcolor=colors.BLUE_500, 
                tooltip='this is the button',
                elevation=10, 
                disabled=True,
                # icon=icons.PERSON,
                # icon_color=colors.DEEP_ORANGE_500,
                # opacity=0.5,
                # autofocus=True,

                on_click=click, 
                on_long_press=long_press,
                on_hover=hover,
                content=Row(
                    controls=[
                        Icon(
                            name=icons.PEDAL_BIKE,
                            color=colors.PINK_100,
                        ),
                        Text(
                            value='Elevated button', 

                        )
                        , 
                        Icon(
                            name=icons.FLUTTER_DASH,
                        ), 
                        
                    ], 
                    alignment='spaceAround',
                


                ), 
              
                # style=ButtonStyle(
                #     shape=buttons.RoundedRectangleBorder(radius=10),
                # )
                # style=ButtonStyle(
                #     shape=buttons.BeveledRectangleBorder(radius=10),
                # )
            
                # style=ButtonStyle(
                #     shape=buttons.CircleBorder(),
                   
                # )
                style=ButtonStyle(
                    shape=buttons.CountinuosRectangleBorder(radius=10),
                    # color={
                    #     'disabled':colors.RED_400,
                    # }
                   
                )







            ), 
            #! Filled button
            FilledButton(
                text='Filled button',
                icon=icons.PERCENT,
            ),
            OutlinedButton(
                text='Outlined Button',
                icon=icons.FLUTTER_DASH,

            ),
            
            #! Text Button
            TextButton(
                text='Text Button',
            ),
            f,
            f,
            f1,
            

        ]
    )
    page.add(c)


flet.app(target=main, view=flet.FLET_APP)

>>>>>>> a75473c4fba2b6a32ca9be704bb0091a07c7bd50
