import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title("My Tkinter App")

MENU_COLOR = "#383838"

options_fm = tk.Frame(root, bg=MENU_COLOR, height=40)
options_fm.pack(fill=tk.X, padx=5, pady=5)
options_fm.pack_propagate(False)

main_fm = tk.Frame(root, bg="white", bd=1, relief=tk.SUNKEN)
main_fm.pack(fill=tk.BOTH, expand=True, padx=5, pady=(0, 5))

indicator = tk.Label(options_fm, bg="#00bfff")
buttons = {}
active_page = "Home"

pages = {
    "Home": {
        "color": "#d6eaf8",
        "message": "Welcome! Select an option from the menu above.",
    },
    "About": {
        "color": "#d5f5e3",
        "message": "This application was created with Python and Tkinter.",
    },
    "Products": {
        "color": "#fcf3cf",
        "message": "Browse your products here.",
    },
    "Contact": {
        "color": "#fadbd8",
        "message": "Your contact information goes here.",
    },
    "Settings": {
        "color": "#e8daef",
        "message": "Manage your application settings here.",
    },
}


def move_indicator():
    """Place the indicator below the active menu button."""
    button = buttons[active_page]
    indicator.place(
        x=button.winfo_x(),
        y=options_fm.winfo_height() - 4,
        width=button.winfo_width(),
        height=3,
    )


def show_panel(page_name):
    """Replace the current panel with the selected page."""
    global active_page
    active_page = page_name

    for widget in main_fm.winfo_children():
        widget.destroy()

    page = pages[page_name]
    color = page["color"]

    panel = tk.Frame(main_fm, bg=color)
    panel.pack(fill=tk.BOTH, expand=True)

    tk.Label(
        panel,
        text=page_name,
        font=("Arial", 24, "bold"),
        bg=color,
        fg="#222222",
    ).pack(pady=(40, 20))

    tk.Label(
        panel,
        text=page["message"],
        font=("Arial", 12),
        bg=color,
        fg="#222222",
        wraplength=400,
    ).pack(padx=20, pady=10)

    root.after_idle(move_indicator)


def create_menu_button(text, command):
    button = tk.Button(
        options_fm,
        text=text,
        command=command,
        bg=MENU_COLOR,
        fg="white",
        activebackground="#555555",
        activeforeground="white",
        bd=0,
        cursor="hand2",
        padx=8,
        pady=5,
    )
    button.pack(side=tk.LEFT, padx=3)
    return button


for page_name in pages:
    buttons[page_name] = create_menu_button(
        page_name,
        lambda name=page_name: show_panel(name),
    )

exit_btn = create_menu_button("Exit", root.destroy)

# Reposition the indicator when the menu changes size.
options_fm.bind("<Configure>", lambda event: move_indicator())

show_panel("Home")

root.mainloop()