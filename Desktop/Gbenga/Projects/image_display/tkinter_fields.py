from tkinter import *

root = Tk()

entries  = Entry(root, width=50, bg='green')
entries.pack()
entries.insert(0, 'Enter your name: ')


def my_click():
    user_says = 'Hello, how are you today :  '  +  entries.get()
    my_label = Label(root, text= user_says)
    my_label.pack()

my_button = Button(root, text='Click Me', padx=100, command=my_click, fg='teal', bg='magenta')

my_button.pack()


root.mainloop() 