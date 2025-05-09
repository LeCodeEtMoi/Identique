import os

print("Bienvenue dans IDENTIQUE.")
print("Pour que le script fonctionne correctement, placez-le dans un dossier contenant uniquement :")
print("- le script Python")
print("- les 2 fichiers texte à comparer\n")

# Demander les noms de fichiers
nom_fichier1 = input("Nom du fichier 1 : ")
nom_fichier2 = input("Nom du fichier 2 : ")

# Vérifier si les fichiers existent
if not os.path.isfile(nom_fichier1):
    print(f"Erreur : le fichier '{nom_fichier1}' n'existe pas.")
    exit()

if not os.path.isfile(nom_fichier2):
    print(f"Erreur : le fichier '{nom_fichier2}' n'existe pas.")
    exit()

# Lire les contenus
with open(nom_fichier1, "r", encoding="utf-8") as f1:
    contenu1 = f1.read()

with open(nom_fichier2, "r", encoding="utf-8") as f2:
    contenu2 = f2.read()

# Comparaison caractère par caractère
en_trop = ""
min_len = min(len(contenu1), len(contenu2))

for i in range(min_len):
    if contenu1[i] != contenu2[i]:
        en_trop += contenu1[i]

# Ajouter les caractères restants s’il y en a
if len(contenu1) > len(contenu2):
    en_trop += contenu1[min_len:]
elif len(contenu2) > len(contenu1):
    en_trop += contenu2[min_len:]

# Résultat
if len(en_trop) == 0:
    print("\nLes fichiers sont identiques.")
elif 1 <= len(en_trop) < 20:
    print("\nLes fichiers sont presque identiques.")
    print("Différences détectées :")
    print(en_trop)
else:
    print("\nLes fichiers sont très différents.")
    print("Différences détectées :")
    print(en_trop)
