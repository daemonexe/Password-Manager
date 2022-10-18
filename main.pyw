# Required Modules
import random
import sqlite3
from tkinter import *
import os
from tkinter import ttk
from tkinter import filedialog
import shutil
from tkinter import messagebox
import string

# variables
window = Tk()
iid_val = 0
added_sno = []
invalid_counter = 0
total_clicks = 0
total_clicks1 = 0
total_clicks2 = 0
total_clicks3 = 0
button_clicks1 = 0
new_list = []

# Creating all pages in the app
sign_up_page = Frame(window)
login_page = Frame(window)
window.iconbitmap('icon.ico')

# Page switcher
def switch_page(frame):
    frame.tkraise()

# Arranging all frames
for frames in (login_page,sign_up_page):
    frames.grid(row=0, column=0, sticky='news')

# Importing the image files (PNG)
sign_up_img = PhotoImage(file = 'Sign_Up/sign_up.png')
sign_up_button_image = PhotoImage(file='Sign_Up/sign_up_button.png')
invalid_password_page = PhotoImage(file='Sign_Up/no_match_sign_in.png')
login_page_img = PhotoImage(file = 'Login/login.png')
login_button_img = PhotoImage(file = 'Login/login_button.png')
login_incorrect = PhotoImage(file = 'Login/login_incorrect_img.png')
less_characters_sign_up = PhotoImage(file = 'Sign_Up/less_characters_sign_up_img.png')
manager_baground = PhotoImage(file = 'Manager/manager.png')
exit_button_image = PhotoImage(file = 'Sign_Up/exit_button.png')
sing_up_button_hover = PhotoImage(file = 'Sign_Up/sign_up_button_on_hover.png')
eyes_closed_icon = PhotoImage(file='Login/eyes closed.png')
eyes_open_icon = PhotoImage(file='Login/eyes open .png')
search_icon_image = PhotoImage(file = 'Manager/search_icon.png')
refresh_icon_image = PhotoImage(file='Manager/refresh_icon.png')
import_icon_image = PhotoImage(file='Manager/import_image.png')
export_icon_image = PhotoImage(file='Manager/export_image.png')
update_button_image = PhotoImage(file = 'Manager/update_button_image.png')
delete_button_image = PhotoImage(file = 'Manager/delete_button_image.png')
reset_button_image = PhotoImage(file = 'Manager/reset_button_image.png')
logout_button_image =  PhotoImage(file = 'Manager/logout_button_image.png')
hover_image_add_button =  PhotoImage(file = 'Manager/add_database_hover_image .png')
hover_image_delete_button = PhotoImage(file = 'Manager/delete_button_hover_image.png')
hover_image_reset_button =PhotoImage(file = 'Manager/reset_button_hover_image.png')
hover_image_update_button = PhotoImage(file = 'Manager/update_button_hover_image.png')
hover_image_add_button_small = PhotoImage(file = 'Manager/add_database_image_hover_image.png')
hover_image_log_out = PhotoImage(file = 'Manager/logout_button_hover_image.png')
hover_image_clearfields = PhotoImage(file= 'Manager/clear_fields_image_hover.png')
hover_on_refresh_image =  PhotoImage(file= 'Manager/refresh_icon_hover_image.png')
hover_on_import_image = PhotoImage(file= 'Manager/import_image_hover.png')
hover_on_export_image = PhotoImage(file= 'Manager/export_image_hover.png')
search_icon_image_hover = PhotoImage(file= 'Manager/search_icon_hover.png')
generate_button_image_hover = PhotoImage(file= 'Manager/generate_button_image_hover.png')
copy_button_hover_image =  PhotoImage(file= 'Manager/copy_button_image_hover.png')
button_image = PhotoImage(file='Manager/button_image_.png')
copy_image = PhotoImage(file='Manager/copy_button_image.png')
add_data_new_image = PhotoImage(file='Manager/add_database_image .png')
clear_field_image = PhotoImage(file='Manager/clear_fields_image.png')
empty_fields_password_manager = PhotoImage(file = 'Manager/manager_empty_fields.png')
sno_error = PhotoImage(file = 'Manager/sno_error.png')
login_hover_image = PhotoImage(file = 'Login/login_button_hover_animation.png')
no_fields_checked = PhotoImage(file = 'Manager/manager_empty_password_fields.png')
check_buton_img_disabled = PhotoImage(file='Manager/check_button_disabled.png')
check_buton_img_enabled = PhotoImage(file='Manager/check_button_enabled.png')
check_button_hover_image = PhotoImage(file='Manager/check_button_hover_image.png')

# Default Page
switch_page(sign_up_page)

# Window Parameters
height_of_win = 723
width_of_win = 1160
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_cord = (screen_width / 2) - (width_of_win / 2)
y_cord = (screen_height / 2.5) - (height_of_win / 2.5)

# Centering the window
window.geometry('%dx%d+%d+%d' % (width_of_win, height_of_win, x_cord, y_cord))
window.overrideredirect(True)

