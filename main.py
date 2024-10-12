import os
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image


def get_image_info(image_path):
    try:
        with Image.open(image_path) as img:
            image_info = {
                "File Name": os.path.basename(image_path),
                "Size (px)": f"{img.width} x {img.height}",
                "Resolution (dpi)": img.info.get('dpi', 'Unknown'),
                "Color Depth (mode)": img.mode,
                "Compression": img.info.get('compression', 'None')
            }
            return image_info
    except Exception as e:
        return {"Error": f"Failed to process {image_path}: {str(e)}"}


def choose_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_label.config(text=folder_path)
        process_images(folder_path)
    else:
        messagebox.showwarning("Warning", "Folder not selected!")


def process_images(folder_path):
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.tif', '.bmp', '.pcx')
    files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.lower().endswith(image_extensions)]

    if not files:
        messagebox.showinfo("Info", "No images found in the selected folder.")
        return

    text_area.config(state=NORMAL)
    text_area.delete(1.0, END)

    for file in files:
        info = get_image_info(file)

        for key, value in info.items():
            text_area.insert(END, f"{key}: {value}\n")
        text_area.insert(END, "-"*50 + "\n")

    text_area.config(state=DISABLED)


root = Tk()
root.title("Image Info Reader")
root.geometry("600x400")

label = Label(root, text="Select a folder containing images:")
label.pack(pady=10)

choose_button = Button(root, text="Choose Folder", command=choose_folder)
choose_button.pack()

folder_label = Label(root, text="No folder selected", fg="blue")
folder_label.pack(pady=5)

text_area = Text(root, height=15, width=70)
text_area.pack(pady=10)
text_area.config(state=DISABLED)

root.mainloop()
