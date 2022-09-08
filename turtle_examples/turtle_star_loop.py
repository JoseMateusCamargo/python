import turtle

colors = ['yellow', 'red', 'blue', 'green', 'magenta', 'cyan', 'orange']

# Documentation: https://docs.python.org/3/library/turtle.html
t = turtle.Turtle()
t.begin_fill()

screen = turtle.Screen()
screen.bgcolor('white')
t.speed(30)

for i in range(120):
    t.color(colors[i % 6])
    t.forward(i * 4)
    t.left(150)
    t.width(2)

t.end_fill()
turtle.exitonclick()
