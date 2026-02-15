from tkinter import * 


# This code creates a simple GUI window using the Tkinter library in Python. It sets up the window's size, title, and background color, and adds a label with an image and a button that prints a message when clicked.
window = Tk() # instantiate an instance of a window
window.geometry ("1280x1080") # changing the size of the window
window.title("Cancer Pharmacogenomics Dashboard") # changing the title of the window


# icon settings
icon = PhotoImage(file=r"C:\Users\allan\Desktop\TU\Spring 2026\Projects of Data Science\Project\Helix.png") 
window.iconphoto(True, icon)
# window.config(background="grey") # changing the background color of the window
window.config(background="#2d292d") # changing the background color of the window using hex code



# Label settings
photo_Label = PhotoImage(file=r"C:\Users\allan\Desktop\TU\Spring 2026\Projects of Data Science\Project\Helix.png") # loading an image from a file
photo_Label = photo_Label.subsample(20, 20) # resizing the image to fit the label
Titlelabel = Label(window, 
                   text="Welcome to the Cancer Pharmacogenomics Dashboard!", 
                   font=("Arial", 16), 
                   bg="#2d292d", 
                   fg="white", 
                   image=photo_Label, 
                   compound='left') # creating a label with specific font and colors
# Titlelabel = Label(window, text="Welcome to the Cancer Pharmacogenomics Dashboard!", font=("Arial", 16), bg="#2d292d", fg="white") # creating a label with specific font and colors
Titlelabel.pack(pady=20) # adding the label to the window with some padding


'''
# Button settings
count = 0
def click():  # giving the button a function to execute when clicked
    global count
    count += 1
    #print(f"Button clicked {count} times!")
    Label_4_Button.config(text=count) # updating the label text to show the new count
    if count == 10: # if the button has been clicked 10 times
        Label_4_Button.config(text="Button clicked 10 times!") # update the label text to show a message
        
Button = Button(window, text="Submit", 
                font=("Ink Free", 14), 
                bg="#4CAF50", fg="white", 
                padx=10, 
                pady=10) # creating a button with specific font and colors
Button.config(command=click) # setting the command to be executed when the button is clicked
Button.pack(pady=100) # adding the button to the window with some padding
Button.config(activebackground="#FF0000") # changing the background color of the button when it is active (clicked)
# Button.config(state=DISABLED) # disabling the button so it cannot be clicked
Label_4_Button = Label(window, text=count, font=("Monospace", 50), bg="#2d292d", fg="white") # creating a label to display the count of button clicks
Label_4_Button.pack() # adding the label to the window
'''

# for input
entry = Entry(window, width=30) # creating an entry widget for user input
entry.pack(pady=20) # adding the entry widget to the window with some padding
entry.config(font=("Ink Free", 50)) # changing the font of the entry widget
entry.config(bg="#978EC1", fg="white") # changing the background and foreground colors of the entry widget
# entry.insert(0, "Enter your text here") # inserting default text into the entry widget
# entry.config(state=DISABLED) # disabling the entry widget so it cannot be edited
entry.config(width=10) # just to display the number characters, not characters limit
# entry.config(show="*") # changing the entry widget to show asterisks instead of the actual characters (useful for password input)

# Buttons for the input
def submit_4_input():
    user_name = entry.get() # getting the text from the entry widget
    print(user_name) # printing the user input to the console
submit = Button(window, text="Submit",
                command=submit_4_input) # creating a button for submitting the input
submit.pack(side = RIGHT) # adding the submit button to the window with some padding

def delete_4_input():
    entry.delete(0, END) # deleting all text from the entry widget
delete = Button(window, text="CLear",
                command=delete_4_input) # creating a button for submitting the input
delete.pack(side = RIGHT) # adding the submit button to the window with some padding

def backspace_4_input():
    entry.delete(len(entry.get())-1, END) # deleting the last character from the entry widget
backspace = Button(window, text="Backspace",
                command=backspace_4_input) # creating a button for submitting the input
backspace.pack(side = RIGHT) # adding the submit button to the window with some padding



# For running the window
window.mainloop() # run the window, keeps it open until we close it



