def calculer_exercice9():
    listeNombreParfait = []
    for nombre in range(1, 1000):
        somme_diviseurs = sum(i for i in range(1, nombre) if nombre % i == 0)
        if somme_diviseurs == nombre:
            listeNombreParfait.append(nombre)

    print(f"Voici la liste des nombres parfait entre 1 et 1000 : {listeNombreParfait}")

calculer_exercice9()