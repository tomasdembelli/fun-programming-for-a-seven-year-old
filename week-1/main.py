import turtle

t = turtle.Turtle()

for i in range(20):
    t.forward(100)  # move forward 100 steps
    t.forward(10)
    t.right(90)  # turn right 90 degrees
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.forward(10)
    t.right(90) #This is to leave the turtle facing right


# triangle
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)

turtle.done()