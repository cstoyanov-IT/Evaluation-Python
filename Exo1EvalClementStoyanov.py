# Version Python Clément Stoyanov
# Récupère les 3 nombre entiers
nombreA = int(input("Saisir un premier nombre entier : "))
nombreB = int(input("Saisir un second nombre entier : "))
nombreC = int(input("Saisir un troisième nombre entier : "))
# Effectue la somme de ces 3 nombre puis affiche la somme
somme = nombreA+nombreB+nombreC
print ('la somme de ces 3 nombres est : ', somme)
# Divise la somme par 3 pour obtenir la moyenne et affiche le résultat
resultat = (somme / 3)
print ("La moyenne de ces 3 nombres est", resultat)

# Explication en peudo code :

# Je demande à l'utilisateur de renseigner 3 nombres que je stock dans des variables,
# J'effectue la somme de ces 3 nombres et j'affiche la somme.
# je divise cette somme par 3 car dans ce programme, nous avons 3 nombres renseignés.
# J'affiche le résultat
