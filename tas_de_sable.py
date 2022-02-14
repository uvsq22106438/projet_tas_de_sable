#########################################
# groupe MPCI 3
# Célia GUILLOT
# Bérénice GUEREL
# Luka ZDRAVKOVIC
# https://github.com/uvsq22106438/projet_tas_de_sable
#########################################


#import des modules
import tkinter as tk
from random import randint


#variables globales



#fonctions

def initialisation(nb_lignes, nb_colonnes):
    tableau = []
    for i in range(nb_lignes):
        tableau.append([0]*nb_colonnes)
    return tableau

def aleatoire():
    for i in range(nb_lignes):
        for j in range(nb_colonnes):
            tableau[i[j]] = random.randint(0, 10)
    return tableau

#interface graphique

root = tk.Tk()
label = tk.label(root, text="", font=("courrier", "40"))
label.grid(row=0, column=0)
bouton = tk.Button(root, text="création de la configuration aléatoire", command=btn, font=("courrier", "30"))
bouton.grid()
root.mainloop()

