# Code Python - Clément Stoyanov
tableau = [15, 16.5, 11.5, 12, 4, 8, 7.5, 13, 17, 8.5]
# J'initialise moyenneok à 0
moyenneok= 0
# ajoute +1 à la variable moyenneok a chque fois qu'un eleve à la moyenne'
for i in range(0,10):
    if tableau [i] >=10:
        moyenneok +=1
    

print('nombre de personne ayant la moyenne : ', moyenneok)

# Explication en pseudo-code: 
# je stock un tableau de 10 notes dans la variable tableau, je fais une boucle sur ce tableau et chaque fois
# qu'un éleve à la moyenne, j'ajoute +1 à la variable moyenneok.
# J'affiche ensuite combien de personnes ont la moyenne en récupérant la variable moyenneok
