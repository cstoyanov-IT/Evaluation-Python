print('Bienvenue dans la StoyCal')

nombreA = float(input('Entrer le premier nombre: '))

while True:
    
    operation = input('Entrer une opération (+, -, *, /) ou taper q pour quitter: ')
    if operation == 'q':
        break

    nombreB = float(input('Entrer le second nombre: '))

    if operation == '+':
        resultat = nombreA + nombreB
    elif operation == '-':
        resultat = nombreA - nombreB
    elif operation == '*':
        resultat = nombreA * nombreB
    elif operation == '/':
        if nombreB != 0:
            resultat = nombreA / nombreB
        else:
            print("Division par 0 non autorisé.")
            # continue permet de sortir de cette itération et de passer à la prochaine.
            continue
    else:
        # Dans le cas ou l'opérateur renseigné est invalide
        print('Opération invalide.')
        continue

    print('Le résultat est:', resultat)
    nombreA = resultat
