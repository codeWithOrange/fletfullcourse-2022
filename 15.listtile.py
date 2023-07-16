import flet 
from flet import Page,ListTile,Icon,icons,colors,Text,ListView
from flet.ref import Ref
def main(page:Page):
    page.title='listtile tutorial'
    page.bgcolor=colors.WHITE
    
    def on_click(e):
        ListTile.selected= not ListTile.selected
        page.update()

    def on_long_press(e):
        print('on long press clicked')

    list=[
        {
            'id':1, 
            'username':'angad123', 'email':'angad@gmail.com', 
            'password':333,
        }, 
        {
            'id':2, 
            'username':'chandan123', 'email':'chandan@gmail.com', 
            'password':333,
        }, 
        {
            'id':3, 
            'username':'rajraushan123', 'email':'rajraushan@gmail.com', 
            'password':333,
        }, 
        {
            'id':4, 
            'username':'kriti', 'email':'kriti@gmail.com', 
            'password':333,
        }, 
        {
            'id':4, 
            'username':'kriti', 'email':'kriti@gmail.com', 
            'password':333,
        }, 
        {
            'id':4, 
            'username':'kriti', 'email':'kriti@gmail.com', 
            'password':333,
        }, 
        {
            'id':4, 
            'username':'kriti', 'email':'kriti@gmail.com', 
            'password':333,
        }, 
        {
            'id':4, 
            'username':'kriti', 'email':'kriti@gmail.com', 
            'password':333,
        }, 
        {
            'id':4, 
            'username':'kriti', 'email':'kriti@gmail.com', 
            'password':333,
        }, 
        {
            'id':4, 
            'username':'kriti', 'email':'kriti@gmail.com', 
            'password':333,
        }, 
        {
            'id':4, 
            'username':'kriti', 'email':'kriti@gmail.com', 
            'password':333,
        }, 
        {
            'id':4, 
            'username':'kriti', 'email':'kriti@gmail.com', 
            'password':333,
        }, 
        {
            'id':4, 
            'username':'kriti', 'email':'kriti@gmail.com', 
            'password':333,
        }, 
        {
            'id':4, 
            'username':'kriti', 'email':'kriti@gmail.com', 
            'password':333,
        }, 
        {
            'id':4, 
            'username':'kriti', 'email':'kriti@gmail.com', 
            'password':333,
        }, 
        {
            'id':4, 
            'username':'kriti', 'email':'kriti@gmail.com', 
            'password':333,
        }, 
        {
            'id':4, 
            'username':'kriti', 'email':'kriti@gmail.com', 
            'password':333,
        }, 
        {
            'id':4, 
            'username':'kriti', 'email':'kriti@gmail.com', 
            'password':333,
        }, 
        {
            'id':4, 
            'username':'kriti', 'email':'kriti@gmail.com', 
            'password':333,
        }, 
        {
            'id':4, 
            'username':'kriti', 'email':'kriti@gmail.com', 
            'password':333,
        }, 
        {
            'id':4, 
            'username':'kriti', 'email':'kriti@gmail.com', 
            'password':333,
        }, 
        {
            'id':4, 
            'username':'kriti', 'email':'kriti@gmail.com', 
            'password':333,
        }, 
        {
            'id':4, 
            'username':'kriti', 'email':'kriti@gmail.com', 
            'password':333,
        }, 
        {
            'id':4, 
            'username':'kriti', 'email':'kriti@gmail.com', 
            'password':333,
        }, 
        {
            'id':4, 
            'username':'kriti', 'email':'kriti@gmail.com', 
            'password':333,
        }, 
        {
            'id':4, 
            'username':'kriti', 'email':'kriti@gmail.com', 
            'password':333,
        }, 

    ]

    # listtile=ListTile(
    #     title=Text(value="this is the title"), 
    #     subtitle=Text(value='subtitle')
    #     , 
    #     leading=Icon(
    #         name=icons.PERSON,
    #     ),
    #     trailing=Icon(
    #         name=icons.ACCESSIBLE_FORWARD
    #     ), 
    #     content_padding=10,
       
    #     # dense=True,
    #     is_three_line=True,
    #     on_click=on_click, 
    #     on_long_press=on_long_press

    


    # )

    listview=Ref[ListView]()
    
    page.add(
        ListView(
            ref=listview, 
            expand=True, 
        )
    )

    for data in list:
        listview.current.controls.append(
            ListTile(
                title=Text(
                    value=data['username']
                )
                , 
                subtitle=Text(
                    value=data['email']

                ), 
                leading=Icon(
                    name=icons.PERSON, 
                ), 
                trailing=Icon(
                    name=icons.ADD_BUSINESS
                )


            )
        )
        page.update()


    

    
   


flet.app(target=main,view=flet.FLET_APP)
