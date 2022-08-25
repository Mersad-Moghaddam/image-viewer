from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")
root.geometry("300x300")
root.maxsize(300, 300)
root.minsize(300, 300)

def forward(image_number):
    global my_label
    global button_forward
    global button_back
    button_forward.destroy()
    button_back.destroy()
    my_label.destroy()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))
    if image_number == len(image_list) :
        button_forward = Button(root, text=">>", state=DISABLED)

    button_forward.pack()
    button_back.pack()
    my_label.pack()


def back(image_number):
    global my_label
    global button_forward
    global button_back
    button_forward.destroy()
    button_back.destroy()
    my_label.destroy()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))
    if image_number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    button_forward.pack()
    button_back.pack()
    my_label.pack()


my_img1 = ImageTk.PhotoImage(Image.open("images/1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/5.jpg"))
my_img6 = ImageTk.PhotoImage(Image.open("images/6.jpg"))
button_back = Button(root, text="<<", command=back, state=DISABLED)
button_forward = Button(root, text=">>", command=lambda: forward(2))
button_exit = Button(root, text="Exit", command=root.quit)

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6]

my_label = Label(image=my_img1)

button_exit.pack()
button_forward.pack()
button_back.pack()
my_label.pack()

root.mainloop()
