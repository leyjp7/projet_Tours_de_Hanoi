import turtle

li =[]
def resoudre(n,a=0,b=1,c=2):
    if (n > 0):
        resoudre(n-1,a,c,b)
        deplace = [a, c]
        li.append(deplace)
        resoudre(n-1,b,a,c)

resoudre(3)
print(li)
'''
fichier_scoretab = open('coup1.obj', 'rb')
scores = pickle.load(fichier_scoretab)
print(scores)
'''

def anime_sol(li, n):
    plateau =  init(n)
    efface_tout(plateau, n)
    efface_plato(n)
    for coup in li:
        tdep = plateau[coup[0]]
        piece_sup_dep = tdep[-1]
        efface_disque(piece_sup_dep, plateau, n)
        tdep.remove(piece_sup_dep)
        tfin = plateau[coup[1]]
        tfin.append(piece_sup_dep)
        dessine_disque(piece_sup_dep, plateau, n)