import random
import pygame.gfxdraw
import time
import math
import csv
import matplotlib.pyplot as plt
import pandas as pd

pygame.init()
scr = pygame.display.set_mode((1500, 800))
pygame.display.set_caption('Fitts\' Law')

# Open csv file
outfile = open("fitts_law.csv", 'w',newline='')
outfile_field = ['SNo', 'Radius', 'Distance','ID', 'Time']
writer = csv.DictWriter(outfile, fieldnames=outfile_field)
writer.writeheader()

colors = [(255,0,0),(0,255,0),(0,0,255),(128,128,0),(0,128,128),(128,0,128),(12,200,58),(184,6,83),(14,153,206),(200,200,200)]
count = 0
startingTime = 0
analysis = []

circle_radius = random.randint(20,50)
x_centre = random.randint(50,1450)
y_centre = random.randint(100,750)
color = colors[random.randint(0,9)]

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Click the Circle', True, (0,0,0))
textRect = text.get_rect()
textRect.center = (750, 50)


while count<40:
    pygame.display.update()
    scr.fill((255, 255, 255))
    scr.blit(text, textRect)
    pygame.gfxdraw.filled_circle(scr, x_centre , y_centre , circle_radius, color)

    # Mouse Click Event
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = scr.get_at(pygame.mouse.get_pos()) == color
            if click == 1:
                old_x = x_centre
                old_y = y_centre
                x_centre = random.randint(50, 1450)
                y_centre = random.randint(100, 750)
                distance = round(math.sqrt((old_x-x_centre)**2+(old_y-y_centre)**2),2)
                time_elapsed = round(time.time() - startingTime,2)
                analysis.append([str(count)+" "+str(circle_radius)+" "+str(distance)+" "+str(time_elapsed)])
                if count!=0:
                    writer.writerow({'SNo': str(count), 'Radius': str(circle_radius), 'Distance': str(distance),
                                 'ID': str(math.log2(distance / circle_radius + 1)),'Time': str(time_elapsed)})
                count += 1
                color = colors[random.randint(0, 9)]
                circle_radius = random.randint(20, 50)
                font = pygame.font.Font('freesansbold.ttf', 32)
                text = font.render('Click the Circle', True, (0, 0, 0))
                textRect = text.get_rect()
                textRect.center = (750, 50)
                startingTime = time.time()

outfile.close()
pygame.quit()

# Displaying graph
import numpy as np
df = pd.read_csv('fitts_law.csv')
print(df)

plt.figure(figsize=(20,8))
plt.title('Fitts Law Demo')
x = df['ID']
y = df['Time']
plt.scatter(x,y)
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b)
plt.xlabel('Index of Difficulty')
plt.ylabel('Time')
plt.show()

# Displaying table
from tkinter import *
import tkinter.ttk as ttk
import csv

root = Tk()
root.title("Fitts Law Demo Table")
width = 500
height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

TableMargin = Frame(root, width=500)
TableMargin.pack(side=TOP)
tree = ttk.Treeview(TableMargin, columns=("Radius", "Distance", "Time"), height=400, selectmode="extended")
tree.heading('Radius', text="Radius", anchor=W)
tree.heading('Distance', text="Distance", anchor=W)
tree.heading('Time', text="Time", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=200)
tree.column('#2', stretch=NO, minwidth=0, width=200)
tree.column('#3', stretch=NO, minwidth=0, width=300)
tree.pack()

with open('fitts_law.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        radius = row['Radius']
        dist = row['Distance']
        times = row['Time']
        tree.insert("", 0, values=(radius, dist, times))

if __name__ == '__main__':
    root.mainloop()

sys.exit()