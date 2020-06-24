# Import Library
from tkinter import *


# Create the Application
root = Tk()

# Title
root.title("mp4 to mp3 Converter")

# Function for button
def myClick():
    myLabel = Label(root, text = "Look: I click a Button!")
    myLabel.grid(row = 0, column = 1)

# Creating a label Widget
my_label = Label(root, text = "Hello World")
my_label.grid(row = 0, column = 0)

# Creating button
my_button = Button(root, text = "Click Me!", command = myClick)
my_button.grid(row = 0, column = 1)

# Creating Entry (Input Text Box)
my_entry = Entry(root, width = 50, borderwidth = 2)
my_entry.grid(row = 1, column = 0)
my_entry.insert(0, "Enter something")

# Constant loop that ends if the program ends
root.mainloop()
