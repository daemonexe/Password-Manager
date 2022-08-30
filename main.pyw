# Required Modules
import random
import sqlite3
from tkinter import *
import os
from tkinter import ttk
from tkinter import filedialog
import shutil
from tkinter import messagebox

# Creaing the function
window = Tk()
iid_val = 0
added_sno = []

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
login_succesful = PhotoImage(file = 'Login/login_succesful_img.png')
less_characters_sign_up = PhotoImage(file = 'Sign_Up/less_characters_sign_up_img.png')
manager_baground = PhotoImage(file = 'Manager/manager.png')
hover_on_exit = PhotoImage(file = 'Hover Animations/Exit On hover.png')
hover_on_reset = PhotoImage(file = 'Hover Animations/reset_on_hover.png')
hover_on_add = PhotoImage(file = 'Hover Animations/hover on add.png')
hover_on_delete = PhotoImage(file = 'Hover Animations/hover delete.png')
hover_on_update = PhotoImage(file = 'Hover Animations/Update on hover.png')
hover_on_import = PhotoImage(file = 'Hover Animations/import on hover.png')
hover_on_export = PhotoImage(file = 'Hover Animations/export hover.png')
new_button = PhotoImage(file = 'Manager/button.png')
update_button = PhotoImage(file = 'Manager/update_button.png')
delete_button = PhotoImage(file = 'Manager/delete_button.png')
reset_button = PhotoImage(file = 'Manager/reset_button.png')
import_button = PhotoImage(file = 'Manager/import_button.png')
export_button = PhotoImage(file = 'Manager/export_button.png')
exit_button = PhotoImage(file = 'Manager/exit_button.png')
copy_button_img = PhotoImage(file = 'Manager/copy button.png')
add_button_new = PhotoImage(file = 'Manager/add_button.png')
new_copy_image = PhotoImage(file = 'Manager/new copy image.png')
check_button_disable_img = PhotoImage(file = 'Manager/clicker_disabled.png')
check_button_enabled_img = PhotoImage(file = 'Manager/clicker_enabled.png')
generate_button_image = PhotoImage(file = 'Manager/generate_button.png')
clear_fields_button_image = PhotoImage(file = 'Manager/clear_Feild_img.png')

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

# Creating the widgets :
baground = Label(sign_up_page,image = sign_up_img,bg = 'black')
username_field = Entry(sign_up_page,width=17, bd=0, font=('Arial Bold', 21), bg='#ebebeb')
password_field1 = Entry(sign_up_page,width=17, bd=0, font=('Arial', 21), bg='#ebebeb')
password_field2 = Entry(sign_up_page,width=17, bd=0, font=('Arial', 21), bg='#ebebeb')
exit_button_1 = Button(sign_up_page,text = 'X',width = 3,bd = 0,font = ('arial bold',10),bg = 'red',fg = 'white')