# Widgets
baground = Label(sign_up_page,image = sign_up_img,bg = 'black')
username_field = Entry(sign_up_page,width=25, bd=0,fg = '#b7b7b7', font=('Roboto Medium', 17), bg  ='#1d1d1f',insertbackground = '#626262')
password_field1 = Entry(sign_up_page,width=25, bd=0,fg = '#b7b7b7', font=('Roboto Medium', 17), bg  ='#1d1d1f',insertbackground = '#626262')
password_field2 = Entry(sign_up_page,width=25, bd=0,fg = '#b7b7b7', font=('Roboto Medium', 17), bg  ='#1d1d1f',insertbackground = '#626262')
sign_up_button = Button(sign_up_page,bd = 0,image=sign_up_button_image,activebackground = '#1d1d1f', bg ='#1a1a1c')
exit_button_1 = Button(sign_up_page,activebackground = 'black',image = exit_button_image,bd = 0, bg ='#1a1a1c')

def button_Click(e):
    global invalid_counter

    if password_field2.get() == password_field1.get():
        if len(password_field2.get()) >= 8:

            conn = sqlite3.connect("sign_up.db")
            c = conn.cursor()

            c.execute("""CREATE TABLE IF NOT EXISTS signup (
            username DATATYPE,
            password TEXT
            )""")

            a = username_field.get()
            b = password_field1.get()

            c.execute(f"INSERT INTO signup VALUES ('{a}','{b}')")

            switch_page(login_page)
            conn.commit()
            conn.close()
        else:
            baground.config(image=less_characters_sign_up)
    else:
        baground.config(image = invalid_password_page)

