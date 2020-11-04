import turtle
t = turtle.Turtle()

turtle.bgcolor('black')
turtle.screensize(500,500)
turtle.speed(0)
turtle.tracer(1,0)

t.color('white')

def square(magnitude):
    size = round(10/(magnitude + 2))
    t.begin_fill()
    t.pendown()
    t.fd(size)
    t.right(90)
    t.fd(size)
    t.right(90)
    t.fd(size)
    t.right(90)
    t.fd(size)
    t.end_fill()

with open('stars.txt') as starcoords:
    for coords in starcoords:
        print(coords.split())
        x = float(coords.split()[0]) * 250
        y = float(coords.split()[1]) * 250
        z = coords.split()[2]
        brightness = float(coords.split()[4])
        print(brightness)
        t.penup()
        t.goto(x, y)
        square(brightness)


turtle.exitonclick()
