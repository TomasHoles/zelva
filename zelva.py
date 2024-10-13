from turtle import *


def hvezdy():
    right(75)
    forward(100)
    speed(100)
    bgcolor("black")
    for i in range(4):
        pencolor("yellow")
        left(90)
        for i in range(5):
            right(144)
            forward(100)
    mainloop()



def spirala():
    for i in range(360):
        speed(100)
        shape("turtle")
        bgcolor("black")
        pencolor("yellow")
        width(i//100+1)
        forward(i)
        left(59)
    mainloop()

def barevne_slunce():
    color = ["red","green", "blue","purple", "orange","yellow"]
    for i in range(180):
        speed(1000)
        shape("turtle")
        bgcolor("black")
        pencolor(color[i%6])
        forward(i%500)
        left(i%360)
    mainloop()


def vrtule():
    speed(100)
    shape("turtle")
    bgcolor("black")
    color("yellow")
    for i in range(18):
        left(60)
        forward(180)
        left(90)
        forward(50)
        left(110)
        forward(150)
    mainloop()
        

