from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project


def create_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
               'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)  # Adauga toate elementele din lista ca un singur String
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()  # .get() - Preia info introduse in fiecare entry
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }}
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Reading old data
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)  # Sterge din entry informatiile anterioare
            password_entry.delete(0, END)


# ---------------------------- SEARCH FUNCTION ------------------------------- #


def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            # Reading old data
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="This data file does not exist")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email:{email}\n" f"Password:{password}")
        elif len(website) == 0:
            messagebox.showinfo(title="Error", message=f"Please write an address!")
        else:
            messagebox.showinfo(title="Error", message=f"Sorry,no entries saved for '{website}' account!")


# ---------------------------- UI SETUP ------------------------------- #

# Create Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Create Canvas with logo
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Create Labels

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Create Entries

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()  # Se deschide fereastra cu focus pe website entries
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "danielionut17@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Create Buttons

password_button = Button(text="Generate Pass", command=create_password)
password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=29, command=save)
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text="Search", width=10, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
