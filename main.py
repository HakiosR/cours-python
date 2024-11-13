import tkinter as tk
from tkinter import messagebox

def exercice1_interface():
    exercice1_window = tk.Toplevel()
    exercice1_window.title("Exercice 1")

    label1 = tk.Label(exercice1_window, text="Veuillez entrer un nombre :")
    label1.pack(pady=5)
    entry1 = tk.Entry(exercice1_window)
    entry1.pack(pady=5)

    label2 = tk.Label(exercice1_window, text="Veuillez entrer un autre nombre :")
    label2.pack(pady=5)
    entry2 = tk.Entry(exercice1_window)
    entry2.pack(pady=5)

    def calculer_exercice1():
        try:
            nombre1 = int(entry1.get())
            nombre2 = int(entry2.get())

            if (nombre1 > 0 and nombre2 > 0) or (nombre1 < 0 and nombre2 < 0):
                resultat = "Le produit de ces deux nombres est positif."
            elif (nombre1 < 0 and nombre2 > 0) or (nombre1 > 0 and nombre2 < 0):
                resultat = "Le produit de ces deux nombres est négatif."
            else:
                resultat = "Le produit de ces deux nombres est nul."

            messagebox.showinfo("Résultat", resultat)
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des valeurs entières valides.")

    bouton_valider = tk.Button(exercice1_window, text="Calculer", command=calculer_exercice1)
    bouton_valider.pack(pady=10)

def exercice2_interface():
    exercice2_window = tk.Toplevel()
    exercice2_window.title("Exercice 2")

    label1 = tk.Label(exercice2_window, text="Veuillez entrer un nombre (A) :")
    label1.pack(pady=5)
    entryA = tk.Entry(exercice2_window)
    entryA.pack(pady=5)

    label2 = tk.Label(exercice2_window, text="Veuillez entrer un autre nombre (B) :")
    label2.pack(pady=5)
    entryB = tk.Entry(exercice2_window)
    entryB.pack(pady=5)

    label3 = tk.Label(exercice2_window, text="Veuillez entrer un dernier nombre (C) :")
    label3.pack(pady=5)
    entryC = tk.Entry(exercice2_window)
    entryC.pack(pady=5)

    def calculer_exercice2():
        try:
            nombreA = int(entryA.get())
            nombreB = int(entryB.get())
            nombreC = int(entryC.get())

            resultat_avant = f"Avant permutation : A = {nombreA}, B = {nombreB}, C = {nombreC}"
            nombreA, nombreB, nombreC = nombreC, nombreA, nombreB
            resultat_apres = f"Après permutation : A = {nombreA}, B = {nombreB}, C = {nombreC}"

            messagebox.showinfo("Résultat", f"{resultat_avant}\n{resultat_apres}")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des valeurs entières valides.")

    bouton_valider = tk.Button(exercice2_window, text="Permuter", command=calculer_exercice2)
    bouton_valider.pack(pady=10)

def exercice3_interface():
    exercice3_window = tk.Toplevel()
    exercice3_window.title("Exercice 3 - Division par 5")

    label = tk.Label(exercice3_window, text="Veuillez entrer un nombre que vous voulez diviser par 5 :")
    label.pack(pady=5)
    entry = tk.Entry(exercice3_window)
    entry.pack(pady=5)

    def calculer_exercice3():
        try:
            nombreUser = int(entry.get())
            divisionBy5 = nombreUser // 5
            resteDivision = nombreUser % 5
            messagebox.showinfo("Résultat", f"Le résultat de la division de {nombreUser} par 5 est {divisionBy5} avec un reste de {resteDivision}")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre entier valide.")

    bouton_valider = tk.Button(exercice3_window, text="Calculer", command=calculer_exercice3)
    bouton_valider.pack(pady=10)

