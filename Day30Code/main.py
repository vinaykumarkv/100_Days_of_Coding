from tkinter import *
import random
import string
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    a2z = string.ascii_uppercase
    a2z = [*a2z]
    print(a2z)
    n = [str(i) for i in range(1, 10)]
    n = [*n]
    print(n)
    Sy = string.punctuation
    Sy = [*Sy]
    print(Sy)
    passwd = ""
    la = lnum = ls = 9
    for i in range(la):
        passwd = passwd + (random.choice(a2z))
    print(passwd)
    for j in range(lnum):
        passwd = passwd + (random.choice(n))
    print(passwd)
    for j in range(ls):
        passwd = passwd + (random.choice(Sy))
    print(passwd)
    passwd = [*passwd]
    random.shuffle(passwd)
    passwd = ''.join(passwd)
    Password.insert(END, f"{passwd}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    email = Email.get()
    website = Website.get()
    password = Password.get()
    if len(email) == 0 or len(website) ==0 or len(password)==0:
        messagebox.showinfo(title="oops", message="Please check the details!!\n All fields are mandatory")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\n is it OK to save?")
        if is_ok == True:
            try:
                with open("data.txt", "a") as data_file:
                    data_file.write(f"{website} | {email} | {password}\n")
                    Website.delete(0, END)
                    Password.delete(0, END)
            except FileNotFoundError:
                messagebox.showinfo(title="File Not Found",
                                    message="Please check if application is installed correctly\n and Re-install the application")
            except KeyError as error:
                messagebox.showinfo(title="File Not Found",
                                    message= f"{error}")




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Website Label
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0, sticky="E")

# Website field
Website = Entry(width=35)
Website.focus()
Website.grid(row=1, column=1, columnspan=2)



# Email Label
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="E")


# Email/Username field
Email = Entry(width=35)
Email.insert(0, "vinay@sample.com")
Email.grid(row=2, column=1, columnspan=2)

# Password Label
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="E")

# Password field
Password = Entry(width=21)
Password.grid(row=3, column=1, sticky="W", padx=22)

# Generate Password Button

#calls action() when pressed
gen_button = Button(text="Generate Password", command=password_generator)
gen_button.grid(row=3, column=1, sticky="E")


# Add Password Button


#calls action() when pressed
add_button = Button(text="Add", command=add_password, height=1, width=36)
add_button.grid(row=4, column=1)

window.mainloop()


