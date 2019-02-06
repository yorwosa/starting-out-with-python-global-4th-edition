# This program uses the side='left' argument with
# the pack method to change the layout of the widgets.

import tkinter

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()

        # Create two Label widget.
        self.label1 = tkinter.Label(self.main_window, \
                                    text='Hello World!')
        self.label2 = tkinter.Label(self.main_window, \
                         text='This is my GUI program.')

        # Call both Label widgets' pack method.
        self.label1.pack(side='left')
        self.label2.pack(side='left')

        # Enter the tkinter main loop.
        tkinter.mainloop()

# Create an instance of the MyGUI class.
my_gui = MyGUI()

