# PIL (Python Imaging Library) bibliothèque de traitement d’image python
from PIL import Image

# je demande le nom du fichier
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

# Définitions des variables de y = hauteur_img
# Définitions des variables de X = largeur_img

for y in range(hauteur_img) :
    for x in range(largeur_img) :

         #traitements de l'image

        r,v,b=img.getpixel((x,y))
        # Si il y a des pixels blancs
        if r>niveau_blanc and v>niveau_blanc and b>niveau_blanc :
            # Je remplace le blanc par du JAUNE
            img.putpixel((x,y),(254,254,1))
        else:
            #
            img.putpixel((x,y),(b,v,r))
#Sauvegarde du fichier sous le nom de "résultat A"
img.save("résultat A.jpg")

# je demande le nom du fichier
print("Veuillez entrer le nom de l'image")

#variable
fichier_image = input()

# Le fichier est défini par la variable fichier_image = input()
print("Démarrage du traitement de : ", fichier_image)

# Chargement du fichier image
img = Image.open(fichier_image)

# Dimension de l'image en largeur et en hauteur
largeur_img, hauteur_img = img.size

# Définitions des variables de y = hauteur_img
# Définitions des variables de X = largeur_img

for y in range(hauteur_img) :
    for x in range(largeur_img) :

         #traitements de l'image

        r,v,b=img.getpixel((x,y))
        # Si il y a des pixels blancs
        if r>niveau_blanc and v>niveau_blanc and b>niveau_blanc :
        # Je remplace le blanc par du VERT
            img.putpixel((x,y),(145,254,1))
        else:
            #
            img.putpixel((x,y),(r,b,v))
#Sauvegarde du fichier sous le nom de "résultat B"
img.save("résultat B.jpg")



# Traitemens de la troisième image

# je demande le nom du fichier
print("Veuillez entrer le nom de l'image")

#variable

fichier_image = input()

# Le fichier est défini par la variable fichier_image = input()
print("Démarrage du traitement de : ", fichier_image)

# Chargement du fichier image
img = Image.open(fichier_image)

# Dimension de l'image en largeur et en hauteur
largeur_img, hauteur_img = img.size

# Définitions des variables de y = hauteur_img
# Définitions des variables de X = largeur_img

for y in range(hauteur_img) :
    for x in range(largeur_img) :

        #traitements de l'image

        r,v,b=img.getpixel((x,y))
        # Si il y a des pixels blancs
        if r>niveau_blanc and v>niveau_blanc and b>niveau_blanc :
        # Je remplace le blanc par du ROUGE
            img.putpixel((x,y),(254,1,1))
        else:
            #
            img.putpixel((x,y),(b,r,v))

img.save("résultat C.jpg")
#Sauvegarde du fichier sous le nom de "résultat C"