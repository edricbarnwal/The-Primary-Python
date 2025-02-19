import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    text_area.delete(1.0, tk.END)
    root.title("Untitled - Notepad")

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, content)
        root.title(f"{file_path} - Notepad")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))
        root.title(f"{file_path} - Notepad")
    
def exit_app():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()

def cut_text():
    text_area.event_generate("<<Cut>>")

def copy_text():
    text_area.event_generate("<<Copy>>")

def paste_text():
    text_area.event_generate("<<Paste>>")

root = tk.Tk()
root.title("Untitled - Notepad")
root.geometry("800x600")

text_area = tk.Text(root, font=("Arial", 12), undo=True)
text_area.pack(expand=True, fill=tk.BOTH)

menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

root.config(menu=menu_bar)
root.protocol("WM_DELETE_WINDOW", exit_app)

root.mainloop()
