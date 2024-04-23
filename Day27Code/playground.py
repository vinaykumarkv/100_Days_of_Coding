from tkinter import *

window = Tk()
window.title('My First GUI')
window.minsize(width=500, height=500)

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()
my_label["text"] = "New Text"
my_label.config(text="New Text 2")


def button_clicked():
    my_label.config(text=input.get())


button = Button(text="click me", command=button_clicked)
button.pack()

input = Entry(width = 10)
input.pack()


# def add(*n):
#     sum = 0
#     for i in n:
#         sum += i
#     return sum
# print(add(1,2,3,4,5))


window.mainloop()
