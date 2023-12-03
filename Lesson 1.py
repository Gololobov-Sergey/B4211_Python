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

from turtle import *
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


input()