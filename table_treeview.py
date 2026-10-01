import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("650x500")
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
        "message": "Select a product to view its details.",
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

products = [
    (1, "Keyboard", 29.99),
    (2, "Mouse", 15.99),
    (3, "Monitor", 149.99),
    (4, "Printer", 89.99),
    (5, "Speakers", 39.99),
    (6, "Webcam", 49.99),
]


def move_indicator():
    """Place the indicator below the active menu button."""
    button = buttons.get(active_page)
    if button is None:
        return

    indicator.place(
        x=button.winfo_x(),
        y=options_fm.winfo_height() - 4,
        width=button.winfo_width(),
        height=3,
    )


def refresh_row_colors(tree):
    """Alternate colors based on the current row order."""
    for index, item_id in enumerate(tree.get_children()):
        tag = "evenrow" if index % 2 == 0 else "oddrow"
        tree.item(item_id, tags=(tag,))


def create_products_tree(panel):
    """Create the Products table with alternating row colors."""
    table_frame = tk.Frame(panel, bg=pages["Products"]["color"])
    table_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=15)

    tree = ttk.Treeview(
        table_frame,
        columns=("id", "name", "price"),
        show="headings",
        selectmode="browse",
    )

    tree.heading("id", text="ID")
    tree.heading("name", text="Product Name")
    tree.heading("price", text="Price")

    tree.column("id", width=60, minwidth=50, anchor=tk.CENTER)
    tree.column("name", width=280, minwidth=150, anchor=tk.W)
    tree.column("price", width=100, minwidth=80, anchor=tk.E)

    scrollbar = ttk.Scrollbar(
        table_frame,
        orient=tk.VERTICAL,
        command=tree.yview,
    )
    tree.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    tree.tag_configure(
        "evenrow",
        background="#d6eaf8",
        foreground="black",
    )
    tree.tag_configure(
        "oddrow",
        background="#ffffff",
        foreground="black",
    )

    for product_id, name, price in products:
        tree.insert(
            "",
            tk.END,
            values=(product_id, name, f"${price:.2f}"),
        )

    refresh_row_colors(tree)

    selected_text = tk.StringVar(value="No product selected.")

    tk.Label(
        panel,
        textvariable=selected_text,
        font=("Arial", 11),
        bg=pages["Products"]["color"],
        fg="#222222",
    ).pack(padx=20, pady=(0, 15))

    def show_selected_product(event):
        selection = tree.selection()
        if selection:
            product_id, name, price = tree.item(
                selection[0], "values"
            )
            selected_text.set(f"Selected: {name} — {price}")

    tree.bind("<<TreeviewSelect>>", show_selected_product)


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
    ).pack(pady=(25, 10))

    tk.Label(
        panel,
        text=page["message"],
        font=("Arial", 12),
        bg=color,
        fg="#222222",
        wraplength=500,
    ).pack(padx=20, pady=10)

    if page_name == "Products":
        create_products_tree(panel)

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

options_fm.bind("<Configure>", lambda event: move_indicator())

show_panel("Home")

root.mainloop()