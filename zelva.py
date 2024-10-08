from turtle import *


speed(100)
shape("turtle")
bgcolor("black")

def hvezdy():
    right(75)
    forward(100)

    for i in range(4):
        pencolor("yellow")
        left(90)
        for i in range(5):
            right(144)
            forward(100)



def spirala():
    for i in range(360):
        pencolor("yellow")
        width(i//100+1)
        forward(i)
        left(59)

def barevne_slunce():
    color = ["red","green", "blue","purple", "orange","yellow"]
    for i in range(180):
        pencolor(color[i%6])
        forward(i%500)
        left(i%360)


def parametry():
    speed(10)
    color("yellow")
    for i in range(100):
        left(60)
        forward(180)
        left(90)
        forward(50)
        left(110)
        forward(150)







parametry()
mainloop()