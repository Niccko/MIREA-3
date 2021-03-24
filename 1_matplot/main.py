import matplotlib.pyplot as plt
from random import random, randint
import time
from pprint import pprint as pp
from math import sqrt
 

def create_field():
    field = [[0 for x in range(height)] for y in range(width)]
    for i in range(int(population*ratio)):
        x,y = get_free_cell(field)
        field[x][y] = 1
    for i in range(int(population*(1-ratio))):
        x,y = get_free_cell(field)
        field[x][y] = 2
    return field


def is_happy(field,x,y):
    total = 0
    good = 0
    agent = field[x][y]
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if i == x and j == y:
                continue
            if i >= 0 and i < width and j >= 0 and j < height:
                if field[i][j] == agent:
                    good+=1
                total+=1
    if good/total>tolerance:
        return True
    return False

def get_free_cell(field):
    while True:
        x = randint(0,width-1)
        y = randint(0,height-1)
        if field[x][y] == 0:
            return x, y
    return None

def iterate(field):
    happy = 0
    for x in range(width):
        for y in range(height):
            if not is_happy(field,x,y):
                nx, ny = get_free_cell(field)
                field[x][y], field[nx][ny] = field[nx][ny], field[x][y]
            else:
                happy+=1
    return happy

def calculate_mean(field):
    total1 = 0
    total2 = 0
    mag1  = 0
    mag2  = 0
    for x in range(width):
        for y in range(height):
            if field[x][y] == 1:
                total1+=1
                mag1+=x+y
            if field[x][y] == 2:
                total2+=1
                mag2+=x+y
    return mag1/total1, mag2/total2

###############################################################

#Input parameters
# width = int(input("Ширина: "))
# height = int(input("Высота: "))
# population = int(input("Популяция (< "+str(width*height)+"):"))
# ratio = float(input("Соотношение (< 1): "))
# tolerance = float(input("Толерантность (< 1): "))
# iteration_count = int(input("Количество итераций: "))

width = 100
height = 100
population = 5000
ratio = 0.5
tolerance = 0.4
iteration_count = 10000

plt.figure(figsize=(18, 5))
ax1 = plt.subplot(131)
ax2 = plt.subplot(132)
ax3 = plt.subplot(133)

ax1.set_xlabel("Main field")
ax2.set_xlabel("Average position")
ax3.set_xlabel("Happiness")

field = create_field()


x = []
y1 = []
y2 = []
y1_2 = []
grid = ax1.imshow([[x for x in y] for y in field])

grid_figure = plt.figure(1)
plt.show(block=False)

for i in range(iteration_count):
    happy = iterate(field)
    grid.set_data([[x for x in y] for y in field])

    #Update graphs
    x.append(i)
    ny1, ny2 = calculate_mean(field)
    y1.append(ny1)
    y1_2.append(ny2)
    y2.append(happy)
    
    graph1 = ax2.plot(x,y1, color = '#00FF00')
    graph1_2 = ax2.plot(x,y1_2, color = '#FFFF00')
    graph2 = ax3.plot(x,y2,color = '#FF00FF')


    grid_figure.canvas.draw()
    grid_figure.canvas.flush_events()
    time.sleep(0.001)
    #pp(field)
    #print('\n')

plt.show()

