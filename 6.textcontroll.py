import flet 
from flet import Text, Page, Column, colors

def main(page:Page):
    page.title='text control tutorial'
    page.bgcolor=colors.ORANGE_300
    page.scroll='adaptive'

    c=Column(
        controls=[
            Text(value='hello world lajsdlfkajs dfal sdflas dfasd fasdf', 
            size=40, color=colors.BLUE,
            # bgcolor=colors.GREEN_ACCENT_700,
            # selectable=True,
            weight='w400',
            # italic=True, 
            # max_lines=1, 
            # overflow='ellipsis', 
            text_align='end', 
            font_family='fira code',
            ), 
        Text("Display Large", style="displayLarge"),
        Text("Display Medium", style="displayMedium"),
        Text("Display Small", style="displaySmall"),
        Text("Headline Large", style="headlineLarge"),
        Text("Headline Medium", style="headlineMedium"),
        Text("Headline Small", style="headlineMedium"),
        Text("Title Large", style="titleLarge"),
        Text("Title Medium", style="titleMedium"),
        Text("Title Small", style="titleSmall"),
        Text("Label Large", style="labelLarge"),
        Text("Label Medium", style="labelMedium"),
        Text("Label Small", style="labelSmall"),
        Text("Body Large", style="bodyLarge"),
        Text("Body Medium", style="bodyMedium"),
        Text("Body Small", style="bodySmall"),

        ]
    )

    page.add(c)

flet.app(target=main, view=flet.FLET_APP)
