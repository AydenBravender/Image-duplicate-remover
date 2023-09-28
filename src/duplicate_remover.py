import cv2
import os
from os import listdir
import tkinter as tk

photo_list = []

def duplicate_remover():
    image_Dir = img_Dir.get() # retrieves the variable from the tkinter GUI
    checkbox_value = checkbox_var.get() # retrieves the variable from the tkinter GUI
    if checkbox_value == 1: # If the checkbox has been clicked
        root.destroy() # closes the Tkinter GUI window
        try: 
            for images in os.listdir(image_Dir):
                if (images.endswith(".png") or images.endswith(".jpg") or images.endswith(".jpeg")): # skips over all other files like .txt files
                    img_path = os.path.join(image_Dir, images)
                    img = cv2.imread(img_path)
                    frame_resized = cv2.resize(img, (1, 1))
                    pixel_color = frame_resized[0, 0].tolist()
            
                    if pixel_color in photo_list:
                        print(f"Deleting {images}") # Optional argument, allows you to see what is getting deleted
                        os.remove(images) # Deletes the image
                    else:
                        photo_list.append(pixel_color) # Adds the pixel refrence to 'photo_list'
        except FileNotFoundError:
            print("Invalid file source, please try again")
    else:
        print("You need to agree to continue")
    
        
        

root = tk.Tk()

Header = root.title('Duplicate Remover')
my_canvas = tk.Canvas(root, bg="black", height=300, width=600)
my_canvas.pack()

# adding the labels for the tkinter window
label = tk.Label(root, text='Enter Directory of Images: ')
label.config(font=('helvetica', 14), fg='white', bg='black')
my_canvas.create_window(300, 100, window=label)


# creating input window
img_Dir = tk.Entry(root)
my_canvas.create_window(300, 150, height=30, width=400, window=img_Dir)

# creating checkbox
checkbox_var = tk.IntVar()  # Changed the name to 'checkbox_var'
checkbox = tk.Checkbutton(root, text="I take full responsibility for any files deleted by this program", variable=checkbox_var, onvalue=1, offvalue=0)
checkbox.pack()




# the resize button
button = tk.Button(
    root,
    text="Delete Duplicates",
    width=25,
    height=3,
    bg="black",
    fg="white",
    font=('helvetica', 10, 'bold'),
    command=duplicate_remover
    )

my_canvas.create_window(300, 250, height=40,width=150, window=button)

root.mainloop()





