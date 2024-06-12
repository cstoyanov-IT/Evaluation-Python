# Code Python - Clément Stoyanov

tableau = [31, 54, 23, 98, 43, 32, 72, 40, 21, 17]

valeurRecherche = int(input("Entrez un entier à rechercher dans le tableau : "))

nb = 0

for nombre in tableau:
    if nombre == valeurRecherche:
        nb += 1

if nb > 0:
    print(f"L'entier {valeurRecherche} est présent dans le tableau et apparaît {nb} fois.")
else:
    print(f"L'entier {valeurRecherche} n'est pas présent dans le tableau.")

# Explication pseudo Code
# J'ai prévu 2 différentes variables pour comparé la valeur séparé au tableau
