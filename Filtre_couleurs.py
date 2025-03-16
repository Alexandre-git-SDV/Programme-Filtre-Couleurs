# PIL (Python Imaging Library) bibliothèque de traitement d’image python
from PIL import Image
# Tkinter est une bibliothèque graphique du langage de programmation Python
import tkinter as tk
from tkinter import filedialog

# Demande le nom du fichier image
print("Veuillez entrer le nom de l'image")

#variable
fichier_image = input()

# Le fichier est défini par la variable fichier_image = input()
print("Démarrage du traitement de : ", fichier_image)

# Chargement du fichier image
img = Image.open(fichier_image)

# Dimension de l'image en largeur et en hauteur
largeur_img, hauteur_img = img.size

# Definition niveau blanc
niveau_blanc = 180
print("niveau_blanc",niveau_blanc)

choixuser = input("Veuillez choisir une couleur de filtre pour votre image : 1 pour Jaune, 2 pour Vert, 3 pour Rouge et 4 pour Noir et Blanc : ")

if choixuser == "1":
    print("Vous avez choisi le filtre Jaune")
    for y in range(hauteur_img):
        for x in range(largeur_img):
            # traitements de l'image
            r, v, b = img.getpixel((x, y))
            # Si il y a des pixels blancs
            if r > niveau_blanc and v > niveau_blanc and b > niveau_blanc:
                # Je remplace le blanc par du JAUNE
                img.putpixel((x, y), (254, 254, 1))
            else:
                img.putpixel((x, y), (b, v, r))
    # Sauvegarde du fichier sous le nom de "résultat A"
    img.save("Image Jaune.jpg")
    print("Traitement terminé")

elif choixuser == "2":
    print("Vous avez choisi le filtre Vert")
    for y in range(hauteur_img):
        for x in range(largeur_img):
            # traitements de l'image
            r, v, b = img.getpixel((x, y))
            # Si il y a des pixels blancs
            if r > niveau_blanc and v > niveau_blanc and b > niveau_blanc:
                # Je remplace le blanc par du VERT
                img.putpixel((x, y), (145, 254, 1))
            else:
                img.putpixel((x, y), (r, b, v))
    # Sauvegarde du fichier sous le nom de "résultat B"
    img.save("Image Verte.jpg")
    print("Traitement image verte terminé")

elif choixuser == "3":
    print("Vous avez choisi le filtre Rouge")
    for y in range(hauteur_img):
        for x in range(largeur_img):
            # traitements de l'image
            r, v, b = img.getpixel((x, y))
            # Si il y a des pixels blancs
            if r > niveau_blanc and v > niveau_blanc and b > niveau_blanc:
                # Je remplace le blanc par du ROUGE
                img.putpixel((x, y), (254, 1, 1))
            else:
                img.putpixel((x, y), (b, r, v))
    img.save("Image Rouge.jpg")
    print("Traitement image rouge terminé")
    
elif choixuser == "4":
    print("Vous avez choisi le filtre Noir et Blanc")
    for y in range(hauteur_img):
        for x in range(largeur_img):
            # traitements de l'image
            r, v, b = img.getpixel((x, y))
            # Si il y a des pixels blancs
            if r > niveau_blanc and v > niveau_blanc and b > niveau_blanc:
                # Je remplace le blanc
                img.putpixel((x, y), (254, 254, 254))  # par du blanc
            else:
                img.putpixel((x, y), (0, 0, 0))
    img.save("Image Noir et Blanc.jpg")
    print("Traitement image noir et blanc terminé")

else:
    print("Vous n'avez pas choisi de filtre")
