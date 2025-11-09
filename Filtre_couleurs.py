# PIL (Python Imaging Library) bibliothèque de traitement d’image python
from PIL import Image
# Tkinter est une bibliothèque graphique du langage de programmation Python
import tkinter as tk
from tkinter import filedialog

# Importation des fichiers de filtres
from Filtre_jaune import Filtre_jaune
from Filtre_vert import Filtre_vert
from Filtre_rouge import Filtre_rouge
from Filtre_noir_blanc import Filtre_noir_blanc

# Demande de sélectionner un fichier image
print("Veuillez choisir votre image pour l'utilisation des filtres")

#Variable correspondant à la sélection du fichier
fichier_image = filedialog.askopenfilename(title="Sélectionner un fichier")

# Chargement du fichier image
img = Image.open(fichier_image)

# Dimension de l'image en largeur et en hauteur
largeur_img, hauteur_img = img.size

# Definition niveau blanc
niveau_blanc = 180
print("niveau_blanc",niveau_blanc)

choixuser = input("Veuillez choisir une couleur de filtre pour votre image : 1 pour Jaune, 2 pour Vert, 3 pour Rouge, 4 pour Noir et Blanc et 5 pour faire les 4 filtres : ")

# Vérification que l'entrée est bien un chiffre valide
if choixuser in ["1", "2", "3", "4", "5"]:
    print("Filtre en cours d'application...")

    if choixuser == "1":
        Filtre_jaune.Filtre_jaune()
    
    elif choixuser == "2":
        Filtre_vert.Filtre_vert()
    
    elif choixuser == "3":
        Filtre_rouge.Filtre_rouge()
    
    elif choixuser == "4":
        Filtre_noir_blanc.Filtre_noir_blanc()
    
    elif choixuser == "5":
        Filtre_jaune.Filtre_jaune()
        Filtre_vert.Filtre_vert()
        Filtre_rouge.Filtre_rouge()
        Filtre_noir_blanc.Filtre_noir_blanc()
    
    print("Filtrage terminé !")
else:
    print("Vous n'avez pas choisi de filtre valide.")
