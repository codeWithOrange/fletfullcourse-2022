<<<<<<< HEAD
import flet 
from flet import View,Text,page,colors,Icon,icons,AppBar,Page,ElevatedButton,FloatingActionButton,Control,Column
from flet.ref import Ref

def main(page:Page):
    page.theme_mode='light'
    page.title='navigation and routing in flet framework tutorial'
    columnRef=Ref[Column]()
    def returnMultipleText():
        for i in range(100):
            columnRef.current.controls.append(
                Text(
                    f'{i}'
                )
            )
            page.update()

    
    def change_route(route):
        if page.route=='/':
            page.views.clear()
            page.views.append(
                View(
                    route='/',
                    controls=[
                        ElevatedButton(
                            text='about page',
                            on_click=lambda e:e.page.go('/about')
                        ),
                        ElevatedButton(
                            text='about page',
                            on_click=lambda e:e.page.go('/about')
                        ),
                        Column(
                            ref=columnRef,
                        )
                
                        
                    ],
                    spacing=2,
                    bgcolor=colors.PINK_900,
                    appbar=AppBar(
                        title=Text('home page')
                    ),
                    floating_action_button=FloatingActionButton(
                        content=Icon(
                            name=icons.ADD_A_PHOTO
                        )
                    ),
                    # vertical_alignment='center',
                    # horizontal_alignment='center',
                    padding=0,
                    scroll=True,

                )
            )
        elif page.route=='/about':
            page.views.append(
                View(
                    route='/about',
                    appbar=AppBar(
                        title=Text(
                            'about page'
                        )
                    ),
                    controls=[
                        ElevatedButton(
                            text='Contact page',
                            on_click=lambda e:e.page.go('/contact'),
                        )
                    ]
                )
            )
        elif page.route=='/contact':
            page.views.append(
                View(
                    '/contact',
                    appbar=AppBar(
                        title=Text('contact page'),
                    ),
                    controls=[
                        Text('contact page'),
                        ElevatedButton(
                            text='home page',
                            on_click=lambda e:e.page.go('/')
                        )
                    ]
                )
            )
        else:
            page.views.append(
                View(
                    controls=[
                        Text(
                            'no page found'
                        )
                    ]
                )
            )
        page.update()

    def pop_view(route):
        page.views.pop()
        top_page=page.views[-1]
        page.go(top_page.route);
        

        
        
    
    
    page.update()
    page.on_route_change=change_route
    page.on_view_pop=pop_view
    page.go(page.route);
    returnMultipleText()


=======
import flet 
from flet import View,Text,page,colors,Icon,icons,AppBar,Page,ElevatedButton,FloatingActionButton,Control,Column
from flet.ref import Ref

def main(page:Page):
    page.theme_mode='light'
    page.title='navigation and routing in flet framework tutorial'
    columnRef=Ref[Column]()
    def returnMultipleText():
        for i in range(100):
            columnRef.current.controls.append(
                Text(
                    f'{i}'
                )
            )
            page.update()

    
    def change_route(route):
        if page.route=='/':
            page.views.clear()
            page.views.append(
                View(
                    route='/',
                    controls=[
                        ElevatedButton(
                            text='about page',
                            on_click=lambda e:e.page.go('/about')
                        ),
                        ElevatedButton(
                            text='about page',
                            on_click=lambda e:e.page.go('/about')
                        ),
                        Column(
                            ref=columnRef,
                        )
                
                        
                    ],
                    spacing=2,
                    bgcolor=colors.PINK_900,
                    appbar=AppBar(
                        title=Text('home page')
                    ),
                    floating_action_button=FloatingActionButton(
                        content=Icon(
                            name=icons.ADD_A_PHOTO
                        )
                    ),
                    # vertical_alignment='center',
                    # horizontal_alignment='center',
                    padding=0,
                    scroll=True,

                )
            )
        elif page.route=='/about':
            page.views.append(
                View(
                    route='/about',
                    appbar=AppBar(
                        title=Text(
                            'about page'
                        )
                    ),
                    controls=[
                        ElevatedButton(
                            text='Contact page',
                            on_click=lambda e:e.page.go('/contact'),
                        )
                    ]
                )
            )
        elif page.route=='/contact':
            page.views.append(
                View(
                    '/contact',
                    appbar=AppBar(
                        title=Text('contact page'),
                    ),
                    controls=[
                        Text('contact page'),
                        ElevatedButton(
                            text='home page',
                            on_click=lambda e:e.page.go('/')
                        )
                    ]
                )
            )
        else:
            page.views.append(
                View(
                    controls=[
                        Text(
                            'no page found'
                        )
                    ]
                )
            )
        page.update()

    def pop_view(route):
        page.views.pop()
        top_page=page.views[-1]
        page.go(top_page.route);
        

        
        
    
    
    page.update()
    page.on_route_change=change_route
    page.on_view_pop=pop_view
    page.go(page.route);
    returnMultipleText()


>>>>>>> a75473c4fba2b6a32ca9be704bb0091a07c7bd50
flet.app(target=main, view=flet.FLET_APP)