def exercice4_interface():
    exercice4_window = tk.Toplevel()
    exercice4_window.title("Exercice 4 - Calcul de prix")

    labels_texts = [
        "Veuillez entrer le prix HT de l'article :",
        "Veuillez entrer la quantité :",
        "Veuillez entrer le taux de TVA (%) :"
    ]
    entries = []

    for text in labels_texts:
        label = tk.Label(exercice4_window, text=text)
        label.pack(pady=5)
        entry = tk.Entry(exercice4_window)
        entry.pack(pady=5)
        entries.append(entry)

    def calculer_exercice4():
        try:
            prixHT = float(entries[0].get())
            quantite = int(entries[1].get())
            tauxTVA = float(entries[2].get()) / 100
            prixTTC = prixHT + (prixHT * tauxTVA)
            prixTotal = prixTTC * quantite
            messagebox.showinfo("Résultat", f"Prix TTC: {prixTTC:.2f}€, Prix Total: {prixTotal:.2f}€")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des valeurs valides.")

    bouton_valider = tk.Button(exercice4_window, text="Calculer", command=calculer_exercice4)
    bouton_valider.pack(pady=10)

def exercice5A_interface():
    exercice5A_window = tk.Toplevel()
    exercice5A_window.title("Exercice 5A - Table de multiplication")

    label = tk.Label(exercice5A_window, text="Veuillez entrer le nombre de la table de multiplication (1-10) :")
    label.pack(pady=5)
    entry = tk.Entry(exercice5A_window)
    entry.pack(pady=5)

    def calculer_exercice5A():
        try:
            nombreTable = int(entry.get())
            if nombreTable < 1 or nombreTable > 10:
                raise ValueError("Le nombre doit être entre 1 et 10.")
            resultat = "\n".join([f"{nombreTable} x {i} = {nombreTable * i}" for i in range(1, 11)])
            messagebox.showinfo("Résultat", resultat)
        except ValueError as e:
            messagebox.showerror("Erreur", str(e))

    bouton_valider = tk.Button(exercice5A_window, text="Afficher", command=calculer_exercice5A)
    bouton_valider.pack(pady=10)

def exercice5B_interface():
    exercice5B_window = tk.Toplevel()
    exercice5B_window.title("Exercice 5B - Tables de multiplication")

    def afficher_exercice5B():
        resultat = ""
        for i in range(1, 10):
            resultat += f"Table de multiplication de {i} :\n"
            resultat += "\t".join([f"{j} x {i} = {i * j}" for j in range(1, 11)]) + "\n\n"
        messagebox.showinfo("Résultat", resultat)

    bouton_valider = tk.Button(exercice5B_window, text="Afficher les tables", command=afficher_exercice5B)
    bouton_valider.pack(pady=10)

