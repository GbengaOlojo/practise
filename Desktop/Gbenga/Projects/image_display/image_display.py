from tkinter import  *
'''from PIL import image, ImageTK'''
import random 
import glob
import time


class Image_display:
    
    def __init__(self, mainwin):
        self.mainwin = mainwin
        self.mainwin.title('Tkinter Picture frame') 
        self.mainwin.state('zoomed')
        self.mainwin.font('verdana')
        self.mainwin.configure(bg = 'teal')

        self.frame = tk.Frame(mainwin)
        self.frame.place(relheight = 0.85, relwidth = 0.09, relx= 0.05, rely = 0.05)

root = tk.TK()
myprog = Image_display(root)
root.mainloop()


 # device goes off and becomes non-functional
    def device_off(self):
        if device == 'No':
            return False
    device_off('off')
    print('Thanks for using the picture display device')


    # device come on and becomes functional
    def device_on(self):
        if device == 'yes':
            return True        
    device_on('On')
    print('Welcome to picture display device')
    print('How would you like to connect')
'''
   
    

    # Users select how they will like to connect their pictures to the device
    def connection_mode(self):
        Connection_A = 'Manual Connection'
        Connection_B = 'Bluetooth Connection'
        Connection_C = 'Cloud Connection'

        verify_connection =  input('Please select your connection mode: ')

        if self.connection_mode == Connection_A:

    
    def Bluetooth_on:(self)


    def Bluetooth_off(self):
    """ turns off the bluetooth """


    # After selecting the connection mode, users uploads their image
    def upload_image() 
    
    # The images begins to display 
    def begin_display(self):
        for images in device


    # Select the display time to display
    def display_duration():



    # displaying of pictures stops but device is still on 
    def stop_dislpay(self)


    # display/device goes into standy mode
    def standby_mode(self)

    # 
    def process_image(self)
    

    # the pictures will be appended or removed on prompt
    def update_image(self)


    # pictures/s will be deleted
    def delete_image(self) 

    
    # time of the day will be displayed
    def display_time(self) 

    
    # date of the year will be displayed
    def display_date(self)


    # applicable to SDcards only, available storage displayed
    def available_space()


    # users selects desired colours from list
    def background_color(self)

    # the device will randomly display pictures from all images 
    def random_display(self)


    # users could select pictures to be displayed from lists
    def queued_display(self)
'''

