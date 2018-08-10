# By Dominic Eggerman

def btnClicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text=res)

if __name__ == "__main__":

    # Imports
    from tkinter import *


    window = Tk()
    window.title("GUI interface")
    window.geometry("600x400")

    lbl = Label(window, text="Hello", font=("Arial Bold", 40))
    lbl.grid(column=0, row=0)

    txt = Entry(window, width=10)
    txt.grid(column=1, row=0)

    btn = Button(window, text="button", bg="green", fg="blue", command=btnClicked)
    btn.grid(column=2, row=0)

    # Run window
    window.mainloop()