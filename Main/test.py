import tkinter as tk

root = tk.Tk()
child = tk.Toplevel(root)
child.title('child')

# def close_both():
#     child.destroy()
#     root.destroy()

# child.protocol("WM_DELETE_WINDOW", close_both)

for child in root.winfo_children():
    print(child)
    if str(child) == '.!toplevel':
        print(1)
    else:
        print(0)

root.mainloop()