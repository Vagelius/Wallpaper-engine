import ctypes
import os
import tkinter as tk
from tkinter import filedialog, messagebox

SPI_SETDESKWALLPAPER = 20
SPIF_UPDATEINIFILE = 0x01
SPIF_SENDWININICHANGE = 0x02


def change_wallpaper(image_path):
    try:
        return ctypes.windll.user32.SystemParametersInfoW(
            SPI_SETDESKWALLPAPER,
            0,
            image_path,
            SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE,
        )
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return False


def choose_image():
    file_path = filedialog.askopenfilename(
        title="Choose Wallpaper",
        filetypes=[
            ("Image Files", "*.jpg *.jpeg *.png *.bmp"),
            ("All Files", "*.*")
        ]
    )

    if not file_path:
        return

    valid = (".jpg", ".jpeg", ".png", ".bmp")

    if not file_path.lower().endswith(valid):
        messagebox.showerror("Invalid File", "Please select an image.")
        return

    if change_wallpaper(os.path.abspath(file_path)):
        messagebox.showinfo("Success", "Wallpaper changed!")
    else:
        messagebox.showerror("Error", "Failed to change wallpaper.")


def remove_wallpaper():
    # May not work on all versions of Windows.
    if change_wallpaper(""):
        messagebox.showinfo("Success", "Wallpaper removed.")
    else:
        messagebox.showwarning(
            "Not Supported",
            "Your version of Windows does not support removing the wallpaper this way."
        )


fullscreen = False


def toggle_fullscreen():
    global fullscreen
    fullscreen = not fullscreen
    root.attributes("-fullscreen", fullscreen)


def exit_fullscreen(event=None):
    global fullscreen
    fullscreen = False
    root.attributes("-fullscreen", False)


root = tk.Tk()
root.title("Wallpaper Changer")
root.geometry("400x250")

tk.Label(
    root,
    text="Wallpaper Changer",
    font=("Segoe UI", 16, "bold")
).pack(pady=15)

tk.Button(
    root,
    text="Choose Wallpaper",
    width=25,
    command=choose_image
).pack(pady=5)

tk.Button(
    root,
    text="Remove Wallpaper",
    width=25,
    command=remove_wallpaper
).pack(pady=5)

tk.Button(
    root,
    text="Toggle Fullscreen",
    width=25,
    command=toggle_fullscreen
).pack(pady=5)

tk.Button(
    root,
    text="Exit",
    width=25,
    command=root.destroy
).pack(pady=5)

# Press Esc to leave fullscreen
root.bind("<Escape>", exit_fullscreen)

root.mainloop()
