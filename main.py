from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for sym in range(nr_symbols)]
    password_list += [random.choice(numbers) for num in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)

    input_pass.delete(0, END)
    input_pass.insert(0, f'{password}')
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    web = input_website.get()
    email = input_email.get()
    pasw = input_pass.get()
    new_data = {
        web: {
            'email': email,
            'password': pasw,
        }
    }

    if len(web) == 0 or len(email) == 0 or len(pasw) == 0:
        messagebox.showinfo(message='Please do not leave inputs empty.')
    else:
        confirmation = messagebox.askokcancel(title=web, message=f'Confirm: \nEmail: {email}\nPassword: {pasw} ')
        if confirmation:
            try:
                with open('data.json', 'r') as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open('data.json', 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open('data.json', 'w') as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                input_website.delete(0, END)
                input_pass.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=30, pady=30)

canvas = Canvas(width=200, height=200)
pass_manager_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=pass_manager_img)
canvas.grid(column=1, row=0)

label_website = Label(text='Website: ')
label_website.grid(column=0, row=1)

input_website = Entry(width=35)
input_website.grid(column=1, row=1, columnspan=2)
input_website.focus()

label_email = Label(text='Email/Usernane: ')
label_email.grid(column=0, row=2)

input_email = Entry(width=35)
input_email.grid(column=1, row=2, columnspan=2)
input_email.insert(0, 'mymail@pup.ru')

label_pass = Label(text='Password: ')
label_pass.grid(column=0, row=3)

input_pass = Entry(width=21)
input_pass.grid(column=1, row=3)

button_gen_pass = Button(text='Generate password', command=generate_password)
button_gen_pass.grid(column=2, row=3)

button_add = Button(text='Add', width=36, command=save_data)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()