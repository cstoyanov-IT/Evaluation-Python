# Code python - Clément Stoyanov
# AVEC BOUCLE FOR
tableau = [13, 23, 15, 28, 4, 32, 7, 12, 5, 98]
print ("Voici les valeurs du tableau ainsi que leur statut pair/impair développé avec une boucle for\n")
for i in range(0,10):
   if tableau[i] % 2 ==0:
       print(tableau[i],'est un nombre pair \n')
   else: print(tableau[i],'est un nombre impair\n')


# AVEC BOUCLE WHILE
tableau = [13, 23, 15, 28, 4, 32, 7, 12, 5, 98]
print ("Voici les valeurs du tableau ainsi que leur statut pair/impair avec une boucle while\n")
i = 0 # Je défini i=0 au début
while i < 10:
    if tableau[i] % 2 ==0:
       print(tableau[i],'est un nombre pair \n')
    else: print(tableau[i],'est un nombre impair \n')

    i+=1 # j'ajoute +1 à i jusqu'à 10
 
# Explication pseudo code
# Je crée un tableau que je stock dans une variable, et je boucle le tableau j'usqu'à arrivé a l'indice 10.
# J'indique grace a une condition que si le reste de % de 2 est 0 alors, j'indique que le nombre est pair sinon il est impair.

