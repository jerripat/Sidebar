import tkinter as tk
from pathlib import Path

root = tk.Tk()
root.geometry("400x600")
root.title("My Tkinter App")

MENU_COLOR = "#383838"
menu_expanded = False

image_path = Path(__file__).resolve().parent / "images" / "menu-icon.png"
toggle_icon = tk.PhotoImage(file=str(image_path))
home_icon = tk.PhotoImage(file=str(Path(__file__).resolve().parent / "images" / "home-icon.png"))
menu_bar_frame = tk.Frame(root, bg=MENU_COLOR, width=45)
menu_bar_frame.pack(side=tk.LEFT, fill=tk.Y, padx=3, pady=4)
menu_bar_frame.pack_propagate(False)


def toggle_menu():
    global menu_expanded

    menu_expanded = not menu_expanded

    if menu_expanded:
        menu_bar_frame.config(width=150)
        menu_options.pack(fill=tk.X, pady=10)
    else:
        menu_options.pack_forget()
        menu_bar_frame.config(width=45)


toggle_menu_btn = tk.Button(
    menu_bar_frame,
    image=toggle_icon,
    command=toggle_menu,
    bg=MENU_COLOR,
    activebackground=MENU_COLOR,
    bd=0,
    cursor="hand2",
)
toggle_menu_btn.pack(anchor="nw", padx=4, pady=10)

menu_options = tk.Frame(menu_bar_frame, bg=MENU_COLOR)

for name in ("Home", "Settings", "About"):
    button = tk.Button(
        menu_options,
        text=name,
        command=lambda selected=name: content_label.config(text=selected),
        bg=MENU_COLOR,
        fg="white",
        activebackground="#505050",
        activeforeground="white",
        bd=0,
        anchor="w",
        cursor="hand2",
    )
    button.pack(fill=tk.X, padx=8, pady=5)

content_frame = tk.Frame(root)
content_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

content_label = tk.Label(
    content_frame,
    text="Home",
    font=("Arial", 20),
)
content_label.pack(pady=30)

if __name__ == "__main__":
    root.mainloop()