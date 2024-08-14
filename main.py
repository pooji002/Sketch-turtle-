#Random sketching with use of keyboard buttons
from turtle import Turtle, Screen

tut=Turtle()
sc=Screen()
sc.listen()
def move_forward():
    tut.forward(20)
def move_back():
    tut.backward(20)
def move_right():
    tut.right(10)
def move_left():
    tut.left(10)
def clear():
    tut.clear()
    tut.penup()
    tut.home()
    tut.pendown()
sc.onkey(move_forward,"w")
sc.onkey(move_back,"s")
sc.onkey(move_right,"d")
sc.onkey(move_left,"a")
sc.onkey(clear,"c")






sc.exitonclick()