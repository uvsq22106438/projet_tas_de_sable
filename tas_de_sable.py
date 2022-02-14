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

nb_lignes = 3
nb_colonnes = 42

#fonctions

def initialisation(nb_lignes, nb_colonnes):
    configuration = []
    for i in range(nb_lignes):
        configuration.append([0]*nb_colonnes)
    return configuration

def aleatoire(configuration):
    for i in range(nb_lignes):
        for j in range(nb_colonnes):
            configuration[i[j]] = random.randint(0, 10)
    return configuration

def stabilite(case):
    if case >= 4:
        return True
    else:
        return False

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

def coloration(configuration):
    for i in range(nb_colonnes):
        for j in range(nb_lignes):
            case = configuration[i[j]]
            if case==0:
                color = "snow"
            elif case==1:
                color = "goldenrod1"
            elif case==2:
                color = "goldenrod2"
            elif case==3:
                color = "goldenrod3"
            elif case==4:
                color = "goldenrod4"
            elif case==5:
                color = "DarkGoldenrod1"
            elif case==6:
                color = "DarkGoldenrod2"
            elif case==7:
                color = "DarkGoldenrod3"
            elif case==8:
                color = "DarkGoldenrod4"
            elif case==9:
                color = "black"
            canvas.create_rectangle((i*largeur_case, j*hauteur_case),
                    ((i+1)*largeur_case, (j+1)*hauteur_case), fill=color)


#INTERFACE GRAPHIQUE

HEIGHT = 500
WIDTH = 500
largeur_case = WIDTH // (nb_colonnes)
hauteur_case = HEIGHT // (nb_lignes)


#window
root = tk.Tk()

#parametres window
root.title("Grain de sable")
root.geometry("720x380")
root.config(bg="#D2E9E1")

#title
label_title = tk.Label(root, text="click button", font=("courrier", "40"), bg="#D2E9E1")
label_title.pack()

#canvas

racine = tk.Tk()
canvas = tk.Canvas(racine, bg="white", height=HEIGHT, width=WIDTH, command=coloration())
canvas.grid()


#frame
frame = tk.Frame(root, bg="#D2E9E1")
frame.pack(side=tk.BOTTOM)

#widget button
bouton = tk.Button(frame, text="création de la configuration aléatoire", font=("Courrier", "30"), bg="#D2E9E1", fg="black")
bouton.pack()

root.mainloop()







