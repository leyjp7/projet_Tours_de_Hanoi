import turtle
turtle.speed(1)

def rectcentra(lon,lar):
    turtle.forward(lon/2)
    turtle.right(90)
    turtle.forward(lar)
    turtle.right(90)
    turtle.forward(lon)
    turtle.right(90)
    turtle.forward(lar)
    turtle.right(90)
    turtle.forward(lon/2)

n = 5
long = 30*n + 10

turtle.up()
turtle.goto(-200, -200)
turtle.down()
rectcentra(long, 20)
