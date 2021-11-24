import tkinter as tk

# pythonでGUIを作る例 実務では使うことなさそう
root = tk.Tk()
root.title('初めてのtkinter')
input_box = tk.Entry(root)
input_box.pack()
root.mainloop()
