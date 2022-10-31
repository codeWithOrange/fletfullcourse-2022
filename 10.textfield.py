
from email.policy import default
import flet 
from flet import TextField, Page, colors , border_radius, padding, icons,Text


def main(page:Page):
    page.title='textfield tutorial'
    page.bgcolor='grey'
    def on_change(e):
        t1.value=t.value
        page.update()

    def on_submit(e):
        t1.value=t.value;
        page.update()

    def on_focus(e):
        t1.value=t.value;
        t.border_color=colors.YELLOW_600
        t.border_width=10
        page.update(
             
        )

    def on_blur(e):
        t.border_width=2
        t.border_color='black'
        page.update()


    t1=Text()
    t=TextField(
        # width=100,
        # height=100, 
        # disabled=True,
        # read_only=True, 
        # value='this is my name'
        # text_size=50,
        border_radius=border_radius.horizontal(left=10, right=4),
        cursor_color=colors.LIGHT_GREEN_ACCENT_400,
    
        # border_width=10,
        # border_color='red'
        # focused_border_color='red', 
        # focused_border_width=10,
        content_padding=padding.only(top=20,left=10,),
        # max_length=10,
        # label='enter your name'
        hint_text='enter your name', 
        filled=True,
        bgcolor=colors.PURPLE_100,
        color=colors.BLACK87,
        helper_text='Enter your email', 
        icon=icons.PERSON_ADD,

        # prefix_icon='ten_k',
        # suffix_icon=icons.MOBILE_FRIENDLY,
        # prefix=Text(value='+91'),
        # suffix=Text(value='hello'),
        # prefix_text='+91',
        # suffix_text='hello',
        multiline=True,
        # min_lines=2, 
        # max_lines=5,
        # password=True,
        # can_reveal_password=True,
        shift_enter=True,
        # keyboard_type='email',
        selection_color=colors.RED_400,
        # text_align='end',
        # border='underline' , 
        # on_change=on_change,
        # on_submit=on_submit,
        # autofocus=True,
        on_focus=on_focus,
        # value='this is the default value',
        on_blur= on_blur,
        capitalization='sentences',
    
    
    )
    page.add(t,t1)

flet.app(target=main ,view=flet.FLET_APP)
