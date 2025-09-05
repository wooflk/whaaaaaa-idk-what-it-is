import tkinter as tk
import os

file = "note.txt"

def new_file():
    text.delete("1.0", "end")

def open_file():
    if os.path.exists(file):
        with open(file, "r", encoding="utf-8") as f:
            text.delete("1.0", "end")
            text.insert("1.0", f.read())

def save_file():
    with open(file, "w", encoding="utf-8") as f:
        f.write(text.get("1.0", "end-1c"))

root = tk.Tk()
root.title("блокнот")
root.geometry("600x400")

btn_frame = tk.Frame(root)
btn_frame.pack(side="top", fill="x")

tk.Button(btn_frame, text="новый", command=new_file).pack(side="left")
tk.Button(btn_frame, text="открыть", command=open_file).pack(side="left")
tk.Button(btn_frame, text="сохранить", command=save_file).pack(side="left")

text = tk.Text(root, wrap="word")
text.pack(fill="both", expand=True)

root.mainloop()
