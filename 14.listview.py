<<<<<<< HEAD
import flet 
from flet import Page, ListView , Container, Text,colors, padding
from flet.ref import Ref

def main(page:Page):
    page.title='listview tutorial'
    page.bgcolor=colors.BLUE_GREY
    page.padding=0
    
    # listview=ListView(
    #     controls=[
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Container(
                
    #             content=Text(
    #                 value='this is the container',
    #             ),
    #             bgcolor=colors.RED,
    #         )

    #     ], 
    #     expand=True, 
    #     auto_scroll=True,
    #     # width=100,
    #     # height=100,
    #     # first_item_prototype=True,
    #     spacing=30,
    #     padding=padding.only(left=30), 
        

    # )
    listview=Ref[ListView]()
    page.add(
        ListView(
            ref=listview, 
            expand=True,
            divider_thickness=30,
            
        )
    )
    dict={
        'user1':{
            'id':1, 
            'firstname':'varun', 
            'lastname':'aryan', 
            'email':'varun@gmail.com',
            'age':33,

        }, 
        'user2':{
            'id':2, 
            'firstname':'rajraushan', 
            'lastname':'kumar', 
            'email':'rajraushan@gmail.com',
            'age':32,

        }, 
        'user3':{
            'id':3, 
            'firstname':'chandan', 
            'lastname':'kumar', 
            'email':'chandan@gmail.com',
            'age':36,

        }, 
        
    }

    # for i in range(1,31):
    #     listview.current.controls.append(
    #         Text(value=str(i))

    #     )
    #     page.update()
    for k,v in dict.items():
        for k1,v1 in v.items():
            listview.current.controls.append(
                Text(value=f'{k1}:{v1}')
            )
            page.update()



flet.app(target=main, view=flet.FLET_APP)
=======
import flet 
from flet import Page, ListView , Container, Text,colors, padding
from flet.ref import Ref

def main(page:Page):
    page.title='listview tutorial'
    page.bgcolor=colors.BLUE_GREY
    page.padding=0
    
    # listview=ListView(
    #     controls=[
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Text(value='this is text control'),
    #         Container(
                
    #             content=Text(
    #                 value='this is the container',
    #             ),
    #             bgcolor=colors.RED,
    #         )

    #     ], 
    #     expand=True, 
    #     auto_scroll=True,
    #     # width=100,
    #     # height=100,
    #     # first_item_prototype=True,
    #     spacing=30,
    #     padding=padding.only(left=30), 
        

    # )
    listview=Ref[ListView]()
    page.add(
        ListView(
            ref=listview, 
            expand=True,
            divider_thickness=30,
            
        )
    )
    dict={
        'user1':{
            'id':1, 
            'firstname':'varun', 
            'lastname':'aryan', 
            'email':'varun@gmail.com',
            'age':33,

        }, 
        'user2':{
            'id':2, 
            'firstname':'rajraushan', 
            'lastname':'kumar', 
            'email':'rajraushan@gmail.com',
            'age':32,

        }, 
        'user3':{
            'id':3, 
            'firstname':'chandan', 
            'lastname':'kumar', 
            'email':'chandan@gmail.com',
            'age':36,

        }, 
        
    }

    # for i in range(1,31):
    #     listview.current.controls.append(
    #         Text(value=str(i))

    #     )
    #     page.update()
    for k,v in dict.items():
        for k1,v1 in v.items():
            listview.current.controls.append(
                Text(value=f'{k1}:{v1}')
            )
            page.update()



flet.app(target=main, view=flet.FLET_APP)
>>>>>>> a75473c4fba2b6a32ca9be704bb0091a07c7bd50
