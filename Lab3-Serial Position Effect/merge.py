import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

root2 = tk.Tk()
root2.title("Recall")

base = tk.Canvas(root2, width = 500, height = 500,bg='red')
base.pack()

c1 = IntVar()
c2 = IntVar()
c3 = IntVar()
c4 = IntVar()
c5 = IntVar()
c6 = IntVar()
c7 = IntVar()
c8 = IntVar()
c9 = IntVar()
c10 = IntVar()
c11 = IntVar()
c12 = IntVar()
c13 = IntVar()
c14 = IntVar()
c15 = IntVar()
c16 = IntVar()
c17 = IntVar()
c18 = IntVar()

def click_me():
    result = c2.get()+c4.get()+c5.get()+c7.get()+c9.get()+c11.get()+c12.get()+c14.get()+c15.get()+c17.get()
    total = c1.get()+c2.get()+c3.get()+c4.get()+c5.get()+c6.get()+c7.get()+c8.get()+c9.get()+c10.get()+c11.get()+c12.get()+c13.get()+c14.get()+c15.get()+c16.get()+c17.get()+c18.get()
    if(total==10):
        if (c1.get()==1):
            name1.config(fg='red')
        if (c2.get()==1):
            name2.config(fg='green')
        if (c3.get()==1):
            name3.config(fg='red')
        if (c4.get()==1):
            name4.config(fg='green')
        if (c5.get()==1):
            name5.config(fg='green')
        if (c6.get()==1):
            name6.config(fg='red')
        if (c7.get()==1):
            name7.config(fg='green')
        if (c8.get()==1):
            name8.config(fg='red')
        if (c9.get()==1):
            name9.config(fg='green')
        if (c10.get()==1):
            name10.config(fg='red')
        if (c11.get()==1):
            name11.config(fg='green')
        if (c12.get()==1):
            name12.config(fg='green')
        if (c13.get()==1):
            name13.config(fg='red')
        if (c14.get()==1):
            name14.config(fg='green')
        if (c15.get()==1):
            name15.config(fg='green')
        if (c16.get()==1):
            name16.config(fg='red')
        if (c17.get()==1):
            name17.config(fg='green')
        if (c18.get()==1):
            name18.config(fg='red')

        if(result==10):
            messagebox.showinfo("Score Card", "Your score : "+ str(result)+"\nAmazinggg!!!")
        elif(result>6):
            messagebox.showinfo("Score Card", "Your score : "+ str(result)+"\nAlmost there. Good going!!")
        elif(result>3):
            messagebox.showinfo("Score Card", "Your score : "+ str(result)+"\nKeep going!!")
        else:
            messagebox.showinfo("Score Card", "Your score : "+ str(result)+"\nTry again!!")
        root2.destroy()

    else:
        messagebox.showinfo("Score Card", "You have selected "+str(total)+" items.\nDo select 10 items")

foot = tk.Canvas(root2, width = 500, height = 5, bg='red')
foot.pack()

sep1 = ttk.Separator(root2, orient='horizontal')
sep1.pack(side='top', fill='x')

name1 = Checkbutton(root2, text="Rat", variable=c1)
name1.config(font=('georgia', 15),bg='red')
base.create_window(130, 50, window=name1)

name2 = Checkbutton(root2, text="Monkey", variable=c2)
name2.config(font=('georgia', 15),bg='red')
base.create_window(150, 100, window=name2)

name3 = Checkbutton(root2, text="Mongoose", variable=c3)
name3.config(font=('georgia', 15),bg='red')
base.create_window(160, 150, window=name3)

name4 = Checkbutton(root2, text="Crocodile", variable=c4)
name4.config(font=('georgia', 15),bg='red')
base.create_window(155, 200, window=name4)

name5 = Checkbutton(root2, text="Dog", variable=c5)
name5.config(font=('georgia', 15),bg='red')
base.create_window(129, 250, window=name5)

name6 = Checkbutton(root2, text="Deer", variable=c6)
name6.config(font=('georgia', 15),bg='red')
base.create_window(134, 300, window=name6)

name7 = Checkbutton(root2, text="Lion", variable=c7)
name7.config(font=('georgia', 15),bg='red')
base.create_window(133, 350, window=name7)

name8 = Checkbutton(root2, text="Jaguar", variable=c8)
name8.config(font=('georgia', 15),bg='red')
base.create_window(142, 400, window=name8)

name9 = Checkbutton(root2, text="Horse", variable=c9)
name9.config(font=('georgia', 15),bg='red')
base.create_window(139, 450, window=name9)

name10 = Checkbutton(root2, text="Fox", variable=c10)
name10.config(font=('georgia', 15),bg='red')
base.create_window(335, 50, window=name10)

name11 = Checkbutton(root2, text="Kangaroo", variable=c11)
name11.config(font=('georgia', 15),bg='red')
base.create_window(360, 100, window=name11)

name12 = Checkbutton(root2, text="Tiger", variable=c12)
name12.config(font=('georgia', 15),bg='red')
base.create_window(340, 150, window=name12)

name13 = Checkbutton(root2, text="Donkey", variable=c13)
name13.config(font=('georgia', 15),bg='red')
base.create_window(350, 200, window=name13)

name14 = Checkbutton(root2, text="Giraffe", variable=c14)
name14.config(font=('georgia', 15),bg='red')
base.create_window(347, 250, window=name14)

name15 = Checkbutton(root2, text="Elephant", variable=c15)
name15.config(font=('georgia', 15),bg='red')
base.create_window(355, 300, window=name15)

name16 = Checkbutton(root2, text="Wolf", variable=c16)
name16.config(font=('georgia', 15),bg='red')
base.create_window(338, 350, window=name16)

name17 = Checkbutton(root2, text="Rabbit", variable=c17)
name17.config(font=('georgia', 15),bg='red')
base.create_window(345, 400, window=name17)

name18 = Checkbutton(root2, text="Cat", variable=c18)
name18.config(font=('georgia', 15),bg='red')
base.create_window(330, 450, window=name18)

z = Button(root2, text="Click here", command=click_me)
z.config(font=('georgia', 15),fg='white smoke',bg='black')
z.pack(padx=15, pady=15)
root2.mainloop()