invalid_counter = 0
total_clicks = 0
total_clicks1 = 0
total_clicks2 = 0
total_clicks3 = 0

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
            print("insertion succesfull ")
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

    if login_username_field.get() == u[0] and login_password_field1.get() == u[1]:
        login_bag.config(image = login_succesful)
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
        height_of_win = 838
        width_of_win = 1388
        screen_width = new_window.winfo_screenwidth()
        screen_height = new_window.winfo_screenheight()
        x_cord = (screen_width / 2) - (width_of_win / 2)
        y_cord = (screen_height / 2.5) - (height_of_win / 2.5)

        # Centering the window
        new_window.resizable(False,False)
        new_window.geometry('%dx%d+%d+%d' % (width_of_win, height_of_win, x_cord, y_cord))


        # Creating the widgets
        change_page(password_manager_page)
        background = Label(password_manager_page,image = manager_baground,bd =0)

        # Treeview
        paz_tree = ttk.Treeview(password_manager_page)
        paz_tree['column'] = ['sno','website_name','username','password']

        # Style

        Style = ttk.Style()
        Style.theme_use('default')
        Style.configure("Treeview", background="white",
        foreground="black",rowheight = 45,bd= 0,highlightcolor = 'white',font = ('Helvetica',15))

        Style.configure("Treeview.Heading", background="#171a1f", foreground="white",font = ('arial',14))
        Style.map("Treeview",background = [('selected','#ECECEC')],foreground = [('selected','#753de1')])

        #Customising rows
        paz_tree.column('#0',width = 0,minwidth = 0)
        paz_tree.column('sno',width = 200,minwidth = 40,anchor = CENTER)
        paz_tree.column('website_name',width = 240,minwidth = 40,anchor = CENTER)
        paz_tree.column('username',width = 260,minwidth = 40,anchor = CENTER)
        paz_tree.column('password',width = 310,minwidth = 40,anchor = CENTER)

        # Creaitng headings
        paz_tree.heading("sno",text = 'Sno')
        paz_tree.heading("website_name",text = 'Website')
        paz_tree.heading("username",text = 'Username')
        paz_tree.heading("password",text = 'Password')
        new_window.title('Password Manager - 2.0.2')
        conn = sqlite3.connect('password_data.db')
        c = conn.cursor()

        new_window.iconbitmap('icon.ico')

        c.execute("""CREATE TABLE IF NOT EXISTS passwords (
        sno TEXT,
        website_name TEXT,
        username TEXT,
        password TEXT
        )""")

        c.execute("SELECT * FROM passwords")
        rows = c.fetchall()
        print('rows are ',rows)

        entr = Entry(password_manager_page,width = 2,font = ('arial',14),bg = '#111418',bd = 0,fg = 'white')
        entr1 = Entry(password_manager_page,bg = '#111418',bd = 0,fg = 'white',width = 24,font = ('arial',12))
        entr2 = Entry(password_manager_page,bg = '#111418',bd = 0,fg = 'white',width = 24,font = ('arial',12))
        entr3 = Entry(password_manager_page,bg = '#111418',bd = 0,fg = 'white',width = 24,font = ('arial',12))
        generated_password_Filed = Entry(password_manager_page,justify='center',bg = '#111418',bd = 0,fg = 'white',width = 28,font = ('arial',12))


        # Griding the widgets
        button1 = Label(password_manager_page,bd= 0,image = new_button)
        button2 = Label(password_manager_page,bd= 0,image = update_button)
        button3 = Label(password_manager_page,bd= 0,image = delete_button)
        button4 = Label(password_manager_page,bd= 0,image = import_button)
        button5 = Label(password_manager_page,bd= 0,image = export_button)
        button6 = Label(password_manager_page,bd= 0,image = reset_button)
        button7 = Label(password_manager_page,bd= 0,image = exit_button)
        button8 = Label(password_manager_page,bd= 0,image = add_button_new)
        button9 = Label(password_manager_page,bd= 0,image = clear_fields_button_image)
        copy1 = Label(password_manager_page,bd= 0,image = new_copy_image)
        copy2 = Label(password_manager_page,bd= 0,image = new_copy_image)
        copy3 = Label(password_manager_page,bd= 0,image = new_copy_image)
        check_button1 = Label(password_manager_page,bd = 0,image = check_button_disable_img)
        check_button2 = Label(password_manager_page,bd = 0,image = check_button_disable_img)
        check_button3 = Label(password_manager_page,bd = 0,image = check_button_disable_img)
        check_button4 = Label(password_manager_page,bd = 0,image = check_button_disable_img)
        generate_button = Label(password_manager_page,bd = 0,image = generate_button_image)

        # Animations
        def on_hover_exit(e):
            button7.config(image = hover_on_exit)
        def on_leave_exit(e):
            button7.config(image = exit_button)
        def on_hover_reset(e):
            button6.config(image = hover_on_reset)
        def on_leave_reset(e):
            button6.config(image = reset_button)
        def on_hover_add(e):
            button1.config(image = hover_on_add)
        def on_leave_add(e):
            button1.config(image = new_button)
        def on_hover_update(e):
            button2.config(image = hover_on_update)
        def on_leave_update(e):
            button2.config(image = update_button)
        def on_hover_delete(e):
            button3.config(image = hover_on_delete)
        def on_leave_delete(e):
            button3.config(image = delete_button)
        def on_hover_import(e):
            button4.config(image = hover_on_import)
        def on_leave_import(e):
            button4.config(image = import_button)
        def on_hover_export(e):
            button5.config(image = hover_on_export)
        def on_leave_export(e):
            button5.config(image = export_button)

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

        button7.bind("<Enter>",on_hover_exit)
        button7.bind("<Leave>",on_leave_exit)
        button6.bind("<Enter>",on_hover_reset)
        button6.bind("<Leave>",on_leave_reset)
        button1.bind("<Enter>",on_hover_add)
        button1.bind("<Leave>",on_leave_add)
        button2.bind("<Enter>",on_hover_update)
        button2.bind("<Leave>",on_leave_update)
        button3.bind("<Enter>",on_hover_delete)
        button3.bind("<Leave>",on_leave_delete)
        button4.bind("<Enter>",on_hover_import)
        button4.bind("<Leave>",on_leave_import)
        button5.bind("<Enter>",on_hover_export)
        button5.bind("<Leave>",on_leave_export)
        copy1.bind("<Button>",copy_wbsite_name_to_clip_board)
        copy2.bind("<Button>",copy_username_name_to_clip_board)
        copy3.bind("<Button>",copy_password_name_to_clip_board)

        # Enable clicking options (Function)
        # HELLO THIS A NEW ADDED CODE PLEASE CHEK THIS OUT
        def button_clicked(e):
            global total_clicks
            total_clicks += 2
            if total_clicks == 2:
                check_button1.config(image = check_button_enabled_img)
            if total_clicks == 4:
                check_button1.config(image = check_button_disable_img)
                total_clicks = 0

        def button_clicked1(e):
            global total_clicks1
            total_clicks1 += 2
            if total_clicks1 == 2:
                check_button2.config(image = check_button_enabled_img)
            if total_clicks1 == 4:
                print(check_button_disable_img)
                check_button2.config(image = check_button_disable_img)
                total_clicks1 = 0

        def button_clicked2(e):
            global total_clicks2
            total_clicks2 += 2
            if total_clicks2 == 2:
                check_button4.config(image = check_button_enabled_img)
            if total_clicks2 == 4:
                check_button4.config(image = check_button_disable_img)
                total_clicks2 = 0

        def button_clicked3(e):
            global total_clicks3
            total_clicks3 += 2
            if total_clicks3 == 2:
                check_button3.config(image = check_button_enabled_img)
            if total_clicks3 == 4:
                check_button3.config(image = check_button_disable_img)
                total_clicks3 = 0

        def generate_random_password(e):

            DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

            LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

            UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

            SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']

            print(check_button1['image'])

            # Enabled 28 Disabled 27
            # Possible combinations LU NU US LS LN SL
            if check_button1['image'] == 'pyimage28' and check_button2['image'] == 'pyimage28'and check_button3['image'] == 'pyimage28' and check_button4['image'] == 'pyimage28':
                a1 = random.choice(DIGITS)
                a2 = random.choice(SYMBOLS)
                a3 = random.choice(UPCASE_CHARACTERS)
                a4 = random.choice(DIGITS)
                a5 = random.choice(SYMBOLS)
                a6 = random.choice(UPCASE_CHARACTERS)
                a7 = random.choice(UPCASE_CHARACTERS)
                a8 = random.choice(SYMBOLS)
                a9 = random.choice(LOCASE_CHARACTERS)
                a10 = random.choice(DIGITS)
                a11 = random.choice(DIGITS)
                a12 = random.choice(SYMBOLS)
                a13 = random.choice(LOCASE_CHARACTERS)
                a14 = random.choice(SYMBOLS)
                a15 = random.choice(LOCASE_CHARACTERS)
                a16 = random.choice(DIGITS)

                generated_password = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 +a11 +a12 + a13 +a14 + a15 + a16

                generated_password_Filed.delete(0,END)
                generated_password_Filed.insert(0,generated_password)
            if check_button1['image'] == 'pyimage28' and check_button2['image'] == 'pyimage27'and check_button3['image'] == 'pyimage27' and check_button4['image'] == 'pyimage27':
                a1 = random.choice(UPCASE_CHARACTERS)
                a2 = random.choice(UPCASE_CHARACTERS)
                a3 = random.choice(UPCASE_CHARACTERS)
                a4 = random.choice(UPCASE_CHARACTERS)
                a5 = random.choice(UPCASE_CHARACTERS)
                a6 = random.choice(UPCASE_CHARACTERS)
                a7 = random.choice(UPCASE_CHARACTERS)
                a8 = random.choice(UPCASE_CHARACTERS)
                a9 = random.choice(UPCASE_CHARACTERS)
                a10 = random.choice(UPCASE_CHARACTERS)
                a11 = random.choice(UPCASE_CHARACTERS)
                a12 = random.choice(UPCASE_CHARACTERS)
                a13 = random.choice(UPCASE_CHARACTERS)
                a14 = random.choice(UPCASE_CHARACTERS)
                a15 = random.choice(UPCASE_CHARACTERS)
                a16 = random.choice(UPCASE_CHARACTERS)

                generated_password = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 +a11 +a12 + a13 +a14 + a15 + a16

                generated_password_Filed.delete(0,END)
                generated_password_Filed.insert(0,generated_password)
            if check_button1['image'] == 'pyimage27' and check_button2['image'] == 'pyimage28'and check_button3['image'] == 'pyimage27' and check_button4['image'] == 'pyimage27':
                a1 = random.choice(DIGITS)
                a2 = random.choice(DIGITS)
                a3 = random.choice(DIGITS)
                a4 = random.choice(DIGITS)
                a5 = random.choice(DIGITS)
                a6 = random.choice(DIGITS)
                a7 = random.choice(DIGITS)
                a8 = random.choice(DIGITS)
                a9 = random.choice(DIGITS)
                a10 = random.choice(DIGITS)
                a11 = random.choice(DIGITS)
                a12 = random.choice(DIGITS)
                a13 = random.choice(DIGITS)
                a14 = random.choice(DIGITS)
                a15 = random.choice(DIGITS)
                a16 = random.choice(DIGITS)

                generated_password = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 +a11 +a12 + a13 +a14 + a15 + a16

                generated_password_Filed.delete(0,END)
                generated_password_Filed.insert(0,generated_password)
            if check_button1['image'] == 'pyimage27' and check_button2['image'] == 'pyimage27'and check_button3['image'] == 'pyimage28' and check_button4['image'] == 'pyimage27':
                a1 = random.choice(SYMBOLS)
                a2 = random.choice(SYMBOLS)
                a3 = random.choice(SYMBOLS)
                a4 = random.choice(SYMBOLS)
                a5 = random.choice(SYMBOLS)
                a6 = random.choice(SYMBOLS)
                a7 = random.choice(SYMBOLS)
                a8 = random.choice(SYMBOLS)
                a9 = random.choice(SYMBOLS)
                a10 = random.choice(SYMBOLS)
                a11 = random.choice(SYMBOLS)
                a12 = random.choice(SYMBOLS)
                a13 = random.choice(SYMBOLS)
                a14 = random.choice(SYMBOLS)
                a15 = random.choice(SYMBOLS)
                a16 = random.choice(SYMBOLS)

                generated_password = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 +a11 +a12 + a13 +a14 + a15 + a16

                generated_password_Filed.delete(0,END)
                generated_password_Filed.insert(0,generated_password)
            if check_button1['image'] == 'pyimage27' and check_button2['image'] == 'pyimage27'and check_button3['image'] == 'pyimage27' and check_button4['image'] == 'pyimage28':
                a1 = random.choice(LOCASE_CHARACTERS)
                a2 = random.choice(LOCASE_CHARACTERS)
                a3 = random.choice(LOCASE_CHARACTERS)
                a4 = random.choice(LOCASE_CHARACTERS)
                a5 = random.choice(LOCASE_CHARACTERS)
                a6 = random.choice(LOCASE_CHARACTERS)
                a7 = random.choice(LOCASE_CHARACTERS)
                a8 = random.choice(LOCASE_CHARACTERS)
                a9 = random.choice(LOCASE_CHARACTERS)
                a10 = random.choice(LOCASE_CHARACTERS)
                a11 = random.choice(LOCASE_CHARACTERS)
                a12 = random.choice(LOCASE_CHARACTERS)
                a13 = random.choice(LOCASE_CHARACTERS)
                a14 = random.choice(LOCASE_CHARACTERS)
                a15 = random.choice(LOCASE_CHARACTERS)
                a16 = random.choice(LOCASE_CHARACTERS)

                generated_password = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 +a11 +a12 + a13 +a14 + a15 + a16

                generated_password_Filed.delete(0,END)
                generated_password_Filed.insert(0,generated_password)

            # 2 Selected at a time 1U,2N,3S,4L

            if check_button1['image'] == 'pyimage27' and check_button4['image'] == 'pyimage28'and check_button2['image'] == 'pyimage27'and check_button3['image'] == 'pyimage28':
                a1 = random.choice(LOCASE_CHARACTERS)
                a2 = random.choice(SYMBOLS)
                a3 = random.choice(SYMBOLS)
                a4 = random.choice(LOCASE_CHARACTERS)
                a5 = random.choice(SYMBOLS)
                a6 = random.choice(LOCASE_CHARACTERS)
                a7 = random.choice(LOCASE_CHARACTERS)
                a8 = random.choice(SYMBOLS)
                a9 = random.choice(LOCASE_CHARACTERS)
                a10 = random.choice(LOCASE_CHARACTERS)
                a11 = random.choice(SYMBOLS)
                a12 = random.choice(LOCASE_CHARACTERS)
                a13 = random.choice(SYMBOLS)
                a14 = random.choice(LOCASE_CHARACTERS)
                a15 = random.choice(SYMBOLS)
                a16 = random.choice(SYMBOLS)
                generated_password = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 +a11 +a12 + a13 +a14 + a15 + a16

                generated_password_Filed.delete(0,END)
                generated_password_Filed.insert(0,generated_password)
            if check_button1['image'] == 'pyimage28' and check_button4['image'] == 'pyimage27'and check_button2['image'] == 'pyimage27'and check_button3['image'] == 'pyimage28':
                a1 = random.choice(UPCASE_CHARACTERS)
                a2 = random.choice(UPCASE_CHARACTERS)
                a3 = random.choice(SYMBOLS)
                a4 = random.choice(UPCASE_CHARACTERS)
                a5 = random.choice(SYMBOLS)
                a6 = random.choice(UPCASE_CHARACTERS)
                a7 = random.choice(UPCASE_CHARACTERS)
                a8 = random.choice(SYMBOLS)
                a9 = random.choice(UPCASE_CHARACTERS)
                a10 = random.choice(UPCASE_CHARACTERS)
                a11 = random.choice(SYMBOLS)
                a12 = random.choice(UPCASE_CHARACTERS)
                a13 = random.choice(SYMBOLS)
                a14 = random.choice(UPCASE_CHARACTERS)
                a15 = random.choice(SYMBOLS)
                a16 = random.choice(SYMBOLS)

                generated_password = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 +a11 +a12 + a13 +a14 + a15 + a16

                generated_password_Filed.delete(0,END)
                generated_password_Filed.insert(0,generated_password)
            if check_button1['image'] == 'pyimage28' and check_button4['image'] == 'pyimage27'and check_button2['image'] == 'pyimage28'and check_button3['image'] == 'pyimage27':
                a1 = random.choice(UPCASE_CHARACTERS)
                a2 = random.choice(UPCASE_CHARACTERS)
                a3 = random.choice(DIGITS)
                a4 = random.choice(UPCASE_CHARACTERS)
                a5 = random.choice(DIGITS)
                a6 = random.choice(UPCASE_CHARACTERS)
                a7 = random.choice(UPCASE_CHARACTERS)
                a8 = random.choice(DIGITS)
                a9 = random.choice(UPCASE_CHARACTERS)
                a10 = random.choice(UPCASE_CHARACTERS)
                a11 = random.choice(DIGITS)
                a12 = random.choice(UPCASE_CHARACTERS)
                a13 = random.choice(DIGITS)
                a14 = random.choice(UPCASE_CHARACTERS)
                a15 = random.choice(DIGITS)
                a16 = random.choice(DIGITS)

                generated_password = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 +a11 +a12 + a13 +a14 + a15 + a16

                generated_password_Filed.delete(0,END)
                generated_password_Filed.insert(0,generated_password)
            if check_button1['image'] == 'pyimage28' and check_button4['image'] == 'pyimage28'and check_button2['image'] == 'pyimage27'and check_button3['image'] == 'pyimage27':
                a1 = random.choice(UPCASE_CHARACTERS)
                a2 = random.choice(UPCASE_CHARACTERS)
                a3 = random.choice(LOCASE_CHARACTERS)
                a4 = random.choice(UPCASE_CHARACTERS)
                a5 = random.choice(LOCASE_CHARACTERS)
                a6 = random.choice(UPCASE_CHARACTERS)
                a7 = random.choice(UPCASE_CHARACTERS)
                a8 = random.choice(LOCASE_CHARACTERS)
                a9 = random.choice(UPCASE_CHARACTERS)
                a10 = random.choice(UPCASE_CHARACTERS)
                a11 = random.choice(LOCASE_CHARACTERS)
                a12 = random.choice(UPCASE_CHARACTERS)
                a13 = random.choice(LOCASE_CHARACTERS)
                a14 = random.choice(UPCASE_CHARACTERS)
                a15 = random.choice(LOCASE_CHARACTERS)
                a16 = random.choice(LOCASE_CHARACTERS)

                generated_password = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 +a11 +a12 + a13 +a14 + a15 + a16

                generated_password_Filed.delete(0,END)
                generated_password_Filed.insert(0,generated_password)
            if check_button1['image'] == 'pyimage27' and check_button4['image'] == 'pyimage28'and check_button2['image'] == 'pyimage28'and check_button3['image'] == 'pyimage27':
                a1 = random.choice(UPCASE_CHARACTERS)
                a2 = random.choice(DIGITS)
                a3 = random.choice(LOCASE_CHARACTERS)
                a4 = random.choice(DIGITS)
                a5 = random.choice(LOCASE_CHARACTERS)
                a6 = random.choice(DIGITS)
                a7 = random.choice(UPCASE_CHARACTERS)
                a8 = random.choice(LOCASE_CHARACTERS)
                a9 = random.choice(DIGITS)
                a10 = random.choice(UPCASE_CHARACTERS)
                a11 = random.choice(LOCASE_CHARACTERS)
                a12 = random.choice(DIGITS)
                a13 = random.choice(DIGITS)
                a14 = random.choice(UPCASE_CHARACTERS)
                a15 = random.choice(DIGITS)
                a16 = random.choice(LOCASE_CHARACTERS)

                generated_password = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 +a11 +a12 + a13 +a14 + a15 + a16

                generated_password_Filed.delete(0,END)
                generated_password_Filed.insert(0,generated_password)
            if check_button1['image'] == 'pyimage27' and check_button4['image'] == 'pyimage27'and check_button2['image'] == 'pyimage28'and check_button3['image'] == 'pyimage28':
                a1 = random.choice(UPCASE_CHARACTERS)
                a2 = random.choice(UPCASE_CHARACTERS)
                a3 = random.choice(DIGITS)
                a4 = random.choice(DIGITS)
                a5 = random.choice(SYMBOLS)
                a6 = random.choice(DIGITS)
                a7 = random.choice(SYMBOLS)
                a8 = random.choice(SYMBOLS)
                a9 = random.choice(DIGITS)
                a10 = random.choice(SYMBOLS)
                a11 = random.choice(SYMBOLS)
                a12 = random.choice(DIGITS)
                a13 = random.choice(DIGITS)
                a14 = random.choice(SYMBOLS)
                a15 = random.choice(DIGITS)
                a16 = random.choice(SYMBOLS)

                generated_password = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 +a11 +a12 + a13 +a14 + a15 + a16

                generated_password_Filed.delete(0,END)
                generated_password_Filed.insert(0,generated_password)
            if check_button1['image'] == 'pyimage27' and check_button4['image'] == 'pyimage28'and check_button2['image'] == 'pyimage27'and check_button3['image'] == 'pyimage28':
                a1 = random.choice(LOCASE_CHARACTERS)
                a2 = random.choice(SYMBOLS)
                a3 = random.choice(LOCASE_CHARACTERS)
                a4 = random.choice(DIGITS)
                a5 = random.choice(LOCASE_CHARACTERS)
                a6 = random.choice(DIGITS)
                a7 = random.choice(LOCASE_CHARACTERS)
                a8 = random.choice(LOCASE_CHARACTERS)
                a9 = random.choice(DIGITS)
                a10 = random.choice(LOCASE_CHARACTERS)
                a11 = random.choice(LOCASE_CHARACTERS)
                a12 = random.choice(DIGITS)
                a13 = random.choice(DIGITS)
                a14 = random.choice(LOCASE_CHARACTERS)
                a15 = random.choice(DIGITS)
                a16 = random.choice(LOCASE_CHARACTERS)

                generated_password = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 +a11 +a12 + a13 +a14 + a15 + a16

                generated_password_Filed.delete(0,END)
                generated_password_Filed.insert(0,generated_password)

            # Single empty field option :

            if check_button1['image'] == 'pyimage28' and check_button2['image'] == 'pyimage28'and check_button3['image'] == 'pyimage28' and check_button4['image'] == 'pyimage27':
                a1 = random.choice(UPCASE_CHARACTERS)
                a2 = random.choice(SYMBOLS)
                a3 = random.choice(SYMBOLS)
                a4 = random.choice(DIGITS)
                a5 = random.choice(UPCASE_CHARACTERS)
                a6 = random.choice(SYMBOLS)
                a7 = random.choice(DIGITS)
                a8 = random.choice(UPCASE_CHARACTERS)
                a9 = random.choice(SYMBOLS)
                a10 = random.choice(UPCASE_CHARACTERS)
                a11 = random.choice(SYMBOLS)
                a12 = random.choice(DIGITS)
                a13 = random.choice(SYMBOLS)
                a14 = random.choice(UPCASE_CHARACTERS)
                a15 = random.choice(DIGITS)
                a16 = random.choice(UPCASE_CHARACTERS)

                generated_password = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 +a11 +a12 + a13 +a14 + a15 + a16

                generated_password_Filed.delete(0,END)
                generated_password_Filed.insert(0,generated_password)
            if check_button1['image'] == 'pyimage28' and check_button2['image'] == 'pyimage28'and check_button3['image'] == 'pyimage27' and check_button4['image'] == 'pyimage28':
                a1 = random.choice(LOCASE_CHARACTERS)
                a2 = random.choice(SYMBOLS)
                a3 = random.choice(SYMBOLS)
                a4 = random.choice(DIGITS)
                a5 = random.choice(UPCASE_CHARACTERS)
                a6 = random.choice(UPCASE_CHARACTERS)
                a7 = random.choice(LOCASE_CHARACTERS)
                a8 = random.choice(UPCASE_CHARACTERS)
                a9 = random.choice(SYMBOLS)
                a10 = random.choice(LOCASE_CHARACTERS)
                a11 = random.choice(LOCASE_CHARACTERS)
                a12 = random.choice(DIGITS)
                a13 = random.choice(SYMBOLS)
                a14 = random.choice(UPCASE_CHARACTERS)
                a15 = random.choice(DIGITS)
                a16 = random.choice(LOCASE_CHARACTERS)

                generated_password = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 +a11 +a12 + a13 +a14 + a15 + a16

                if check_button1['image'] == 'pyimage28' and check_button2['image'] == 'pyimage28' and check_button3['image'] == 'pyimage27' and check_button4['image'] == 'pyimage28':

                    generated_password_Filed.delete(1,END)
                    generated_password_Filed.insert(0,generated_password)
                    a1 = random.choice(UPCASE_CHARACTERS)
                    a2 = random.choice(DIGITS)
                    a3 = random.choice(LOCASE_CHARACTERS)
                    a4 = random.choice(UPCASE_CHARACTERS)
                    a5 = random.choice(UPCASE_CHARACTERS)
                    a6 = random.choice(LOCASE_CHARACTERS)
                    a7 = random.choice(DIGITS)
                    a8 = random.choice(UPCASE_CHARACTERS)
                    a9 = random.choice(DIGITS)
                    a10 = random.choice(UPCASE_CHARACTERS)
                    a11 = random.choice(UPCASE_CHARACTERS)
                    a12 = random.choice(DIGITS)
                    a13 = random.choice(DIGITS)
                    a14 = random.choice(UPCASE_CHARACTERS)
                    a15 = random.choice(LOCASE_CHARACTERS)
                    a16 = random.choice(UPCASE_CHARACTERS)

                    generated_password = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 +a11 +a12 + a13 +a14 + a15 + a16

                    generated_password_Filed.delete(0,END)
                    generated_password_Filed.insert(0,generated_password)


            if check_button1['image'] == 'pyimage28' and check_button2['image'] == 'pyimage27'and check_button3['image'] == 'pyimage28' and check_button4['image'] == 'pyimage28':
                a1 = random.choice(UPCASE_CHARACTERS)
                a2 = random.choice(SYMBOLS)
                a3 = random.choice(LOCASE_CHARACTERS)
                a4 = random.choice(SYMBOLS)
                a5 = random.choice(SYMBOLS)
                a6 = random.choice(LOCASE_CHARACTERS)
                a7 = random.choice(SYMBOLS)
                a8 = random.choice(UPCASE_CHARACTERS)
                a9 = random.choice(UPCASE_CHARACTERS)
                a10 = random.choice(LOCASE_CHARACTERS)
                a11 = random.choice(UPCASE_CHARACTERS)
                a12 = random.choice(SYMBOLS)
                a13 = random.choice(SYMBOLS)
                a14 = random.choice(UPCASE_CHARACTERS)
                a15 = random.choice(LOCASE_CHARACTERS)
                a16 = random.choice(UPCASE_CHARACTERS)

                generated_password = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 +a11 +a12 + a13 +a14 + a15 + a16

                generated_password_Filed.delete(0,END)
                generated_password_Filed.insert(0,generated_password)
            if check_button1['image'] == 'pyimage27' and check_button2['image'] == 'pyimage28'and check_button3['image'] == 'pyimage28' and check_button4['image'] == 'pyimage28':
                a1 = random.choice(DIGITS)
                a2 = random.choice(SYMBOLS)
                a3 = random.choice(LOCASE_CHARACTERS)
                a4 = random.choice(SYMBOLS)
                a5 = random.choice(SYMBOLS)
                a6 = random.choice(LOCASE_CHARACTERS)
                a7 = random.choice(SYMBOLS)
                a8 = random.choice(SYMBOLS)
                a9 = random.choice(DIGITS)
                a10 = random.choice(LOCASE_CHARACTERS)
                a11 = random.choice(LOCASE_CHARACTERS)
                a12 = random.choice(SYMBOLS)
                a13 = random.choice(SYMBOLS)
                a14 = random.choice(LOCASE_CHARACTERS)
                a15 = random.choice(LOCASE_CHARACTERS)
                a16 = random.choice(DIGITS)

                generated_password = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 +a11 +a12 + a13 +a14 + a15 + a16

                generated_password_Filed.delete(0,END)
                generated_password_Filed.insert(0,generated_password)

        def adding_data(e):
            global iid_val
            global added_sno
            conn = sqlite3.connect('password_data.db')
            c = conn.cursor()

            sno_inp = entr.get()
            website_name = entr1.get()
            username_inp = entr2.get()
            password_inp = entr3.get()

            # Creating the db if not exists
            c.execute("""CREATE TABLE IF NOT EXISTS passwords (
            sno TEXT,
            website_name TEXT,
            username TEXT,
            password TEXT
            )""")


            paz_tree.insert(iid=iid_val, index='end', parent='', values=(f'{sno_inp}', f'{website_name}', f'{username_inp}', f'{password_inp}'))
            c.execute(f"INSERT INTO passwords VALUES ('{sno_inp}','{website_name}','{username_inp}','{password_inp}')")
            iid_val += 1

            # Clsoning the conntection
            conn.commit()
            conn.close()

        def update_data(e):
            conn = sqlite3.connect("password_data.db")
            c = conn.cursor()
            sno = entr.get()
            website_name = entr1.get()
            username = entr2.get()
            passwords = entr3.get()
            print(sno,website_name,username,passwords)

            c.execute("SELECT * FROM passwords")

            selected = paz_tree.focus()
            value = paz_tree.item(selected, 'values')
            sno_old = str(value[0])

            c.execute(f"""UPDATE passwords SET website_name = '{website_name}',sno = '{sno}',username = '{username}',password = '{passwords}'
                WHERE sno = '{sno_old}'

            """)

            paz_tree.item(selected,text = '',values = (sno,website_name,username,passwords))

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

            # Closing the connection
            conn.commit()
            conn.close()

        def selectItem(a):
            selected = paz_tree.focus()
            final_values = paz_tree.item(selected, 'values')
            sno = final_values[0]
            website_name = final_values[1]
            username = final_values[2]
            password = final_values[3]

            # Flusing
            entr.delete(0,END)
            entr1.delete(0,END)
            entr2.delete(0,END)
            entr3.delete(0,END)

            # Inserting
            entr.insert(0,sno)
            entr1.insert(0,website_name)
            entr2.insert(0,username)
            entr3.insert(0,password)

        def clear_Fields(e):
            entr.delete(0,END)
            entr1.delete(0,END)
            entr2.delete(0,END)
            entr3.delete(0,END)

        def exit_application(e):
            new_window.destroy()

        # Move Data outside
        def export_Files(e):
            files = [('Database File [Highly Encrypted]', '*.db')]
            file = filedialog.asksaveasfile(filetypes=files,initialfile = 'password_data', defaultextension=files)
            old_directory = os.getcwd() + '\password_data.db'
            new_directory = file.name
            shutil.copyfile(src = old_directory,dst = new_directory)
            messagebox.showinfo(" < Export Successful > ",'Your database file (password_data.db) has been exported to the specified directory... ')

        # Move data into program
        def import_Files(e):
            files = [('Database Files', '*.db')]
            file = filedialog.askopenfile(filetypes=files,initialfile = 'red', defaultextension=files)
            old_directory = os.getcwd()
            new_directory = file.name # gets the file path



            # Get file name :

            shutil.copy(src = new_directory,dst = old_directory)
            # delete the already existing file :
            os.remove('password_data.db')
            file_name = os.path.basename(new_directory)

            new_window.destroy()
            os.startfile("main.pyw")

            print('file removed ')

            # Rename the imported file to password_data.db
            os.rename(file_name, 'password_data.db')

            # messagebox.showinfo(" < Import Successful > ",'Database imported successfully , Restart the software to see imported data...')
            # new_window.destroy()

        def clear_data(e):
            entr.delete(0,END)
            entr1.delete(0,END)
            entr2.delete(0,END)
            entr3.delete(0,END)

        # Delete data from squlite3 and Treeview
        def delete_file(e):
            file = os.getcwd() + '\password_data.db'
            os.remove(file)
            messagebox.showwarning(" < Reset Successful > ",'Your database file has been erased, restart the software to flush the data ')
            new_window.destroy()

        button7.bind("<Button>",exit_application)
        paz_tree.bind('<Button-1>', selectItem)
        button8.bind("<Button>",clear_Fields)
        button4.bind("<Button>",import_Files)
        button5.bind("<Button>",export_Files)
        button7.bind("<Button>",exit_application)
        button1.bind("<Button>",adding_data)
        button2.bind("<Button>",update_data)
        button3.bind("<Button>",delete_data)
        button6.bind("<Button>",delete_file)
        generate_button.bind("<Button>",generate_random_password)
        check_button1.bind("<Button>",button_clicked)
        check_button2.bind("<Button>",button_clicked1)
        check_button4.bind("<Button>",button_clicked2)
        check_button3.bind("<Button>",button_clicked3)
        button8.bind("<Button>",adding_data)
        button9.bind("<Button>", clear_data)

        # Printing data on rows and columns
        conn = sqlite3.connect("password_data.db")
        c = conn.cursor()

        c.execute("SELECT * FROM passwords")
        rows = c.fetchall()

        # Squlite3 - Treeview
        for row in rows:
            print(row)  # it print all records in the database
            paz_tree.insert("", END, values=row)

        c.execute("""CREATE TABLE IF NOT EXISTS passwords (
        sno TEXT,website_name TEXT,username TEXT,password TEXT)""")

        conn.commit()
        conn.close()

        # Gridded widgets
        background.grid(row = 1,column = 1,columnspan = 100,rowspan = 100)
        button1.grid(row = 70,column = 3)
        button2.grid(row = 72,column = 3)
        button3.grid(row = 74,column = 3)
        button4.grid(row = 76,column = 3)
        button5.grid(row = 78,column = 3)
        button6.grid(row = 80,column = 3)
        button7.grid(row = 82,column = 3)
        paz_tree.grid(row = 4,column = 4,columnspan = 100,rowspan = 74)
        entr.grid(row = 74,column = 1,columnspan = 41,rowspan =800)
        entr1.grid(row = 74,column = 1,columnspan = 68,rowspan =300)
        entr2.grid(row = 76,column = 1,columnspan = 68,rowspan =60)
        entr3.grid(row = 77,column = 1,columnspan = 68,rowspan =500)
        button8.grid(row = 81,column = 1,columnspan = 60,rowspan =10)
        button9.grid(row = 81,column = 1,columnspan = 80,rowspan =10)
        copy1.grid(row = 74,column = 1,columnspan = 125,rowspan =800)
        copy2.grid(row = 76,column = 1,columnspan = 125,rowspan =800)
        copy3.grid(row = 77,column = 1,columnspan = 125,rowspan =800)
        generated_password_Filed.grid(row = 74,column = 45,columnspan = 200,rowspan =800)
        check_button1.grid(row = 76,column = 18,columnspan = 200,rowspan =200)
        check_button2.grid(row = 76,column = 50,columnspan = 200,rowspan =200)
        check_button3.grid(row = 78,column = 50,columnspan = 200,rowspan =200)
        check_button4.grid(row = 78,column = 18,columnspan = 200,rowspan =200)
        generate_button.grid(row = 81,column = 44,columnspan = 200,rowspan =10)

        new_window.mainloop()

    # If password is wrong
    else:
        login_bag.config(image = login_incorrect)
        invalid_counter +=  1
        if invalid_counter == 3:
            messagebox.showerror('< Invalid Password - Program Terminated > ','You have entered the wrong password for more than 3 times.')
            window.destroy()

