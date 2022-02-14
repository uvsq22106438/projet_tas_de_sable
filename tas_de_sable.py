#########################################
# groupe MPCI 3
# Célia GUILLOT
# Bérénice GUEREL
# Luka ZDRAVKOVIC
# https://github.com/uvsq22106438/projet_tas_de_sable
#########################################


#import des modules
import tkinter as tk


#variables globales



#fonctions


#interface graphique

root = tk.Tk()
label = tk.label(root, text="", font=("courrier", "40"))
label.grid(row=0, column=0)
bouton = tk.Button(root, text="création de la configuration aléatoire", command=btn, font=("courrier", "30"))
bouton.grid()
root.mainloop()

