import tkinter as tk
from PIL import Image, ImageTk
import os

def create_splash():
    root = tk.Tk()
    root.overrideredirect(True)
    image_path = os.path.join(os.path.dirname(__file__), "Joe.png")
    try:
        img = Image.open(image_path)
        photo = ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Error: {e}")
        root.destroy()
        return
    label = tk.Label(root, image=photo, bg='black')
    label.pack()
    root.update_idletasks()
    width = img.width
    height = img.height
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    root.deiconify()
    root.attributes("-topmost", True)
    root.after(5000, root.destroy)
    
    root.mainloop()

if __name__ == "__main__":
    create_splash()
