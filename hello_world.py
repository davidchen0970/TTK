"""
Author: Akuli
Source: https://github.com/Akuli/tkinter-tutorial/blob/master/getting-started.md
"""

import tkinter
from tkinter import ttk

root = tkinter.Tk()
root.geometry("400x200")  # 設定視窗大小為 800x600

# Pack a big frame so, it behaves like the window background
big_frame = ttk.Frame(root)
big_frame.pack(fill="both", expand=True)

label = tkinter.Label(root, text="Hello World!", font=("-size", 15, "-weight", "bold"))
label.place(relx=0.5, rely=0.5, anchor='center')  # 將文字標籤放在視窗的中央

# Set the initial theme
root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "dark")

root.mainloop()
