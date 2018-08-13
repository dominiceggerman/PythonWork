# By Dominic Eggerman

def btnClicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text=res)

if __name__ == "__main__":

    # Imports
    import tkinter as tk

    # Build window
    window = tk.Tk()
    window.title("GUI interface")
    window.geometry("600x400")

    lbl = tk.Label(window, text="Hello", font=("Arial Bold", 40))
    lbl.grid(column=0, row=0)

    txt = tk.Entry(window, width=10)
    txt.grid(column=1, row=0)

    btn = tk.Button(window, text="button", bg="green", fg="blue", command=btnClicked)
    btn.grid(column=2, row=0)

    # Run window
    window.mainloop()