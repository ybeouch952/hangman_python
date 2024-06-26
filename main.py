import random

def choisir_mot():

    mot_choisi = None
    with open('francais.txt', 'r') as file:
        lignes = file.readlines()
        ligne_choisie = random.randint(0, len(lignes) - 1)
        mot_choisi = lignes[ligne_choisie].strip()
        
    return mot_choisi

def afficher_mot(mot, lettrestrouve):
    mot_affiche = ""
    for lettre in mot:
        if lettre in lettrestrouve:
            mot_affiche += lettre
        else:
            mot_affiche += "_"
    return mot_affiche

def jouer_pendu():
    mot_a_deviner = choisir_mot() 
    lettrestrouve = set()
    essai_restant = 6
    mot_cache = afficher_mot(mot_a_deviner, lettrestrouve)

    print("Bienvenue sur le jeu du pendu")
    print(f"Mot à deviner : {mot_cache}")

    while essai_restant > 0 and '_' in mot_cache:
        lettre = input("Deviner une lettre : ")
        if lettre in lettrestrouve:
            print("Vous avez déjà deviné cette lettre")
        elif lettre in mot_a_deviner:
            lettrestrouve.add(lettre)
            print("Bonne lettre !")
        else:
            essai_restant -= 1
            print(f"Mauvaise lettre, il vous reste {essai_restant} essais.")
        mot_cache = afficher_mot(mot_a_deviner, lettrestrouve)
        print(f"Mot à deviner : {mot_cache}")

    if '_' not in mot_cache:
        print("Vous avez deviné le mot :", mot_a_deviner)
    else:
        print("Vous avez perdu, le mot était", mot_a_deviner)

def rejouer():
    while True:
        reponse = input("Voulez-vous rejouer ? (oui/non) : ")
        if reponse == 'oui':
            jouer_pendu()
        elif reponse == 'non':
            print("Merci d'avoir joué !")
            break
        else:
            print("Réponse invalide. Veuillez répondre par 'oui' ou 'non'.")

jouer_pendu()
rejouer()