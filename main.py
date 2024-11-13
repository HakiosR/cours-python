def exercice1():
    nombre_1 = int(input("Veuillez choisir vos premier nombre : \n\t"))
    nombre_2 = int(input("Veuillez choisir vos deuxième nombre : \n\t"))

    if (nombre_1 > 0 and nombre_2 > 0) or (nombre_1 < 0 and nombre_2 < 0):
        print(f"{nombre_1}*{nombre_2} est positif.")
    elif (nombre_1 < 0 and nombre_2 > 0) or (nombre_2 < 0 and nombre_1 > 0):
        print(f"{nombre_1}*{nombre_2} est négatif.")
    elif nombre_1 == 0 or nombre_2 == 0:
        print(f"{nombre_1}*{nombre_2} est nul.")

def exercice2():
    a = input("Donnez moi une valeur pour A: \n\t")
    b = input("Donnez moi une valeur pour B: \n\t")
    c = input("Donnez moi une valeur pour C: \n\t")

    print("Nous allons permuter les nombres")

    print("Avant permutation : " + a, b, c)

    a, b, c = c, a, b

    print("Après permutation : " + a, b, c)

def exercice3():
    nombre_1 = int(input("Veuillez entrer un nombre :\n\t"))
    reste = nombre_1 % 5
    print(f"Le résultat de {nombre_1} par 5 est de {nombre_1/5} et reste {reste}.")

def exercice4():
    prix_article = float(input("Veuillez saisir le prix de l'article s'il vous plait :\n\t"))
    nombre_article = int(input("Veuillez saisir le nombre d'article s'il vous plait :\n\t"))
    taux_tva = float(input("Veuillez entrer le taux de TVA :\n\t")) / 100

    montant_tva = prix_article * taux_tva 
    prix_article += montant_tva
    prix_total = prix_article * nombre_article
    
    print(f"Le total de {nombre_article} à {prix_article}€ avec un taux de TVA à {taux_tva*100}%, vous devrez payer {prix_total}€")

def exercice5_1():
    table_multiplication = int(input("Veuillez entrer un chiffre entre 1 et 9:\n\t"))
    while table_multiplication <= 0 and table_multiplication > 9: 
        table_multiplication = int(input("Veuillez entrer un chiffre entre 1 et 9:\n\t"))
    
    for i in range(11):
        result = i * table_multiplication
        print(f"{i} * {table_multiplication} = {result}")
        i += 1

def exercice5_2():
    for multiplier in range(10):
        multiplier += 1
        for multiplicateur in range(10):
            multiplicateur += 1
            print(f"{multiplicateur} * {multiplier} = {multiplicateur*multiplier}", sep=" ")
        print("\n")

def exercice6():
    nombre_utilisateur = int(input("Veuillez entrer un nombre pour obtenir ses diviseurs :\t\n"))

    for i in range(nombre_utilisateur):
        i += 1
        
        while i < nombre_utilisateur:
            while nombre_utilisateur > 1:
                i += 1
                tab_diviseur = []
                if (nombre_utilisateur % i) == 0:
                    tab_diviseur.append(i)
            
            nombre_utilisateur -= 1

        print(i)
    

exercice6()