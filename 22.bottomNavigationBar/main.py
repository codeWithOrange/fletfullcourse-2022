import flet 
from flet import Page,NavigationBar,NavigationDestination,icons,Text,Icon,colors,NavigationBarLabelBehavior
from pages import (
    HomePage, 
    AboutPage, 
    ContactPage, 
    ProfilePage,
    PageNotFound
)
def main(page:Page):
    page.title='bottom navigation bar tutorial'
    page.padding=0
    page.theme_mode='light'
    page.navigation_bar=NavigationBar(
        bgcolor=colors.YELLOW, 
        # elevation=30,
        label_behavior=NavigationBarLabelBehavior.ONLY_SHOW_SELECTED,
        destinations=[
            NavigationDestination(
                icon=icons.HOME_OUTLINED,
                label='Home',
                # icon_content=Icon(name=icons.HOME, color=colors.GREEN),
                selected_icon=icons.HOME_FILLED,
                # selected_icon_content=Icon(name=icons.HOME_FILLED, color=colors.BLUE)
            ),
            NavigationDestination(
                icon=icons.PERSON_OUTLINE,
                label='About',
                # icon_content=Icon(name=icons.HOME, color=colors.GREEN),
                selected_icon=icons.PERSON
            ),
            NavigationDestination(
                icon=icons.CONTACT_EMERGENCY_OUTLINED,
                label='Contact',
                # icon_content=Icon(name=icons.HOME, color=colors.GREEN),
                selected_icon=icons.CONTACT_EMERGENCY_SHARP
            ),
            NavigationDestination(
                icon=icons.PERSON_OUTLINE,
                label='Profile',
                # icon_content=Icon(name=icons.HOME, color=colors.GREEN),
                selected_icon=icons.PERSON_SHARP
            ),

        ],
        # selected_index=1
        on_change=lambda e:set_page(e)
    )

    def set_page(e):
        page.clean()
        page_index=e.control.selected_index
        page_label=e.control.destinations[page_index].label
        if page_label=='Home':
            page.bgcolor=colors.BLUE
            page.add(
                HomePage()
            )
        elif page_label=='About':
            page.bgcolor=colors.RED
            page.add(
                AboutPage()
            )
        elif page_label=='Contact':
            page.bgcolor=colors.YELLOW
            page.add(
                ContactPage()
            )
        elif page_label=='Profile':
            page.bgcolor=colors.PURPLE
            page.add(
                ProfilePage()
            )
        else:
            page.add(
                PageNotFound('page not found')
            )

    # page.bgcolor='blue'
    page.add(
        HomePage()
    )
   
 
   


    page.update()
   


if __name__=='__main__':
    flet.app(target=main, view=flet.FletApp)
