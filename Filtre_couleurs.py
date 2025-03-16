# PIL (Python Imaging Library) bibliothèque de traitement d’image python
from PIL import Image
# Tkinter est une bibliothèque graphique du langage de programmation Python
import tkinter as tk
from tkinter import filedialog

# Importation des filtres
import Filtre_jaune
import Filtre_vert
import Filtre_rouge
import Filtre_noir_blanc

choixuser = input("Veuillez choisir une couleur de filtre pour votre image : 1 pour Jaune, 2 pour Vert, 3 pour Rouge, 4 pour Noir et Blanc et 5 pour faire les 4 filtres : ")

if choixuser == "1":
    Filtre_jaune()

elif choixuser == "2":
    Filtre_vert()

elif choixuser == "3":
    Filtre_rouge()
    
elif choixuser == "4":
    Filtre_noir_blanc()
    
elif choixuser == "5":
    Filtre_jaune()
    Filtre_vert()
    Filtre_rouge()
    Filtre_noir_blanc()
    
else:
    print("Vous n'avez pas choisi de filtre")
