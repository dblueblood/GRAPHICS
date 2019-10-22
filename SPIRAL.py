import turtle
t = turtle
t.speed(20)
t.pencolor("blue")

for i in range(200):
    t.goto(0, 0)
    t.width(2)
    t.forward(200)
    t.right(70)
    t.forward(50)
    t.right(123)
for i in range(100):
    t.pencolor("red")
    t.width(2)
    t.goto(0, 0)
    t.forward(150)
    t.left(123)
    t.forward(50)
for i in range(50):
    t.pencolor("black")
    t.width(2)
    t.goto(0, 0)
    t.forward(80)
    t.right(123)
    t.forward(30)

t.done()



