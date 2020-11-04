import turtle
t = turtle.Turtle()

turtle.bgcolor('black')
turtle.screensize(500,500)
turtle.speed(0)
turtle.tracer(1,0)

turtle.color('white')


with open('stars.txt') as starcoords:
    for coords in starcoords:
        print(coords.split())
        x = coords.split()[0]
        y = coords.split()[1]
        z = coords.split()[2]
        brightness = coords.split()[4]
        print(brightness)
        t.up()
        t.goto(x,y)


turtle.exitonclick()
