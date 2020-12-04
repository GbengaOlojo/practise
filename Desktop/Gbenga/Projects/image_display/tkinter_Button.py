from tkinter import *

root = Tk()

def my_click():
    my_label = Label(root, text='Click the button to manually view the displayable pictures')
    my_label.pack()

my_button = Button(root, text='Click Me', padx=100, command=my_click, fg='teal', bg='magenta')

my_button.pack()


root.mainloop() 