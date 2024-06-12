# Code en python - Clément Stoyanov
pourcentage = float(input("Saisir le pourcentage de vote obtenu par le candidat : "))
if pourcentage <5 :
    print('Le candidat est éliminé')
elif pourcentage <50:
    print ('Le candidat est qualifié au second tour')
else:
    print(' Le candidat est élu')


# Explication pseudo code
# Je stock le pourcentage de vote dans une variable, et défini selon si il obtient au moins 50% il est élu. 
# Si il obtient moins de 50% il passe au second tour, si il obtient moins de 5% il est éliminé.

