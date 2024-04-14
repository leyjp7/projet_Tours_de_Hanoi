import turtle
import pickle
import time


t = turtle.Turtle() # simplifier l'appel des methodes de turtle
t.hideturtle()   #cache le turtle graphique
turtle.tracer(0) #limite l'animation que le turtle fait
s = turtle.Screen() # simplifier l'qppel des methodes de turtle.screen
s.bgcolor('#088DA5')
t.speed(100)
coul = ['#d0bbff' , '#D0CCFE' , '#d0eeff']



aban = True

def abandonne():
    global aban
    aban = False


while aban:
    s.onkey(abandonne, 'Up')
    s.listen()
    print(aban)

turtle.mainloop()