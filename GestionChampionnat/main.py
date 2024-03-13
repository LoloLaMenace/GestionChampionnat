from models import GestionChampionnat, Championnat, Equipe, Match

def main():
    gestionnaire = GestionChampionnat()

    # Création automatique d'un championnat avec 10 équipes
    championnat = Championnat(1, "Ligue 1", "01/08/2024", "30/05/2025", 3, 0, 1, "buts concédés")
    for i in range(1, 11):
        equipe = Equipe(i, f"Équipe {i}", "01/01/1900", f"Stade {i}", f"Entraîneur {i}", f"Président {i}")
        championnat.ajouter_equipe(equipe)
    gestionnaire.ajouter_championnat(championnat)

    while True:
        gestionnaire.menu()
        choix = input("Entrez votre choix : ")

        if choix == '1':
            nom = input("Entrez le nom du championnat : ")
            date_debut = input("Entrez la date de début : ")
            date_fin = input("Entrez la date de fin : ")
            point_gagne = int(input("Entrez le nombre de points pour une victoire : "))
            point_perdu = int(input("Entrez le nombre de points pour une défaite : "))
            point_nul = int(input("Entrez le nombre de points pour un match nul : "))
            type_classement = input("Entrez le type de classement (par buts marqués, buts concédés, différence de buts) : ")

            championnat = Championnat(len(gestionnaire.championnats) + 1, nom, date_debut, date_fin, point_gagne, point_perdu, point_nul, type_classement)
            gestionnaire.ajouter_championnat(championnat)
            print("Championnat ajouté avec succès!")

        elif choix == '2':
            nom_equipe = input("Entrez le nom de l'équipe : ")
            date_creation = input("Entrez la date de création de l'équipe : ")
            stade = input("Entrez le nom du stade de l'équipe : ")
            entraineur = input("Entrez le nom de l'entraîneur de l'équipe : ")
            president = input("Entrez le nom du président de l'équipe : ")

            equipe = Equipe(len(gestionnaire.championnats) + 1, nom_equipe, date_creation, stade, entraineur, president)

            # Choisissez un championnat existant où ajouter l'équipe
            print("Choisissez le championnat où ajouter l'équipe :")
            for i, championnat in enumerate(gestionnaire.championnats, 1):
                print(f"{i}. {championnat.nom}")
            choix_championnat = int(input("Entrez le numéro du championnat : "))
            gestionnaire.ajouter_equipe(gestionnaire.championnats[choix_championnat - 1], equipe)
            print("Équipe ajoutée avec succès!")

        elif choix == '3':
            print("Choisissez le championnat où ajouter le match :")
            for i, championnat in enumerate(gestionnaire.championnats, 1):
                print(f"{i}. {championnat.nom}")
            choix_championnat = int(input("Entrez le numéro du championnat : "))
            championnat = gestionnaire.championnats[choix_championnat - 1]

            print("Choisissez l'équipe à domicile :")
            for i, equipe in enumerate(championnat.equipes, 1):
                print(f"{i}. {equipe.nom}")
            choix_dom = int(input("Entrez le numéro de l'équipe à domicile : "))
            equipe_dom = championnat.equipes[choix_dom - 1]

            print("Choisissez l'équipe à l'extérieur :")
            for i, equipe in enumerate(championnat.equipes, 1):
                if equipe != equipe_dom:
                    print(f"{i}. {equipe.nom}")
            choix_ext = int(input("Entrez le numéro de l'équipe à l'extérieur : "))
            equipe_ext = championnat.equipes[choix_ext - 1]

            score_dom = int(input("Entrez le score de l'équipe à domicile : "))
            score_ext = int(input("Entrez le score de l'équipe à l'extérieur : "))

            match = Match(score_dom, score_ext, len(championnat.matchs) + 1, equipe_dom, equipe_ext)
            gestionnaire.ajouter_match(championnat, match)
            print("Résultat du match ajouté avec succès!")



        elif choix == '4':
            # Afficher les détails d'un championnat
            print("Choisissez le championnat à afficher :")
            for i, championnat in enumerate(gestionnaire.championnats, 1):
                print(f"{i}. {championnat.nom}")
            choix_championnat = int(input("Entrez le numéro du championnat : "))
            gestionnaire.afficher_details_championnat(gestionnaire.championnats[choix_championnat - 1])

        elif choix == '5':
            # Afficher le classement d'un championnat
            print("Choisissez le championnat à afficher le classement :")
            for i, championnat in enumerate(gestionnaire.championnats, 1):
                print(f"{i}. {championnat.nom}")
            choix_championnat = int(input("Entrez le numéro du championnat : "))
            gestionnaire.afficher_classement(gestionnaire.championnats[choix_championnat - 1])

        elif choix == '6':
            print("Au revoir!")
            break

        else:
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 6.")

if __name__ == "__main__":
    main()