import ctypes
import os


def change_wallpaper(C:\Users\Vagelis Petrogiannis\Desktop\Misty-morning-in-a-dense-forest-sunlight-breaking-through-the-fog-wallpaper-Full-HD-1920x1080-1):
           SPI_SETDESKWALLPAPER = 20
           SPIF_UPDATEINFILE = 0x02
           SPIF_SENDWININICHANGE =0x02

           try:
           
                ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path,
                                                   SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE)         

                return True
            except Exception as e:
                print(f"Error changing wallpaper: {e}")
                return False


if __name__ == "__main__"