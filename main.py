import turtle

window = turtle.Screen()
window.title("Ping-Pong")
window.setup(width = 1.0, height = 1.0)
window.bgcolor("black")

border = turtle.Turtle()
border.speed(0)
border.color("green")
border.begin_fill()
border.goto(-500, 300)
border.goto(500, 300)
border.goto(500, -300)
border.goto(-500, -300)
border.goto(-500, 300)
border.end_fill()

border.goto(0, 300)
border.color("white")
border.setheading(270)
for i in range(25):
    if i % 2 == 0:
        border.forward(24)
    else:
        border.up()
        border.forward(24)
        border.down()

border.hideturtle()


rocket_a = turtle.Turtle()
rocket_a.color("white")
rocket_a.shape("square")
rocket_a.shapesize(stretch_len=1, stretch_wid=5)
rocket_a.penup()
rocket_a.goto(-450,0)


def move_up():
    y = rocket_a.ycor()
    rocket_a.sety(y + 5)


def move_down():
    y = rocket_a.ycor()
    rocket_a.sety(y - 5)


window.listen()
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")

window.mainloop()