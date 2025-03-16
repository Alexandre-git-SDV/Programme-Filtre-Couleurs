# PIL (Python Imaging Library) bibliothèque de traitement d’image python
from PIL import Image
# Tkinter est une bibliothèque graphique du langage de programmation Python
import tkinter as tk
from tkinter import filedialog

# Créer une fenêtre Tkinter (mais la masquer)
root = tk.Tk()
root.withdraw()

# Demande de sélectionner un fichier image
print("Veuillez choisir votre image")

#Variable correspondant à la sélection du fichier
fichier_image = filedialog.askopenfilename(title="Sélectionner un fichier")

# Le fichier est défini par la variable fichier_image = input()
print("Démarrage du traitement de : ", fichier_image)

# Chargement du fichier image
img = Image.open(fichier_image)

# Dimension de l'image en largeur et en hauteur
largeur_img, hauteur_img = img.size

# Definition niveau blanc
niveau_blanc = 180
print("niveau_blanc",niveau_blanc)

def Filtre_jaune():
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
    # Sauvegarde du fichier sous le nom de "Image Jaune"
    img.save("Image Jaune.jpg")
    print("Traitement terminé")
    
Filtre_jaune()