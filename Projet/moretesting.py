import pickle

coups = {
    '1' : [],
    '2' : [1],
    '3' : [2],
}

i = 10
fichier_coup = open('coup{0}.obj'.format(i), 'wb')
pickle.dump(coups, fichier_coup)
fichier_coup.close()
print('Coup',i,'enregistre.')

coup_nb = int(input('Tu veux recharger quel coup? '))
print('coup{0}.obj'.format(coup_nb))
fichier_coup2 = open('coup{0}.obj'.format(coup_nb), 'r+b')
coups = pickle.load(fichier_coup2)
fichier_coup2.close()

print(coups)