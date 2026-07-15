import ctypes
import os


def change_wallpaper(image_path):
    SPI_SETDESKWALLPAPER = 20

    SPIF_UPDATEINIFILE = 0x01
    SPIF_SENDWININICHANGE = 0x02

    try:
        result = ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER,0,image_path,SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE,)

        
        return result != 0

    except Exception as e:
        print(f"Error changing wallpaper: {e}")
        return False


if __name__ == "__main__":

    
    image_path = os.path.abspath(
        r"C:\Users\Vagelis Petrogiannis\Desktop\Misty-morning-in-a-dense-forest-sunlight-breaking-through-the-fog-wallpaper-Full-HD-1920x1080-1.jpg"
    )

    if change_wallpaper(image_path):
        print("Wallpaper changed successfully")
    else:
        print("Failed to change wallpaper")