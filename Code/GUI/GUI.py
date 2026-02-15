from tkinter import * 


# This code creates a simple GUI window using the Tkinter library in Python. It sets up the window's size, title, and background color, and adds a label with an image and a button that prints a message when clicked.
window = Tk() # instantiate an instance of a window
window.geometry ("1080x720") # changing the size of the window
window.title("Cancer Pharmacogenomics Dashboard") # changing the title of the window


# icon settings
icon = PhotoImage(file=r"C:\Users\allan\Desktop\TU\Spring 2026\Projects of Data Science\Project\Helix.png") 
window.iconphoto(True, icon)
# window.config(background="grey") # changing the background color of the window
window.config(background="#2d292d") # changing the background color of the window using hex code



# Label settings
photo_Label = PhotoImage(file=r"C:\Users\allan\Desktop\TU\Spring 2026\Projects of Data Science\Project\Helix.png") # loading an image from a file
photo_Label = photo_Label.subsample(10, 10) # resizing the image to fit the label
Titlelabel = Label(window, text="Welcome to the Cancer Pharmacogenomics Dashboard!", font=("Arial", 16), bg="#2d292d", fg="white", image=photo_Label, compound='left') # creating a label with specific font and colors
# Titlelabel = Label(window, text="Welcome to the Cancer Pharmacogenomics Dashboard!", font=("Arial", 16), bg="#2d292d", fg="white") # creating a label with specific font and colors
Titlelabel.pack(pady=20) # adding the label to the window with some padding



# Button settings
def click():  # giving the button a function to execute when clicked
    print("Button clicked!")

Button = Button(window, text="Click Me!", font=("Arial", 14), bg="#4CAF50", fg="white", padx=10, pady=5) # creating a button with specific font and colors
Button.config(command=click) # setting the command to be executed when the button is clicked
Button.pack(pady=10) # adding the button to the window with some padding

window.mainloop() # run the window, keeps it open until we close it



