from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("690x381")
window.configure(bg = "#141212")
canvas = Canvas(
    window,
    bg = "#141212",
    height = 381,
    width = 690,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    346.0, 192.5,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 55, y = 52,
    width = 161,
    height = 184)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 241, y = 52,
    width = 161,
    height = 184)

canvas.create_text(
    126.5, 107.5,
    text = "Nombre:\n\n \nMarca: \n\n",
    fill = "#ffffff",
    font = ("Inder-Regular", int(13.0)))

window.resizable(False, False)
window.mainloop()
