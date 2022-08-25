from tkinter import *
from PIL import ImageTk, Image

# Start
root = Tk()
root.title("Image Viewer")

# root.geometry("300x300")
# root.maxsize(300, 300)
# root.minsize(300, 300)

# functions
def forward(image_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))
    status = Label(root, text=f"image {image_number} of {str(number_of_images)}", bd=1)
    if image_number == len(image_list):
        button_forward = Button(root, text=">>", state=DISABLED)

    button_forward.grid(row=1, column=2, columnspan=1)
    button_back.grid(row=1, column=0, columnspan=1)
    status.grid(row=3, column=1, columnspan=1, pady=10, sticky=W + E)
    my_label.grid(row=0, column=0, columnspan=3)


def back(image_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))
    status = Label(root, text=f"image {image_number} of {str(number_of_images)}", bd=1)
    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    button_forward.grid(row=1, column=2, columnspan=1)
    button_back.grid(row=1, column=0, columnspan=1)
    status.grid(row=3, column=1, columnspan=1, pady=10, sticky=W + E)
    my_label.grid(row=0, column=0, columnspan=3)


# Define images
my_img1 = ImageTk.PhotoImage(Image.open("images/1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/5.jpg"))
my_img6 = ImageTk.PhotoImage(Image.open("images/6.jpg"))
# Define Buttons
button_back = Button(root, text="<<", command=back, state=DISABLED)
button_forward = Button(root, text=">>", command=lambda: forward(2))
button_exit = Button(root, text="Exit", command=root.quit)
# Add images in List
image_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6]
# Define Label
number_of_images = len(image_list)
status = Label(root, text=f"image 1 of {str(number_of_images)}", bd=1)
my_label = Label(image=my_img1)
# Show on Screen
button_exit.grid(row=1, column=1, columnspan=1)
button_forward.grid(row=1, column=2, columnspan=1)
button_back.grid(row=1, column=0, columnspan=1)
my_label.grid(row=0, column=0, columnspan=3)
status.grid(row=3, column=1, columnspan=1, pady=10, sticky=W+E)

root.mainloop()
