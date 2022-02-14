#########################################
# groupe MPCI 3
# Célia GUILLOT
# Bérénice GUEREL
# Luka ZDRAVKOVIC
# https://github.com/uvsq22106438/projet_tas_de_sable
#########################################


#MODULES

import tkinter as tk
from random import randint


#VARIABLES GLOBALES



#FONCTIONS

def avalanche(configuration):
    for i in range(nb_lignes):
        for j in range(nb_colonnes):
            case = configuration[i[j]]
            if stabilite(case) == True:
                case -= 4
                configuration[i-1[j]] += 1
                configuration[i+1[j]] += 1
                configuration[i[j-1]] += 1
                configuration[i[j+1]] += 1
    return configuration


#INTERFACE GRAPHIQUE



#window
root = tk.Tk()

#parametres window
root.title("Grain de sable")
root.geometry("720x380")
root.config(bg="#D2E9E1")

#title
label_title = tk.Label(root, text="click button", font=("courrier", "40"), bg="#D2E9E1")
label_title.pack()

#frame
frame = tk.Frame(root, bg="#D2E9E1")


#widget button
bouton = tk.Button(root, text="création de la configuration aléatoire", font=("Courrier", "30"), bg="#D2E9E1", fg="black")
bouton.pack()


root.mainloop()


