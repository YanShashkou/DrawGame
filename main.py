import turtle

timmy = turtle.Turtle()

def move_forward():
    timmy.forward(3)
def move_left():
    timmy.left(3)
def move_right():
    timmy.right(3)
def move_back():
    timmy.back(3)

def clean():
    timmy.clear()
screen = turtle.Screen()
screen.listen()
screen.onkeypress(move_forward, 'w')
screen.onkeypress(move_left, 'a')
screen.onkeypress(move_back, 's')
screen.onkeypress(move_right, 'd')
screen.onkeypress(clean, 'c')

screen.exitonclick()