def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? ")
    return reponse_nom


def demander_age():
    age_int = 0
    while age_int == 0:
        age_str = input("Quel est votre âge ? ")
        try:
            age_int = int(age_str) # Convertir la chaîne de caractères en entier, j'ai fait comme ça mais c'est juste pour la concaténation avec + 
        except:
            print("ERREUR: Vous devez rentrer un nombre pour l'âge.")
    return age_int

def afficher_informations_personne(nom, age, taille = 0):
    print()
    print(f"Vous vous appelez {nom}. Vous avez {age} ans.")
    print(f"L'année prochaine vous aurez {age + 1} ans.")
    if age == 17:
        print("Vous êtes presque majeur.")
    elif 12 <= age < 18: # elif age >= 12 and age < 18: est équivalent à elif 12 <= age < 18:. Sinon le and et plus utile quand on à 2 variables différentes pour le test.
        print("Vous êtes un adolescent.")
    elif age == 1 or age == 2:
        print("Vous êtes un bébé.")
    elif age == 18:
        print("Vous êtes tout juste majeur : Félicitation.")
    elif age >= 18:
        print("Vous êtes majeur.")
    elif age < 10:
        print("Vous êtes un enfant.")
    else:
        print("Vous êtes mineur.")

    # afficher la taille
    # taille = 1.75
    # print(type(taille))
    if not taille == 0:
        print(f"Vous mesurez {taille} mètres.")

# nom = demander_nom()
# nom1 = demander_nom()

# age = demander_age()
# age1 = demander_age()

# afficher_informations_personne(nom, age)
# afficher_informations_personne(nom1, age1)

# c'est une constante, on ne peut pas la modifier. Les constantes sont en majuscule. Mais en python les constantes n'existent pas.
NB_PERSONNES = 1

# la boucle for
for i in range(0, NB_PERSONNES):
    # print(i)
    nom = f"personne{i + 1}"
    age = demander_age()
    afficher_informations_personne(nom, age)

    print("""
        Vous pouvez faire ce que vous voulez ici.
        Vous pouvez mettre autant de lignes que vous voulez.
        Vous pouvez mettre des lignes vides.
        Vous pouvez mettre des lignes avec du code.
            Vous pouvez placer les lignes comme vous voulez.
                Selon comment on place les lignes elles seront placées de la même façon.
    """)


