import flet 
from flet import Page,Text,TextField,ElevatedButton, Column, colors,icons,padding, alignment,Container,Row,Icon
from flet.ref import Ref
import sqlite3

def main(page:Page):
    page.title='sqlite3 project-01'
    page.bgcolor=colors.GREEN_ACCENT
    page.scroll='auto'

    username=Ref[TextField]()
    email=Ref[TextField]()
    password=Ref[TextField]()

    connection=sqlite3.connect('users.db',check_same_thread=False)
    cursor=connection.cursor()

    
    

    def submit(e):
        query='''
            INSERT INTO USERS(username, email, password) values(?,?,?)
        '''
        values=[
            (f'{username.current.value}', f'{email.current.value}', f'{password.current.value}')

        ]

        cursor.executemany(query, values)
        query1='''
            select * from users
        '''
        cursor.execute(query1)
        data=cursor.fetchall()
        users_data.current.controls.append(
            Text(
                value=data[len(data)-1]
            )
        )




        connection.commit()

        username.current.value=''
        email.current.value=''
        password.current.value=''
        page.update()

    
    users_data=Ref[Column]()


    c=Container(
        alignment=alignment.center,
        content=Column(
            horizontal_alignment='center',
            width=500,
            controls=[
                Container(
                    content=Text(
                    value='Sqlite3 project-01', 
                    size=20, 
                    color=colors.WHITE,
                    
                ), 
                padding=padding.only(bottom=10)
                ),
                
                TextField(
                    ref=username, 
                    prefix_icon=icons.PERSON,
                    hint_text='username', 
                ), 
                TextField(
                    ref=email, 
                    prefix_icon=icons.EMAIL,
                    hint_text='email', 
                ), 
                TextField(
                    ref=password, 
                    prefix_icon=icons.PASSWORD_ROUNDED,
                    hint_text='password',
                    password=True, 
                    can_reveal_password=True, 

                ), 
                ElevatedButton(
                    content=
                        Row(
                            alignment='center',
                            controls=[
                               Icon(
                                name=icons.PERSON_ADD,
                               ) , 
                                Text(
                                value='Submit',
                            ), 

                        ]
                        ),
                     
                    
                    bgcolor=colors.PINK_ACCENT,
                    elevation=0,
                    on_click=submit, 
                   

                    

                ), 
                Column(
                    ref=users_data,
                )



            ]
        )

    )
    page.add(c)
    query2='''
        select * from users
    '''
    cursor.execute(query2)
    data1=cursor.fetchall()
    for d in data1:
        users_data.current.controls.append(
            Text(
                value=d
            )
        )
        page.update()




flet.app(target=main, view=flet.FLET_APP)

