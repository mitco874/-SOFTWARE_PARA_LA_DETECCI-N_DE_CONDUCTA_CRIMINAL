from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("465x600")
window.configure(bg = "#f1e8e8")
canvas = Canvas(
    window,
    bg = "#f1e8e8",
    height = 600,
    width = 465,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = -478, y = -129,
    width = 127,
    height = 33)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = -478, y = 93,
    width = 127,
    height = 33)

window.resizable(False, False)
window.mainloop()
