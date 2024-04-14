import turtle

t = turtle.Turtle()
s = turtle.Screen()

xclick = 0
yclick = 0

def coordonnees(x, y):
    global xclick
    global yclick
    xclick = x
    yclick = y
    print(x, y)

'''
def click():
    s.onscreenclick(coordonnees)
    print(xclick, yclick)
    s.mainloop()
'''


s.onscreenclick(coordonnees)
s.mainloop()