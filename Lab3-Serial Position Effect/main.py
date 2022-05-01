import tkinter as tk
from tkinter import ttk

def countdown(time):
    if time == -1:
        root.destroy()
        import merge as module
    else:
        if time == 0:
            label.configure(text="Time up!!",font=('georgia', 15),fg='red')
        elif (time == 1) or (time == 2) or (time == 3):
            label.configure(text="Time remaining: %d seconds" % time, font=('georgia', 15),fg='red')
        else:
            label.configure(text="Time remaining: %d seconds" % time,font=('georgia', 15))

        root.after(1000, countdown, time-1)

root = tk.Tk()
root.title("Assignment")

base = tk.Canvas(root, width = 400, height = 540,bg='red')
base.pack()

foot = tk.Canvas(root, width = 400, height = 5, bg='red')
foot.pack()

sep1 = ttk.Separator(root, orient='horizontal')
sep1.pack(side='top', fill='x')

name1 = tk.Label(root, text='Tiger')
name1.config(font=('Times', 18),bg='red')
base.create_window(200, 50, window=name1)

name2 = tk.Label(root, text='Kangaroo')
name2.config(font=('Times', 18),bg='red')
base.create_window(200, 100, window=name2)

name3 = tk.Label(root, text='Elephant')
name3.config(font=('Times', 18),bg='red')
base.create_window(200, 150, window=name3)

name4 = tk.Label(root, text='Lion')
name4.config(font=('Times', 18),bg='red')
base.create_window(200, 200, window=name4)

name5 = tk.Label(root, text='Dog')
name5.config(font=('Times', 18),bg='red')
base.create_window(200, 250, window=name5)

name6 = tk.Label(root, text='Crocodile',bg='red')
name6.config(font=('Times', 18))
base.create_window(200, 300, window=name6)

name7 = tk.Label(root, text='Rabbit')
name7.config(font=('Times', 18),bg='red')
base.create_window(200, 350, window=name7)

name8 = tk.Label(root, text='Monkey')
name8.config(font=('Times', 18),bg='red')
base.create_window(200, 400, window=name8)

name9 = tk.Label(root, text='Giraffe')
name9.config(font=('Times', 18),bg='red')
base.create_window(200, 450, window=name9)

name10 = tk.Label(root, text='Horse')
name10.config(font=('Times', 18),bg='red')
base.create_window(200, 500, window=name10)

label = tk.Label(root,fg='red')
label.pack(padx=10,pady=10)
countdown(10)
root.mainloop()