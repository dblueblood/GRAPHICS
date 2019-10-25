"""
Author: Ayo Asekun
Date Created: Oct 19th, 2019
Last Date Modified: Oct 19th, 2019
Program Description: Using Turtle to draw a 7 row 5-dotted line
"""

import turtle

t = turtle
x = 5
y = 7
w = 30
for i in range(y):
    for i in range(x):
        t.down()
        t.dot()
        t.up()
        t.forward(w)
    t.up()
    t.backward(x*w)
    t.right(90)
    t.forward(30)
    t.left(90)
    t.down()

t.done()