def login_button_pressed(e):
    global invalid_counter
    conn = sqlite3.connect("sign_up.db")
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS signup (
    username DATATYPE,
    password TEXT
    )""")
    c.execute("SELECT * FROM signup")
    for u in c.fetchall():
        print(u)
    a = True
    if login_username_field.get() == u[0] and login_password_field1.get() == u[1]:
        window.withdraw()

        new_window = Toplevel()
        password_manager_page = Frame(new_window)
        password_generator_page = Frame(new_window)

        def change_page(frame):
            frame.tkraise()

        # Arranging all frames
        for frames in (password_generator_page, password_manager_page):
            frames.grid(row=0, column=0, sticky='news')

        # Window Parameters
        height_of_win = 864
        width_of_win = 1450
        screen_width = new_window.winfo_screenwidth()
        screen_height = new_window.winfo_screenheight()
        x_cord = (screen_width / 2) - (width_of_win / 2)
        y_cord = (screen_height / 2.5) - (height_of_win / 2.5)

        # Centering the window
        new_window.resizable(False,False)
        new_window.geometry('%dx%d+%d+%d' % (width_of_win, height_of_win, x_cord, y_cord))
        new_window.iconbitmap('icon.ico')

        # widgets
        change_page(password_manager_page)
        background = Label(password_manager_page,image = manager_baground,bd =0)

        # Treeview
        paz_tree = ttk.Treeview(password_manager_page)
        paz_tree['column'] = ['sno','website_name','username','password']

        # styling the elements
        Style = ttk.Style()
        Style.theme_use('default')
        Style.configure("Treeview", background="#202022",borderwidth = 0,fieldbackground = '#202022',
        foreground="#5d5d5f",rowheight = 45,highlightbackground ='red',bd= 0,highlightcolor = 'white',font = ('Arial',15))
        Style.configure("Treeview.Heading",borderwidth = 0,bd= 0, background="#202022", foreground="#989898",font = ('Arial',14),)
        Style.map("Treeview",background = [('selected','#202022')],foreground = [('selected','#e4e4e4')])
        #styling rows
        paz_tree.column('#0',width = 0,minwidth = 0)
        paz_tree.column('sno',width = 140,minwidth = 40,anchor = CENTER)
        paz_tree.column('website_name',width = 290,minwidth = 50,anchor = CENTER)
        paz_tree.column('username',width = 310,minwidth = 80,anchor = CENTER)
        paz_tree.column('password',width = 290,minwidth = 40,anchor = CENTER)

        # style headings
        paz_tree.heading("sno",text = 'SNO')
        paz_tree.heading("website_name",text = 'WEBSITE')
        paz_tree.heading("username",text = 'USERNAME')
        paz_tree.heading("password",text = 'PASSWORD')
        new_window.title('Password Manager')
        conn = sqlite3.connect('password_data.db')
        c = conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS passwords (
        sno TEXT,
        website_name TEXT,
        username TEXT,
        password TEXT
        )""")

        c.execute("SELECT * FROM passwords")
        rows = c.fetchall()
        print('rows are ',rows)

        # widgets
        entr = Entry(password_manager_page,width = 2,font = ('Hack',14),bg = '#1f1f21',bd = 0,fg = '#989898',insertbackground='#626262')
        entr1 = Entry(password_manager_page,bg = '#202022',bd = 0,fg = '#989898',width = 28,font = ('Hack',11),insertbackground='#626262')
        entr2 = Entry(password_manager_page,bg = '#202022',bd = 0,fg = '#989898',width = 28,font = ('Hack',11),insertbackground='#626262')
        entr3 = Entry(password_manager_page,bg = '#202022',bd = 0,fg = '#989898',width = 28,font = ('Hack',11),insertbackground='#626262')
        copy_to_clip_button = Button(password_manager_page,image = copy_image, activebackground='#1a1a1c',bd= 0,bg='#1a1a1c')
        copy_to_clip_button_1 = Button(password_manager_page,image = copy_image, activebackground='#1a1a1c',bd= 0,bg='#1a1a1c')
        copy_to_clip_button_2 = Button(password_manager_page,image = copy_image, activebackground='#1a1a1c',bd= 0,bg='#1a1a1c')
        generated_password_Filed = Entry(password_manager_page,justify='center',bg = '#1f1f21',bd = 0,fg = '#989898',width = 30,font = ('Hack',11))

        # New widgets
        search_box = Entry(password_manager_page, width=25, bd=0, fg='#7b7b7b', font=('Roboto Medium', 16), bg='#202022',insertbackground='#626262')
        search_button = Button(password_manager_page, bd=0, image=search_icon_image, activebackground='#1a1a1c', bg='#202022')
        refresh_button = Button(password_manager_page,bd= 0,image = refresh_icon_image, activebackground='#202022', bg='#202022')
        importButton =  Button(password_manager_page,bd= 0,image = import_icon_image, activebackground='#202022', bg='#202022')
        exportButton =  Button(password_manager_page,bd= 0,image = export_icon_image, activebackground='#202022', bg='#202022')
        b1=  Button(password_manager_page,bd= 0,image = button_image, activebackground='#202022', bg='#202022')
        b2 =  Button(password_manager_page,bd= 0,image = update_button_image, activebackground='#202022', bg='#202022')
        b3=  Button(password_manager_page,bd= 0,image = delete_button_image , activebackground='#202022', bg='#202022')
        b4=  Button(password_manager_page,bd= 0,image = reset_button_image  , activebackground='#202022', bg='#202022')
        b5=  Button(password_manager_page,bd= 0,image = logout_button_image, activebackground='#202022', bg='#202022')

        clear_button=  Button(password_manager_page,bd= 0,image = clear_field_image, activebackground='#202022', bg='#202022')
        add_button =  Button(password_manager_page,bd= 0,image = add_data_new_image, activebackground='#202022', bg='#202022')
        generate_button_image_pro = PhotoImage(file = 'Manager/generate_button_image.png')

        # Griding the widgets
        check_button1 = Label(password_manager_page,bd = 0,image = check_buton_img_disabled)
        check_button2 = Label(password_manager_page,bd = 0,image = check_buton_img_disabled)
        check_button3 = Label(password_manager_page,bd = 0,image = check_buton_img_disabled)
        check_button4 = Label(password_manager_page,bd = 0,image = check_buton_img_disabled)
        generate_button = Label(password_manager_page,bd = 0,image = generate_button_image_pro)

        def copy_wbsite_name_to_clip_board(e):
            password_gen = entr1.get()
            password_manager_page.clipboard_clear()
            password_manager_page.clipboard_append(password_gen)
            password_manager_page.update()

        def copy_username_name_to_clip_board(e):
            password_gen = entr2.get()
            password_manager_page.clipboard_clear()
            password_manager_page.clipboard_append(password_gen)
            password_manager_page.update()

        def copy_password_name_to_clip_board(e):
            password_gen = entr3.get()
            password_manager_page.clipboard_clear()
            password_manager_page.clipboard_append(password_gen)
            password_manager_page.update()

        def copy_generated_password(e):
            password_gen = generated_password_Filed.get()
            print(password_gen)
            password_manager_page.clipboard_clear()
            password_manager_page.clipboard_append(password_gen)
            password_manager_page.update()

        # copy-to-clipboard
        copy_to_clip_button.bind("<Button>",copy_wbsite_name_to_clip_board)
        copy_to_clip_button_1.bind("<Button>",copy_username_name_to_clip_board)
        copy_to_clip_button_2.bind("<Button>",copy_password_name_to_clip_board)

        def button_clicked(e):
            global total_clicks
            total_clicks += 2
            if total_clicks == 2:
                check_button1.config(image = check_buton_img_enabled)
            if total_clicks == 4:
                check_button1.config(image = check_buton_img_disabled)
                total_clicks = 0

        def button_clicked1(e):
            global total_clicks1
            total_clicks1 += 2
            if total_clicks1 == 2:
                check_button2.config(image = check_buton_img_enabled)
            if total_clicks1 == 4:
                check_button2.config(image = check_buton_img_disabled)
                total_clicks1 = 0

        def button_clicked2(e):
            global total_clicks2
            total_clicks2 += 2
            if total_clicks2 == 2:
                check_button3.config(image = check_buton_img_enabled)
            if total_clicks2 == 4:
                check_button3.config(image = check_buton_img_disabled)
                total_clicks2 = 0

        def button_clicked3(e):
            global total_clicks3
            total_clicks3 += 2
            if total_clicks3 == 2:
                check_button4.config(image = check_buton_img_enabled)
            if total_clicks3 == 4:
                check_button4.config(image = check_buton_img_disabled)
                total_clicks3 = 0

        def generate_random_password(e):

            turned_on = 'pyimage43'
            turned_off = 'pyimage42'

            if check_button1['image'] == turned_off and check_button2['image'] == turned_off and check_button3['image'] == turned_off and check_button4['image'] == turned_off:

                background.config(image = no_fields_checked)
                generated_password_Filed.delete(0, END)


            if check_button1['image'] == turned_on and check_button2['image'] == turned_on and check_button3['image'] == turned_on and check_button4['image'] == turned_on:

                background.config(image=manager_baground)
                characters = list(string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%^&*()")

                random.shuffle(characters)
                password = []

                for i in range(17):
                    password.append(random.choice(characters))

                random.shuffle(password)

                new_password = "".join(password)

                generated_password_Filed.delete(0, END)
                generated_password_Filed.insert(0, new_password)

            if check_button1['image'] == turned_on and check_button2['image'] == turned_off and check_button3['image'] == turned_off and check_button4['image'] == turned_off:

                background.config(image=manager_baground)

                characters = list(string.ascii_uppercase)
                print('moba')
                random.shuffle(characters)
                password = []

                for i in range(17):
                    password.append(random.choice(characters))

                random.shuffle(password)

                new_password = "".join(password)

                generated_password_Filed.delete(0, END)
                generated_password_Filed.insert(0, new_password)

            if check_button1['image'] == turned_off and check_button2['image'] == turned_on and check_button3['image'] == turned_off and check_button4['image'] == turned_off:

                background.config(image=manager_baground)
                characters = list(string.ascii_lowercase)
                random.shuffle(characters)
                password = []

                for i in range(17):
                    password.append(random.choice(characters))

                random.shuffle(password)

                new_password = "".join(password)

                generated_password_Filed.delete(0, END)
                generated_password_Filed.insert(0, new_password)

            if check_button1['image'] == turned_off and check_button2['image'] == turned_off and check_button3['image'] == turned_on and check_button4['image'] == turned_off:

                background.config(image=manager_baground)
                characters = list(string.digits)
                random.shuffle(characters)
                password = []

                for i in range(17):
                    password.append(random.choice(characters))

                random.shuffle(password)

                new_password = "".join(password)

                generated_password_Filed.delete(0, END)
                generated_password_Filed.insert(0, new_password)


            if check_button1['image'] == turned_off and check_button2['image'] == turned_off and check_button3['image'] == turned_off and check_button4['image'] == turned_on:

                background.config(image=manager_baground)
                characters = list('!@#$%^&*()')

                random.shuffle(characters)
                password = []
                for i in range(17):
                    password.append(random.choice(characters))
                random.shuffle(password)

                new_password = "".join(password)

                generated_password_Filed.delete(0, END)
                generated_password_Filed.insert(0, new_password)


            if check_button1['image'] == turned_off and check_button4['image'] == turned_off and check_button2['image'] == turned_on and check_button3['image'] == turned_on:

                background.config(image=manager_baground)
                characters = list(string.ascii_lowercase + '!@#$%^&*()')
                random.shuffle(characters)
                password = []

                for i in range(17):
                    password.append(random.choice(characters))

                random.shuffle(password)

                new_password = "".join(password)

                generated_password_Filed.delete(0, END)
                generated_password_Filed.insert(0, new_password)

            if check_button1['image'] == turned_on and check_button4['image'] == turned_on and check_button2['image'] == turned_off and check_button3['image'] == turned_off:

                background.config(image=manager_baground)
                characters = list(string.ascii_uppercase + '!@#$%^&*()')
                print(
                'ass'
                )
                random.shuffle(characters)
                password = []

                for i in range(17):
                    password.append(random.choice(characters))

                random.shuffle(password)

                new_password = "".join(password)

                generated_password_Filed.delete(0, END)
                generated_password_Filed.insert(0, new_password)

            if check_button1['image'] == turned_on and check_button4['image'] == turned_off and check_button2['image'] == turned_off and check_button3['image'] == turned_on:

                background.config(image=manager_baground)
                characters = list(string.ascii_uppercase + string.digits)
                print('mo')
                random.shuffle(characters)
                password = []

                for i in range(17):
                    password.append(random.choice(characters))

                random.shuffle(password)

                new_password = "".join(password)

                generated_password_Filed.delete(0, END)
                generated_password_Filed.insert(0, new_password)

            if check_button1['image'] == turned_on and check_button4['image'] == turned_off and check_button2['image'] == turned_on and check_button3['image'] == turned_off:

                background.config(image=manager_baground)
                characters = list(string.ascii_uppercase + string.ascii_lowercase)
                random.shuffle(characters)
                password = []

                for i in range(17):
                    password.append(random.choice(characters))

                random.shuffle(password)

                new_password = "".join(password)

                generated_password_Filed.delete(0, END)
                generated_password_Filed.insert(0, new_password)

            if check_button1['image'] == turned_off and check_button4['image'] == turned_off and check_button2['image'] == turned_on and check_button3['image'] == turned_on:

                background.config(image=manager_baground)
                characters = list(string.ascii_lowercase + string.digits)
                random.shuffle(characters)

                password = []

                for i in range(17):
                    password.append(random.choice(characters))

                random.shuffle(password)

                new_password = "".join(password)

                generated_password_Filed.delete(0, END)
                generated_password_Filed.insert(0, new_password)

            if check_button1['image'] == turned_on and check_button2['image'] == turned_off and check_button3['image'] == turned_on and check_button4['image'] == turned_on:

                background.config(image=manager_baground)
                characters = list(string.ascii_uppercase + '!@#$%^&*()' + string.digits)
                random.shuffle(characters)
                password = []

                for i in range(17):
                    password.append(random.choice(characters))

                random.shuffle(password)

                new_password = "".join(password)

                generated_password_Filed.delete(0, END)
                generated_password_Filed.insert(0, new_password)

            if check_button1['image'] == turned_off and check_button2['image'] == turned_on and check_button3['image'] == turned_on and check_button4['image'] == turned_on:

                background.config(image=manager_baground)
                characters = list(string.ascii_lowercase + '!@#$%^&*()' + string.digits)
                print('sike')
                random.shuffle(characters)
                password = []

                for i in range(17):
                    password.append(random.choice(characters))

                random.shuffle(password)

                new_password = "".join(password)

                generated_password_Filed.delete(0, END)
                generated_password_Filed.insert(0, new_password)



            if check_button1['image'] == turned_on and check_button2['image'] == turned_on and check_button3['image'] == turned_on and check_button4['image'] == turned_on:

                background.config(image=manager_baground)
                characters = list(string.ascii_lowercase  + string.ascii_uppercase + '!@#$%^&*()' + string.digits)

                random.shuffle(characters)
                password = []

                for i in range(17):
                    password.append(random.choice(characters))
                random.shuffle(password)

                new_password = "".join(password)

                generated_password_Filed.delete(0, END)
                generated_password_Filed.insert(0, new_password)

            if check_button1['image'] == turned_on and check_button2['image'] == turned_on and check_button3['image'] == turned_on and check_button4['image'] == turned_off:

                background.config(image=manager_baground)
                characters = list(string.ascii_lowercase  + string.ascii_uppercase + string.digits)
                random.shuffle(characters)
                password = []

                for i in range(17):
                    password.append(random.choice(characters))

                random.shuffle(password)

                new_password = "".join(password)

                generated_password_Filed.delete(0, END)
                generated_password_Filed.insert(0, new_password)

            if check_button1['image'] == turned_on and check_button2['image'] == turned_on and check_button3['image'] == turned_off and check_button4['image'] == turned_on:

                background.config(image=manager_baground)
                characters = list(string.ascii_lowercase  + string.ascii_uppercase + '!@#$%^&*()')

                random.shuffle(characters)
                password = []
                for i in range(17):
                    password.append(random.choice(characters))

                random.shuffle(password)

                new_password = "".join(password)

                generated_password_Filed.delete(0, END)
                generated_password_Filed.insert(0, new_password)

            if check_button1['image'] == turned_off and check_button2['image'] == turned_off and check_button3['image'] == turned_on and check_button4['image'] == turned_on:

                background.config(image=manager_baground)
                characters = list(string.digits + '!@#$%^&*()')

                random.shuffle(characters)
                password = []
                for i in range(17):
                    password.append(random.choice(characters))

                random.shuffle(password)

                new_password = "".join(password)

                generated_password_Filed.delete(0, END)
                generated_password_Filed.insert(0, new_password)


        def adding_data(e):
            global iid_val
            global added_sno
            global new_list

            conn = sqlite3.connect('password_data.db')
            c = conn.cursor()

            sno_inp = entr.get()
            website_name = entr1.get()
            username_inp = entr2.get()
            password_inp = entr3.get()

            if sno_inp == '' or website_name == '' or username_inp == ''or password_inp == '':
                background.config(image = empty_fields_password_manager)
            else:
                background.config(image=manager_baground)
                c.execute('select sno from passwords;')
                row = c.fetchall()

                for a in row:
                    new_list.append(a[0])


                if sno_inp in new_list:
                    background.config(image=sno_error)
                else:
                    background.config(image = manager_baground)

                    c.execute("""CREATE TABLE IF NOT EXISTS passwords (
                    sno TEXT,
                    website_name TEXT,
                    username TEXT,
                    password TEXT
                    )""")

                    paz_tree.insert(iid=iid_val, index='end', parent='', values=(f'{sno_inp}', f'{website_name}', f'{username_inp}', f'{password_inp}'))
                    c.execute(f"INSERT INTO passwords VALUES ('{sno_inp}','{website_name}','{username_inp}','{password_inp}')")
                    iid_val += 1

                    entr.delete(0, END)
                    entr1.delete(0, END)
                    entr2.delete(0, END)
                    entr3.delete(0, END)

                    conn.commit()
                    conn.close()

        def update_data(e):
            global new_list
            conn = sqlite3.connect("password_data.db")
            c = conn.cursor()
            sno = entr.get()
            website_name = entr1.get()
            username = entr2.get()
            passwords = entr3.get()
            print(sno,website_name,username,passwords)

            row = c.fetchall()
            print('new row',row)
            selected = paz_tree.focus()
            value = paz_tree.item(selected, 'values')
            sno_old = str(value[0])

            c.execute(f"""UPDATE passwords SET website_name = '{website_name}',sno = '{sno}',username = '{username}',password = '{passwords}'
                WHERE sno = '{sno_old}'
            """)

            paz_tree.item(selected,text = '',values = (sno,website_name,username,passwords))

            entr.delete(0,END)
            entr1.delete(0,END)
            entr2.delete(0,END)
            entr3.delete(0,END)

            conn.commit()
            conn.close()

        def delete_data(e):
            global x
            conn = sqlite3.connect('password_data.db')
            c = conn.cursor()

            x = paz_tree.selection()[0]
            selected = paz_tree.focus()
            final_values = paz_tree.item(selected, 'values')
            sno = final_values[0]

            c.execute("SELECT * FROM passwords")
            c.execute("DELETE FROM passwords where sno = ?", (sno,))
            paz_tree.delete(x)

            # closing the connection between front-end and back-end
            conn.commit()
            conn.close()

        def selectItem(a):
            selected = paz_tree.focus()
            final_values = paz_tree.item(selected, 'values')
            sno = final_values[0]
            website_name = final_values[1]
            username = final_values[2]
            password = final_values[3]

            # removing existing data
            entr.delete(0,END)
            entr1.delete(0,END)
            entr2.delete(0,END)
            entr3.delete(0,END)

            # adding new data
            entr.insert(0,sno)
            entr1.insert(0,website_name)
            entr2.insert(0,username)
            entr3.insert(0,password)

        def clear_Fields(e):
            entr.delete(0,END)
            entr1.delete(0,END)
            entr2.delete(0,END)
            entr3.delete(0,END)

        # Exit
        def exit_application(e):
            new_window.destroy()

        # export files to computer
        def export_Files(e):
            files = [('Max PC Safe Encrypted File', '*.ENX')]
            file = filedialog.asksaveasfile(filetypes=files,initialfile = 'password_data', defaultextension=files)
            old_directory = os.getcwd() + '\password_data.db'
            new_directory = file.name
            shutil.copyfile(src = old_directory,dst = new_directory)
            messagebox.showinfo("Export successful",'Your passwords has been exported successfully!')

        # Move data into program
        def import_Files(e):
            files = [('Max PC Safe Encrypted File', '*.ENX')]
            file = filedialog.askopenfile(filetypes=files,initialfile = 'red', defaultextension=files)
            old_directory = os.getcwd()
            new_directory = file.name # gets the file path

            shutil.copy(src = new_directory,dst = old_directory)
            os.remove('password_data.db')

            file_name = os.path.basename(new_directory)
            messagebox.showinfo('Import successfull', 'Your passwords has been imported successfully, a restart is required to view changes ')
            new_window.destroy()

            os.startfile("main.exe")

            # if os.path.isfile('main.pyw'):
            #     os.startfile("main.pyw")
            # else:


            os.rename(file_name, 'password_data.db')

        def search_records(e):
            lookup_record = search_box.get()

            for record in paz_tree.get_children():
                paz_tree.delete(record)

            conn = sqlite3.connect('password_data.db')

            c = conn.cursor()

            c.execute('SELECT website_name, * FROM passwords WHERE website_name LIKE "%{}%"'.format(lookup_record))
            records = c.fetchall()

            global count
            count = 0

            for record in records:
                print(record)
                if count % 2 == 0:
                    paz_tree.insert(parent='', index='end', iid=count, text='',
                                   values=(record[1],record[0],record[3],record[4]),
                                   tags=('evenrow',))
                    print('insert chekc')
                else:
                    paz_tree.insert(parent='', index='end', iid=count, text='',
                                   values=(record[1],record[0],record[3],record[4]),
                                   tags=('evenrow',))
                count += 1
            conn.commit()
            conn.close()

        def refresh_treeview_page(e):
            for item in paz_tree.get_children():
                paz_tree.delete(item)

            conn = sqlite3.connect("password_data.db")
            c = conn.cursor()

            c.execute("SELECT * FROM passwords")
            rows = c.fetchall()

            for row in rows:
                print(row)
                paz_tree.insert("", END, values=row)

            c.execute("""CREATE TABLE IF NOT EXISTS passwords (
            sno TEXT,website_name TEXT,username TEXT,password TEXT)""")

            conn.commit()
            conn.close()

        # --- Delete data from treeview and sqlite3 ---
        def delete_file(e):

            response = messagebox.askyesno('Confirmation',' Are you sure, you want to delete all your passwords? ')

            if response == True:
                os.remove(os.getcwd() + '\password_data.db')
                for i in paz_tree.get_children():
                    paz_tree.delete(i)
                messagebox.showinfo('Reset Complete ',' All passwords have been deleted, a restart is required.')
                new_window.destroy()
                os.startfile('main.exe')

            if response == False:
                pass

        paz_tree.bind('<Button-1>', selectItem)
        check_button1.bind('<Button-1>',button_clicked)
        check_button2.bind('<Button-1>',button_clicked1)
        check_button3.bind('<Button-1>',button_clicked2)
        check_button4.bind('<Button-1>',button_clicked3)
        search_button.bind("<Button>",search_records)
        refresh_button.bind("<Button>",refresh_treeview_page)
        importButton.bind("<Button>", import_Files)
        exportButton.bind("<Button>", export_Files)

        # Printing data on rows and columns
        conn = sqlite3.connect("password_data.db")
        c = conn.cursor()

        c.execute("SELECT * FROM passwords")
        rows = c.fetchall()

        # thsi code converts SQL data and shows into treeview
        for row in rows:
            print(row)
            paz_tree.insert("", END, values=row)

        c.execute("""CREATE TABLE IF NOT EXISTS passwords (
        sno TEXT,website_name TEXT,username TEXT,password TEXT)""")

        conn.commit()
        conn.close()
        copy_password_button = Button(password_manager_page,bd= 0,image = copy_image, activebackground='#1a1a1c', bg='#1a1a1c')

        def hover_on_add_button(e):
            b1.config(image = hover_image_add_button)
        def hover_realeased_add_button(e):
            b1.config(image = button_image)

        def hover_on_update_button(e):
            b2.config(image = hover_image_update_button)
        def hover_realeased_update_button(e):
            b2.config(image = update_button_image)

        def hover_on_delete_button(e):
            b3.config(image = hover_image_delete_button)
        def hover_realeased_delete_button(e):
            b3.config(image = delete_button_image)

        def hover_on_reset_button(e):
            b4.config(image = hover_image_reset_button)
        def hover_realeased_reset_button(e):
            b4.config(image = reset_button_image)

        def hover_on_log_out_button(e):
            b5.config(image = hover_image_log_out)
        def hover_released_log_out_button(e):
            b5.config(image = logout_button_image)

        def hover_on_clear_field_button(e):
            clear_button.config(image = hover_image_clearfields)
        def hover_released_clear_field_button(e):
            clear_button.config(image = clear_field_image )

        def hover_on_add_hover_button(e):
            add_button.config(image = hover_image_add_button_small)
        def hover_released_hover_field_button(e):
            add_button.config(image = add_data_new_image)

        def hover_on_refresh_hover_button(e):
            refresh_button.config(image = hover_on_refresh_image)
        def hover_released_hover_refresh_button(e):
            refresh_button.config(image = refresh_icon_image)

        def hover_on_import_hover_button(e):
            importButton.config(image = hover_on_import_image)
        def hover_released_import_button(e):
            importButton.config(image = import_icon_image)

        def hover_on_export_hover_button(e):
            exportButton.config(image = hover_on_export_image)
        def hover_released_export_button(e):
            exportButton.config(image = export_icon_image)

        def hover_on_search_hover_button(e):
            search_button.config(image = search_icon_image_hover)
        def hover_released_search_button(e):
            search_button.config(image = search_icon_image)

        def hover_on_generate_hover_button(e):
            generate_button.config(image = generate_button_image_hover)
        def hover_released_generate__button(e):
            generate_button.config(image = generate_button_image_pro)

        def copy_on_hover(e):
            copy_to_clip_button.config(image = copy_button_hover_image)
        def copy_on_leave(e):
            copy_to_clip_button.config(image = copy_image)

        def copy_on_hover1(e):
            copy_to_clip_button_1.config(image = copy_button_hover_image)
        def copy_on_leave1(e):
            copy_to_clip_button_1.config(image = copy_image)

        def copy_on_hover2(e):
            copy_to_clip_button_2.config(image = copy_button_hover_image)
        def copy_on_leave2(e):
            copy_to_clip_button_2.config(image = copy_image)

        def copy_on_hover3(e):
            copy_password_button.config(image = copy_button_hover_image)
        def copy_on_leave3(e):
            copy_password_button.config(image = copy_image)

        # --- Gridding the widgets ---
        background.grid(row = 1,column = 1,columnspan = 100,rowspan = 100)
        search_box.grid(row = 2,column = 84)
        search_button.grid(row = 2,column= 91)
        refresh_button.grid(row = 2,column = 81)
        importButton.grid(row = 2,column= 23,rowspan = 2)
        exportButton.grid(row = 2,column= 24,rowspan = 2)
        b1.grid(row = 22,column = 10)
        b2.grid(row = 24,column = 10)
        b3.grid(row = 26,column = 10)
        b4.grid(row = 28,column = 10)
        b5.grid(row = 91,column = 10)
        entr.grid(row = 34,column = 1,columnspan = 70,rowspan = 60)
        entr1.grid(row = 34,column = 11,columnspan = 70,rowspan = 60)
        entr2.grid(row = 48,column = 11,columnspan = 70,rowspan = 60)
        entr3.grid(row = 70,column = 11,columnspan = 70,rowspan = 70)
        add_button.grid(row = 90,column = 9,columnspan = 75,rowspan =100)
        clear_button.grid(row = 90,column = 10,columnspan = 75,rowspan =100)
        copy_to_clip_button.grid(row = 34,column = 15,columnspan = 70,rowspan = 60)
        copy_to_clip_button_1.grid(row = 48,column = 15,columnspan = 70,rowspan = 60)
        copy_to_clip_button_2.grid(row = 70,column = 15,columnspan = 70,rowspan = 60)
        generated_password_Filed.grid(row = 62,column = 67,rowspan=15,columnspan= 69)
        paz_tree.grid(row = 1,column = 12,rowspan = 69,columnspan = 200)
        copy_password_button.grid(row = 62,column = 85,rowspan=15,columnspan= 5)
        check_button1.grid(row = 75,column= 41,columnspan=50,rowspan=15)
        check_button2.grid(row = 79,column= 41,columnspan=50,rowspan=14)
        check_button3.grid(row = 75,column= 72,columnspan=50,rowspan=15)
        check_button4.grid(row = 79,column= 72,columnspan=50,rowspan=14)
        generate_button.grid(row = 90,column = 62,columnspan = 75,rowspan =100)

        # --- Binding the widgets ----
        b1.bind("<Button>",adding_data)
        b2.bind('<Button>',update_data)
        b3.bind('<Button>',delete_data)
        b1.bind('<Enter>',hover_on_add_button)
        b1.bind('<Leave>',hover_realeased_add_button)
        b2.bind('<Enter>',hover_on_update_button)
        b2.bind('<Leave>',hover_realeased_update_button)
        b3.bind('<Enter>',hover_on_delete_button)
        b3.bind('<Leave>',hover_realeased_delete_button)
        b4.bind('<Enter>',hover_on_reset_button)
        b4.bind('<Leave>',hover_realeased_reset_button)
        b4.bind("<Button>",delete_file)
        b5.bind('<Enter>',hover_on_log_out_button)
        b5.bind('<Leave>',hover_released_log_out_button)
        clear_button.bind('<Enter>',hover_on_clear_field_button)
        clear_button.bind('<Leave>',hover_released_clear_field_button)
        add_button.bind('<Enter>',hover_on_add_hover_button)
        add_button.bind('<Leave>',hover_released_hover_field_button)
        refresh_button.bind('<Enter>',hover_on_refresh_hover_button)
        refresh_button.bind('<Leave>',hover_released_hover_refresh_button)
        importButton.bind('<Enter>',hover_on_import_hover_button)
        importButton.bind('<Leave>',hover_released_import_button)
        exportButton.bind('<Enter>',hover_on_export_hover_button)
        exportButton.bind('<Leave>',hover_released_export_button)
        search_button.bind('<Enter>',hover_on_search_hover_button)
        search_button.bind('<Leave>',hover_released_search_button)
        generate_button.bind('<Enter>',hover_on_generate_hover_button)
        generate_button.bind('<Leave>',hover_released_generate__button)
        generate_button.bind('<Button>',generate_random_password)
        copy_password_button.bind('<Button>',copy_generated_password)
        copy_to_clip_button.bind('<Enter>',copy_on_hover)
        copy_to_clip_button.bind('<Leave>',copy_on_leave)
        copy_to_clip_button_1.bind('<Enter>',copy_on_hover1)
        copy_to_clip_button_1.bind('<Leave>',copy_on_leave1)
        copy_to_clip_button_2.bind('<Enter>',copy_on_hover2)
        copy_to_clip_button_2.bind('<Leave>',copy_on_leave2)
        copy_password_button.bind('<Enter>',copy_on_hover3)
        copy_password_button.bind('<Leave>',copy_on_leave3)
        clear_button.bind("<Button>",clear_Fields)
        b5.bind("<Button>", exit_applicaation)
        add_button.bind("<Button>",adding_data)
        new_window.mainloop()

    # --- condition if password was wrong  ---
    else:
        login_bag.config(image = login_incorrect)
        invalid_counter +=  1
        if invalid_counter == 3:
            messagebox.showerror('< Invalid Password - Program Terminated > ','You have entered the wrong password for more than 3 times.')
            window.destroy()

def exit_applicaation(e):
    window.after(1,lambda:window.destroy())


# --- Gridding the widgets ---
baground.grid(row=1, column=1, columnspan=100, rowspan=100)
username_field.grid(row=37, column=78)
password_field1.grid(row=48, column=78)
password_field2.grid(row=58, column=78)
sign_up_button.grid(row=52, column=31, columnspan=100, rowspan=100)
exit_button_1.grid(row = 2,column = 100)

def hover_over_sing_up_button(e):
    sign_up_button.config(image=sing_up_button_hover)

def leave_hover_over_sing_up_button(e):
    sign_up_button.config(image=sign_up_button_image)

# Widget Binding
sign_up_button.bind("<Button>",button_Click)
sign_up_button.bind("<Enter>",hover_over_sing_up_button)
sign_up_button.bind("<Leave>",leave_hover_over_sing_up_button)

# Creating the login widgets
login_bag = Label(login_page,image = login_page_img,bg = 'black') #'#1d1d1f'
login_username_field = Entry(login_page,width=25, bd=0,fg = '#b7b7b7', font=('Roboto Medium', 17), bg  ='#1d1d1f',insertbackground = '#626262')
login_password_field1 = Entry(login_page,width=25, show = '*', bd=0,fg = '#b7b7b7', font=('Roboto Medium', 17), bg  ='#1d1d1f',insertbackground = '#626262')
log_in_button = Button(login_page,image = login_button_img,bd=  0,activebackground = '#1d1d1f', bg ='#1d1d1f')
exit_button_2 = Button(login_page,activebackground = '#1d1d1f',image = exit_button_image,bd = 0, bg ='#1a1a1c')
show_hide_button = Button(login_page,activebackground = '#1d1d1f',image = eyes_closed_icon,bd = 0, bg ='#1a1a1c')

# Griding the widgets
login_bag.grid(row = 1,column = 1,columnspan = 100,rowspan = 100)
exit_button_2.grid(row = 1,column = 100)
login_username_field.grid(row =40,column = 36,columnspan = 100)
login_password_field1.grid(row = 54,column = 36,columnspan = 100)
show_hide_button.grid(row = 54,column =72,columnspan = 100)
log_in_button.grid(row = 65,column = 23,columnspan = 100)

exit_button_2.bind('<Button>',exit_applicaation)
exit_button_1.bind('<Button>',exit_applicaation)
# hover animations
def hover_over_sing_up_button(e):
    sign_up_button.config(image=sing_up_button_hover)

def leave_hover_over_sing_up_button(e):
    sign_up_button.config(image=sign_up_button_image)

# Show hide functionality
def change(e):
    global button_clicks1
    button_clicks1 += 1

    if button_clicks1 % 2 == 0:
        show_hide_button.config(image = eyes_open_icon)
        login_password_field1.config(show = '*')
    else:
        show_hide_button.config(image = eyes_closed_icon)
        login_password_field1.config(show = '')

def login_button_hover(e):
    log_in_button.config(image = login_hover_image)

def login_button_leave(e):
    log_in_button.config(image = login_button_img)

# Binding the widgets
log_in_button.bind('<Button>',login_button_pressed)
log_in_button.bind('<Enter>',login_button_hover)
log_in_button.bind('<Leave>',login_button_leave)
sign_up_button.bind("<Button>",button_Click)
show_hide_button.bind('<Button>',change)

# Check weather the user already has an account
if os.path.isfile('sign_up.db'):
    switch_page(login_page)
else:
    switch_page(sign_up_page)

# Displaying the window
window.mainloop()