'''print("Hello", "Python", 100)
print("Hello", "Python", 100, sep='##')
print("Hello", "Python", 100, 3.14, sep='##', end=' ')
print("Hello")'''

# int
# float
# str
# bool

'''a = int(input("a = "))
b = int(input("b = "))
c = a + b
print(c)'''

'''from turtle import *
import random
shape("turtle")
pensize(1)
speed(50)
color("crimson")
choice = int(input("krug / kwadrat? (1/2)"))
for k in range(72):
    a = random.randint(50, 200)
    if choice == 1:
        circle(a)
    else:
        for i in range(4):
            forward(a)
            left(90)
    left(5)


input()'''


import random
from turtle import *

shape("turtle")
pensize(1)

choice = int(input("ви хочете квітку чи серце? 1/2 "))

if choice == 1:
    speed(2000)
    color("maroon")

    for i in range(4):
        for i in range(50):
            a = random.randint(25, 100)
            circle(a)
            right(90)

    penup()
    color("gold")
    pendown()

    for i in range(5):
        right(70)
        for i in range(15):
            a = random.randint(5, 25)
            circle(a)

else:
    def direction():
        for i in range(200):
            right(1)
            forward(1)

    color("crimson")

    begin_fill()

    left(140)
    forward(120)

    direction()

    left(120)

    direction()

    forward(120)

    end_fill()

input()


