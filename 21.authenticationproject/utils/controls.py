from utils.imports import *

class CustomText(UserControl):
    def __init__(
        self,
        text:str,
        size:float=None,
        color:str=None,
        ref:Ref=None,

    ):
        super().__init__()
        self.ref=ref
        self.text=text
        self.size=size
        self.color=color

    def build(self):
        return Text(
            ref=self.ref,
            value=self.text,
            color=self.color,
            size=self.size
        )

class CustomCard(UserControl):
    def __init__(
        self,
        content:Control,
        width:float=None,
        height:float=None,
        bgcolor:str=None,
    ):
        super().__init__()
        self.content=content
        self.width=width
        self.height=height
        self.bgcolor=bgcolor


    def build(self):
        return Card(
            content=Container(
                padding=20,
                alignment=alignment.center,
                content=self.content,
                border_radius=10,
                bgcolor=self.bgcolor,
            ),
            width=self.width,
            height=self.height,
            
        )

class CustomTextField(UserControl):
    def __init__(
        self,
        ref:Ref=None,
        hint_text:str=None,
        prefix_icon:str=None,
        suffix_icon:str=None,
        isPassword:bool=False,

    ):
        super().__init__()
        self.ref=ref
        self.hint_text=hint_text
        self.prefix_icon=prefix_icon
        self.suffix_icon=suffix_icon
        self.isPassword=isPassword

    def build(self):
        return TextField(
            ref=self.ref,
            hint_text=self.hint_text,
            suffix_icon=self.suffix_icon,
            prefix_icon=self.prefix_icon,
            password=True if self.isPassword else False,
            can_reveal_password=True,

        )

class CustomElevatedButton(UserControl):
    def __init__(
        self,
        text:str,
        bgcolor:str=None,
        color:str=None,
        onTap=None,
        ref:Ref=None

    ):
        super().__init__()
        self.text=text
        self.bgcolor=bgcolor
        self.color=color
        self.onTap=onTap
        self.ref=ref

    def build(self):
        return ElevatedButton(
            content=Container(
                alignment=alignment.center,
                content=CustomText(
                    text=self.text,
                    color=self.color,
                ),
            
            ),
            ref=self.ref,
            on_click=self.onTap,
            bgcolor=self.bgcolor,
        

        )
