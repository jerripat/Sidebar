import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title("My Tkinter App")

options_fm = tk.Frame(root, bg="#383838", width=75)
options_fm.pack(side=tk.LEFT, fill=tk.Y, padx=3, pady=4)

def open_window():
    new_window = tk.Toplevel(root)
    new_window.geometry("400x300")
    new_window.title("New Window")
    label = tk.Label(new_window, text="This is a new window")
    label.pack(pady=20)
    label.focus()

btnMainMenu = tk.Button(
    options_fm,
    text="Main Menu",

    bg="#383838",
    fg="white",
    activebackground="#505050",
    activeforeground="white",
    bd=0,
    anchor="w",
    cursor="hand2")
btnMainMenu.pack(fill=tk.X, pady=2)
btnMainMenu1 = tk.Button(
    options_fm,
    text="Customer Menu",

    bg="#383838",
    fg="white",
    activebackground="#505050",
    activeforeground="white",
    bd=0,
    anchor="w",
    cursor="hand2",
    command=open_window)

btnMainMenu1.pack(fill=tk.X, pady=2)


if __name__ == "__main__":
    root.mainloop()