import ctypes
import os
import tkinter as tk
from tkinter import filedialog, messagebox


def change_wallpaper(image_path):
    SPI_SETDESKWALLPAPER = 20
    SPIF_UPDATEINIFILE = 0x01
    SPIF_SENDWININICHANGE = 0x02

    try:
        result = ctypes.windll.user32.SystemParametersInfoW(
            SPI_SETDESKWALLPAPER,
            0,
            image_path,
            SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE
        )

        return result != 0

    except Exception as e:
        messagebox.showerror("Error", f"Error changing wallpaper:\n{e}")
        return False


def import_file():
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[
            ("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif"),
            ("All Files", "*.*")
        ]
    )

    if not file_path:
        return

    # Check the file extension
    valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif")

    if not file_path.lower().endswith(valid_extensions):
        messagebox.showerror(
            "Invalid File",
            "The selected file is not a supported image."
        )
        return

    # Convert to absolute path
    image_path = os.path.abspath(file_path)

    if change_wallpaper(image_path):
        messagebox.showinfo("Success", "Wallpaper changed successfully!")
    else:
        messagebox.showerror("Failed", "Failed to change wallpaper.")


# Create the main window
root = tk.Tk()
root.title("Wallpaper Changer")
root.geometry("300x150")
root.resizable(False, False)

label = tk.Label(root, text="Choose an image to set as wallpaper")
label.pack(pady=15)

import_button = tk.Button(
    root,
    text="Choose Image",
    command=import_file,
    width=20
)
import_button.pack(pady=10)

root.mainloop()
