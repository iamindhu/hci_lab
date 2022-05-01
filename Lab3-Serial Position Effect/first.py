import tkinter as tk
from tkinter import *

first = tk.Tk()
first.title("Serial Position Effect")

base = tk.Canvas(first,bg='red', width = 800, height = 400)
base.pack()

head = tk.Label(first, text='Instructions')
head.config(font=('Times', 30),bg='red')
base.create_window(400, 70, window=head)

in1 = tk.Label(first, text='1.When you click the get started button, a window with a list of ten animals appears.')
in1.config(font=('Times', 15),bg='red')
base.create_window(400, 150, window=in1)

in2 = tk.Label(first, text='2. It only displays for 10 seconds. Make an effort to remember the creatures on the list.')
in2.config(font=('Times', 15),bg='red')
base.create_window(374, 200, window=in2)

in3 = tk.Label(first, text='3. Following the conclusion of 10 seconds, another window with 18 creatures appears.')
in3.config(font=('Times', 15),bg='red')


base.create_window(393, 250, window=in3)

in4 = tk.Label(first, text='4. Choose all the the previously memorised animals and press the button below.')
in4.config(font=('Times', 15),bg='red')
base.create_window(340, 300, window=in4)

def click_me():
    first.destroy()
    import main

z = Button(first, text="Get Started", command=click_me)
z.config(font=('georgia', 15),fg='black',bg='white')
z.pack(padx=15, pady=15)
first.mainloop()