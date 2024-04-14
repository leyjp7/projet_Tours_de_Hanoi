import turtle
import pickle
import time


t = turtle.Turtle() # simplifier l'appel des methodes de turtle
t.hideturtle()   #cache le turtle graphique
turtle.tracer(0) #limite l'animation que le turtle fait
s = turtle.Screen() # simplifier l'appel des methodes de turtle.screen
s.bgcolor('#088DA5')
t.speed(100)
coul = ['#d0bbff' , '#D0CCFE' , '#d0eeff']

#partie A definition des fonctions initiales

def init(n):
    i = n
    tour1 = []
    
    while i > 0:
        tour1.append(i)
        i-=1
    tour2 = []
    tour3 = []
    plateau = [tour1,tour2,tour3]
        
    return plateau

def nombredisques(plateau,numtour):
    li = plateau[numtour]
    return len(li)

def disquesuperieur(plateau,numtour):
        li = plateau[numtour]
        if li==[]:
            a =-1
        else:
            a = li[-1]
        return a

def positiondisque(plateau,numdisque):
    i = 0
    while i < 3:
        t= plateau[i]
        if numdisque in t:
            return i
        i+=1

def verifier_deplacement(plateau,nt1,nt2):
    t1=plateau[nt1]
    t2=plateau[nt2]
    if t2==[]:
        return True
    elif t1==[]:
        return False
    else:
        if t1[-1]<t2[-1]:
            return True
        else:
            return False

def verifier_victoire(plateau,n):
    i =n
    z = 1
    tv = plateau[2]
    if len(tv)!=n:
        return False
    while i >0:
        if tv[i-1]!=z:
            return False
        i-=1
        z +=1
    return True


#Partie b dessin du jeu avec turtle

def rectcentra(lon,lar): #fonction qui dessine une rectange d'un centre
    t.setheading(0)     # setheading est utilise pour minimiser les erruers d'orientation
    t.forward(lon/2)
    t.right(90)
    t.forward(lar)
    t.right(90)
    t.forward(lon)
    t.right(90)
    t.forward(lar)
    t.right(90)
    t.forward(lon/2)
    turtle.update()   #turtle.update()

def rectangle(lon,lar):  #dessine un rectangle d'un coin
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
    t.setheading(0)
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
        t.left(90)
        rectangle(ltour, 6)
        t.end_fill()
        turtle.update()
        i += 1
    t.setheading(0)

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

def efface_plato(n):
    lplato = 110 + 90 * n
    t.fillcolor('#088DA5')
    t.begin_fill()
    t.up()
    t.goto(-300, -200)
    t.setheading(0)
    t.color('#088DA5')
    t.down()
    rectangle(lplato, 20)
    t.setheading(0)
    t.end_fill()
    turtle.update()

    ltour = 20 * n + 20
    t.up()
    t.fillcolor('#088DA5')
    t.forward(22 + 15 * n)
    t.setheading(90)
    t.color('#088DA5')
    t.begin_fill()
    t.down()
    rectangle(ltour, 6)
    t.end_fill()
    turtle.update()
    i = 1
    while i <= 2:
        t.up()
        t.setheading(0)
        t.fillcolor('#088DA5')
        t.forward(30 * n + 30)
        t.color('#088DA5')
        t.begin_fill()
        t.down()
        t.left(90)
        rectangle(ltour, 6)
        t.end_fill()
        turtle.update()
        i += 1
    t.setheading(0)

#partie c et d interaction avec le joueur et annulation de coups
        
def lire_coords(plateau):
    correct = True
    while correct:
        dep = int(input("Tour de départ?"))
        if dep == -1:
            fin = -1
            return dep, fin
        while not(0<=dep<=2 and plateau[dep]!=[]):
            dep = int(input("Tour de départ? (entre 0 et 2)"))

        fin = int(input("Tour d'arrivee?"))
        while not (0 <= fin <= 2):
            fin = int(input("Tour d'arrivee? (entre 0 et 2)"))
        if verifier_deplacement(plateau, dep, fin) == True:
            return dep, fin
        else:
            print('Incorrect')
            correct = True
			
def jouer_un_coup(plateau,n):
    dep,fin=lire_coords(plateau)
    if dep == -1:
        tdep = 0
        fin = 0
        tfin = 0
        return dep, tdep, fin, tfin
    tdep = plateau[dep]
    piece_sup_dep = tdep[-1]
    efface_disque(piece_sup_dep,plateau,n)
    tdep.remove(piece_sup_dep)
    tfin = plateau[fin]
    tfin.append(piece_sup_dep)
    dessine_disque(piece_sup_dep,plateau,n)
    return dep, tdep, fin, tfin

