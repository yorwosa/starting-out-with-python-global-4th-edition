# This program displays two labels with text.

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
        self.label1.pack()
        self.label2.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()

# Create an instance of the MyGUI class.
my_gui = MyGUI()