def exit_applicaation(e):
    window.after(200,lambda:window.destroy())

# Griding the widgets!
sign_up_button = Button(sign_up_page,bd = 0,image=sign_up_button_image)
baground.grid(row=1, column=1, columnspan=100, rowspan=100)
exit_button_1.grid(row = 1,column = 100)
username_field.grid(row=40, column=80)
password_field1.grid(row=53, column=80)
password_field2.grid(row=66, column=80)
sign_up_button.grid(row=67, column=64, columnspan=100, rowspan=100)

# Widget Binding
sign_up_button.bind("<Button>",button_Click)
exit_button_1.bind("<Button>",exit_applicaation)

# Creating the login widgets
login_bag = Label(login_page,image = login_page_img,bg = 'black')
login_username_field = Entry(login_page,width=17, bd=0, font=('Arial Bold', 21), bg='#ebebeb')
login_password_field1 = Entry(login_page,show = '•',width=17, bd=0, font=('Arial', 21), bg='#ebebeb')
log_in_button = Button(login_page,bd = 0,image=login_button_img)
exit_button_2 = Button(login_page,text = 'X',width = 3,bd = 0,font = ('arial bold',10),bg = 'red',fg = 'white')

# Griding the widgets
login_bag.grid(row = 1,column = 1,columnspan = 100,rowspan = 100)
exit_button_2.grid(row = 1,column = 100)
login_username_field.grid(row =51,column = 43,columnspan = 100)
login_password_field1.grid(row = 65,column = 43,columnspan = 100)
log_in_button.grid(row = 85,column = 47,columnspan = 100)

# Binding the widgets
log_in_button.bind('<Button>',login_button_pressed)
sign_up_button.bind("<Button>",button_Click)
exit_button_2.bind("<Button>",exit_applicaation)

# Check weather the user already has an account
if os.path.isfile('sign_up.db'):
    switch_page(login_page)
else:
    switch_page(sign_up_page)

# Displaying the window
window.mainloop()