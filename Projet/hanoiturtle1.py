import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('#088DA5')
t.hideturtle()
turtle.tracer(0, 10)
#t.speed("fastest")
t.speed(10)

def rectcentra(lon,lar):
    t.setheading(0)
    t.forward(lon/2)
    t.right(90)
    t.forward(lar)
    t.right(90)
    t.forward(lon)
    t.right(90)
    t.forward(lar)
    t.right(90)
    t.forward(lon/2)
    turtle.update()

def rectangle(lon,lar):
    t.forward(lon)
    t.right(90)
    t.forward(lar)
    t.right(90)
    t.forward(lon)
    t.right(90)
    t.forward(lar)
    turtle.update()


def dessine_plateau(n):
    lplato = 110 + 90*n
    t.fillcolor('#FA8072')
    t.begin_fill()
    t.up()
    t.goto(-300,-200)
    t.color('#FA8072')
    t.down()
    rectangle(lplato,20)
    t.setheading(0)
    t.end_fill()
    turtle.update()

    ltour = 20*n + 20
    t.up()
    t.fillcolor(coul[0])
    t.forward(22 + 15*n)
    t.setheading(90)
    t.color(coul[0])
    t.begin_fill()
    t.down()
    rectangle(ltour, 6)
    t.end_fill()
    turtle.update()
    i = 1
    while i <= 2:
        t.up()
        t.setheading(0)
        t.fillcolor(coul[i])
        t.forward(30*n + 30)
        t.color(coul[i])
        t.begin_fill()
        t.down()
        t.setheading(90)
        rectangle(ltour, 6)
        t.end_fill()
        turtle.update()
        i += 1

def dessine_disque(nd, plateau, n):
    nt = 0
    for p in plateau:
        y = -200
        x = -300 + 15*n +25 + (30*n + 30)*nt
        for d in p:
            y += 20
            if d == nd:
                t.up()
                t.goto(x,y)
                t.color(coul[nt])
                t.fillcolor(coul[nt])
                t.begin_fill()
                t.down()
                rectcentra((30*d + 10), 20)
                t.end_fill()
                turtle.update()
        nt += 1

def efface_disque(nd, plateau, n):
    nt = 0
    for p in plateau:
        y = -200
        x = -275 + 15*n + 30*n*nt + 30*nt
        for d in p:
            y += 20
            if d == nd:
                t.up()
                t.goto(x, y)
                t.color('#088DA5')
                t.fillcolor('#088DA5')
                t.begin_fill()
                t.down()
                rectcentra((30*d + 10), 20)
                t.end_fill()
                turtle.update()
                dessine_plateau(n)
        nt += 1

def dessine_config(plateau, n):
    i = n
    while i > 0:
        dessine_disque(i, plateau, n)
        i -= 1

def efface_tout(plateau, n):
    i = n
    while i > 0:
        efface_disque(i, plateau, n)
        i -= 1

coul = ['#d0bbff' , '#D0CCFE' , '#d0eeff']


def init(n):
    i = n
    tour1 = []

    while i > 0:
        tour1.append(i)
        i -= 1
    tour2 = []
    tour3 = []
    plateau = [tour1, tour2, tour3]

    return plateau



def resoudre(n,a=0,b=1,c=2):
    if (n > 0):
        resoudre(n-1,a,c,b)
        deplace = [a, c]
        li.append(deplace)
        resoudre(n-1,b,a,c)


def anime_sol(li, n):
    plateau = init(n)
    efface_tout(plateau, n)
    dessine_config(plateau, n)
    turtle.delay(100000)
    for coup in li:
        tdep = plateau[coup[0]]
        piece_sup_dep = tdep[-1]
        efface_disque(piece_sup_dep, plateau, n)
        tdep.remove(piece_sup_dep)
        tfin = plateau[coup[1]]
        tfin.append(piece_sup_dep)
        dessine_disque(piece_sup_dep, plateau, n)

n=3
li = []
plateau = init(n)
dessine_plateau(n)
dessine_config(plateau, n)
sol = input('sol?')
if sol == 'o':
    resoudre(n)
    anime_sol(li,n)

s.exitonclick()