def exercice6_interface():
    exercice6_window = tk.Toplevel()
    exercice6_window.title("Exercice 6 - Diviseurs d'un nombre")

    label = tk.Label(exercice6_window, text="Veuillez entrer un nombre :")
    label.pack(pady=5)
    entry = tk.Entry(exercice6_window)
    entry.pack(pady=5)

    def calculer_exercice6():
        try:
            nombreUser = int(entry.get())
            diviseurs = [1]
            diviseurs = diviseurs + [i for i in range(2, nombreUser // 2 + 1) if nombreUser % i == 0] + [nombreUser]
            messagebox.showinfo("Résultat", f"Les diviseurs de {nombreUser} sont : {diviseurs}")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre entier valide.")
            calculer_exercice6()

    bouton_valider = tk.Button(exercice6_window, text="Afficher les diviseurs", command=calculer_exercice6)
    bouton_valider.pack(pady=10)

def exercice7_interface():
    exercice7_window = tk.Toplevel()
    exercice7_window.title("Exercice 7 - Nombres cubiques")

    def calculer_exercice7():
        nombreCubique = []
        for nombre in range(150, 411):
            chiffreCubique = [int(chiffre) for chiffre in str(nombre)]
            nombreFinal = sum(chiffre ** 3 for chiffre in chiffreCubique)
            if nombreFinal == nombre:
                nombreCubique.append(nombre)

        messagebox.showinfo("Résultat", f"Voici les nombres cubiques : {nombreCubique}")

    bouton_valider = tk.Button(exercice7_window, text="Calculer", command=calculer_exercice7)
    bouton_valider.pack(pady=10)

def exercice8_interface():
    exercice8_window = tk.Toplevel()
    exercice8_window.title("Exercice 8 - Calcul du PGCD")

    label1 = tk.Label(exercice8_window, text="Veuillez entrer le premier nombre :")
    label1.pack(pady=5)
    entry1 = tk.Entry(exercice8_window)
    entry1.pack(pady=5)

    label2 = tk.Label(exercice8_window, text="Veuillez entrer le deuxième nombre :")
    label2.pack(pady=5)
    entry2 = tk.Entry(exercice8_window)
    entry2.pack(pady=5)

    def calculer_exercice8():
        try:
            nombre1 = int(entry1.get())
            nombre2 = int(entry2.get())

            if nombre1 < 0 or nombre2 < 0:
                raise ValueError("Les deux nombres doivent être positifs.")

            if nombre2 > nombre1:
                nombre1, nombre2 = nombre2, nombre1

            while nombre1 != nombre2:
                if nombre1 > nombre2:
                    nombre1 -= nombre2
                else:
                    nombre2 -= nombre1

            messagebox.showinfo("Résultat", f"Le PGCD est {nombre1}")
        except ValueError as e:
            messagebox.showerror("Erreur", str(e))

    bouton_valider = tk.Button(exercice8_window, text="Calculer", command=calculer_exercice8)
    bouton_valider.pack(pady=10)

def exercice9_interface():
    exercice9_window = tk.Toplevel()
    exercice9_window.title("Exercice 9 - Nombres parfaits")

    def calculer_exercice9():
        listeNombreParfait = []
        for nombre in range(1, 1000):
            somme_diviseurs = sum(i for i in range(1, nombre) if nombre % i == 0)
            if somme_diviseurs == nombre:
                listeNombreParfait.append(nombre)

        messagebox.showinfo("Résultat", f"Les nombres parfaits entre 1 et 1000 sont : {listeNombreParfait}")

    bouton_valider = tk.Button(exercice9_window, text="Calculer", command=calculer_exercice9)
    bouton_valider.pack(pady=10)


def main():
    root = tk.Tk()
    root.title("Choix des exercices :")

    width = 1000
    height = 600

    screen_width = root.winfo_screenwidth()
    screen_hight = root.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_hight // 2) - (height // 2)

    root.geometry(f"{width}x{height}+{x}+{y}")

    root.configure(bg="#F0F0F0")

    style_button = {"bg": "#4CAF50", "fg": "white", "font": ("Arial", 10, "bold"), "relief": "raised"}

    bouton_exercice1 = tk.Button(root, text="Exercice 1", command=exercice1_interface, **style_button)
    bouton_exercice1.pack(pady=10, padx=20)

    bouton_exercice2 = tk.Button(root, text="Exercice 2", command=exercice2_interface, **style_button)
    bouton_exercice2.pack(pady=10, padx=20)

    bouton_exercice3 = tk.Button(root, text="Exercice 3", command=exercice3_interface, **style_button)
    bouton_exercice3.pack(pady=10, padx=20)

    bouton_exercice4 = tk.Button(root, text="Exercice 4", command=exercice4_interface, **style_button)
    bouton_exercice4.pack(pady=10, padx=20)

    bouton_exercice5A = tk.Button(root, text="Exercice 5A", command=exercice5A_interface, **style_button)
    bouton_exercice5A.pack(pady=10, padx=20)

    bouton_exercice5B = tk.Button(root, text="Exercice 5B", command=exercice5B_interface, **style_button)
    bouton_exercice5B.pack(pady=10, padx=20)

    bouton_exercice6 = tk.Button(root, text="Exercice 6", command=exercice6_interface, **style_button)
    bouton_exercice6.pack(pady=10, padx=20)

    bouton_exercice7 = tk.Button(root, text="Exercice 7", command=exercice7_interface, **style_button)
    bouton_exercice7.pack(pady=10, padx=20)

    bouton_exercice8 = tk.Button(root, text="Exercice 8", command=exercice8_interface, **style_button)
    bouton_exercice8.pack(pady=10, padx=20)

    bouton_exercice9 = tk.Button(root, text="Exercice 9", command=exercice9_interface, **style_button)
    bouton_exercice9.pack(pady=10, padx=20)

    bouton_quitter = tk.Button(root, text="Quitter", command=root.quit, bg="#E53935", fg="white", font=("Arial", 10, "bold"))
    bouton_quitter.pack(pady=20, padx=20)


    root.mainloop()

if __name__ == "__main__":
    main()