def boucle_jeu():
    n = int(input("Nombre de disques?"))
    lim_coups = (2**n)+2*n
    plateau = init(n)
    coups = {
        0 : init(n)
    }
    dessine_plateau(n)
    dessine_config(plateau, n)
    i = 0
    while i <= lim_coups:
        i += 1
        dep, tdep, fin, tfin = jouer_un_coup(plateau, n)
        if dep == -1:
            return i, n, plateau, lim_coups
        coups[i] = []
        enreg_config(coups, i, tdep, tfin, dep, fin)
        if verifier_victoire(plateau, n):
            return i, n, plateau, lim_coups
        joueur_option = input('Annuler dernier coup (-)\nEnregistre ce coup (1)\nRecharger un coup (2)\nContinuer (c)')
        if joueur_option == '-':
            i, plateau = annuler_dernier_coup(coups, i, dep, fin, n)
        if joueur_option == '1':
            fichier_coup = open('coup{0}.dico'.format(i), 'wb')
            pickle.dump(coups, fichier_coup)
            print('Coup',i,'enregistre.')
        if joueur_option == '2':
            coup_nb = int(input('Tu veux recharger quel coup? '))
            fichier_coup2 = open('coup{0}.dico'.format(coup_nb), 'rb')
            coups = pickle.load(fichier_coup2)
            i = coup_nb
            efface_tout(plateau,n)
            plateau = coups[i]
            dessine_config(plateau, n)

    return i, n, plateau, lim_coups

def enreg_config(dico, i, nt1, nt2, dep, fin):
    dico[i] = []
    for n in range(3):
        if n == dep:
            dico[i].append(list(nt1))
        elif n == fin:
            dico[i].append(list(nt2))
        else:
            prev = dico[i-1][n]
            dico[i].append(prev)

def dernier_coup(dico,i):
    return dico[i]

def annuler_dernier_coup(dico, i, dep, fin, n):
    derni_cou = dico[i]
    tdep = derni_cou[dep]
    tfin = derni_cou[fin]
    piece_sup_fin = tfin[-1]
    efface_disque(piece_sup_fin, derni_cou, n)
    tfin.remove(piece_sup_fin)
    tdep.append(piece_sup_fin)
    dessine_disque(piece_sup_fin, derni_cou, n)
    dico.popitem()
    i -= 1
    plateau = dico[i]
    return i, plateau


def abandonne():
    global aban
    aban = True


#partie E enregistrement et affichage des scores

def score_func(nom, nd, nc, dico):   #fonction qui enregistre les scores
    t = time.asctime()
    dico[nom] = {}
    dico[nom][t] = [nd, nc]
    fichier_score = open('score{0}.obj'.format(nd), 'r+b')
    pickle.dump(dico, fichier_score)
    fichier_score.close()

def deuxElem(elem):
    return elem[2]

def score_tab(n):  # fonction qui accede qux scores et les affiche
    tab_titre = 'Scores pour ' + str(n) + ' disques.'
    tab_desord = []
    fichier_scoretab = open('score{0}.obj'.format(n), 'r+b')
    scor = pickle.load(fichier_scoretab)
    fichier_scoretab.close()
    for nm in scor:
        for t, sc in scor[nm].items():
            if n == sc[0]:
                tab_desord.append([nm, t, sc[1]])
    tab_ord = sorted(tab_desord, key= deuxElem)
    print(tab_titre+str(tab_ord))
    turtle.color('#FA8072')
    turtle.hideturtle()
    turtle.write(tab_titre+str(tab_ord), align = "center", font=("Arial", 12, "normal"))



score = {}


#partie F resolution recursive du jeu

solution = []
def resoudre(n,a=0,b=1,c=2):
    if (n > 0):
        resoudre(n-1,a,c,b)
        solution.append([a, c])
        resoudre(n-1,b,a,c)

def anime_sol(li, n, plateau):
    efface_tout(plateau, n)
    plateau =  init(n)
    dessine_config(plateau, n)
    i = 0
    while i < len(li):
        tdep = plateau[li[i][0]]
        piece_sup_dep = tdep[-1]
        efface_disque(piece_sup_dep, plateau, n)
        tdep.remove(piece_sup_dep)
        tfin = plateau[li[i][1]]
        tfin.append(piece_sup_dep)
        dessine_disque(piece_sup_dep, plateau, n)
        ensuite = input('prochain etape? (o/n)')
        if ensuite == 'o':
            i += 1
        else:
            i = len(li)
    return plateau


#prog principale et lancement du jeu
aban = False

turtle.listen()

jouer = input("voulez vous jouer? (o/n)")
while jouer == "o":
    i, n, plateau, lim_coups = boucle_jeu()
    if verifier_victoire(plateau, n):
        print("Victoire en ", i , "coups!")
        print("Nombre de coups minimale possible : ", 2**n - 1)
        nom = input('donner un nom : ')
        score_func(nom, n, i, score)
        print('Essai suivant enregistre :',score)
        scortab = input('voir tableau de scores? (o/n)')
        if scortab == 'o':
            score_tab(n)
        sol = input('Voir solution (o/n)')
    elif i > lim_coups:
        print('Defaite apres ', i, ' coups. \nMax coups de ',lim_coups,' depasse.')
        print("Nombre de coups minimale possible : ", 2 ** n - 1)
        sol = input('Voir solution (o/n)')
    else:
        print('Jeu abandonne apres ',i,' coups.')
        print("Nombre de coups minimale possible : ", 2 ** n - 1)
        sol = input('Voir solution (o/n)')

    if sol == 'o':
        resoudre(n)
        print(solution)
        plateau = anime_sol(solution, n, plateau)
    efface_tout(plateau, n)
    efface_plato(n)
    jouer = input("voulez vous rejouer? (o/n)")

print('Au revoir!')
turtle.mainloop()





