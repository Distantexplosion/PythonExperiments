import math
from turtle import Turtle
from random import random

t = Turtle()
t.radians()
pi = math.pi

t.pensize(2)
t.pencolor("blue")
t.teleport(100,100)
t.left(pi / 2)
t.circle(10, 2 * pi)
t.fd(100)
t.begin_fill()
t.circle(-10, pi)
t.end_fill()
t.fd(100)
t.circle(10, 2 * pi)



t.screen.mainloop()