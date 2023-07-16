from flet import UserControl, colors, Text, Column,icons,Icon,Container


class HomePage(UserControl):
    def build(self):
        return Column(
            controls=[
                Text('home page')
            ]
        )
class AboutPage(UserControl):
    def build(self):
        return Column(
            controls=[
                Text('About page'),
                Icon(name=icons.PERSON, color=colors.GREEN, size=30)
            ]
        )
class ContactPage(UserControl):
    def build(self):
        return Column(
            controls=[
                Text('Contact page')
            ]
        )
class ProfilePage(UserControl):
    def build(self):
        return Column(
            controls=[
                Text('profile page')
            ]
        )
    
class PageNotFound(UserControl):
    def __init__(self, title:str):
        super().__init__()
        self.title=title

    def build(self):
        return Container(
            content=Text(self.title)
        )

