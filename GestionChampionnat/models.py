# models.py

class Equipe:
    def __init__(self, id, nom, date_creation, stade, entraineur, president):
        self.id = id
        self.nom = nom
        self.date_creation = date_creation
        self.stade = stade
        self.entraineur = entraineur
        self.president = president
        self.points = 0
        self.but_marques = 0  # Ajout des attributs
        self.but_concedes = 0
        self.diff_goals = 0

    def afficher(self):
        print(f"Nom: {self.nom}")
        print(f"Date de création: {self.date_creation}")
        print(f"Stade: {self.stade}")
        print(f"Entraineur: {self.entraineur}")
        print(f"Président: {self.president}")


    def afficher(self):
        print(f"Nom: {self.nom}")
        print(f"Date de création: {self.date_creation}")
        print(f"Stade: {self.stade}")
        print(f"Entraineur: {self.entraineur}")
        print(f"Président: {self.president}")

class Match:
    def __init__(self, score_equipe1, score_equipe2, numero_journee, equipe1, equipe2):
        self.score_equipe1 = score_equipe1
        self.score_equipe2 = score_equipe2
        self.numero_journee = numero_journee
        self.equipe1 = equipe1
        self.equipe2 = equipe2

    def saisir_resultat(self, score_equipe1, score_equipe2):
        self.score_equipe1 = score_equipe1
        self.score_equipe2 = score_equipe2

class Championnat:
    def __init__(self, id, nom, date_debut, date_fin, point_gagne, point_perdu, point_nul, type_classement):
        self.id = id
        self.nom = nom
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.point_gagne = point_gagne
        self.point_perdu = point_perdu
        self.point_nul = point_nul
        self.equipes = []
        self.matchs = []
        self.type_classement = type_classement  # Ajout du type de classement

    def ajouter_equipe(self, equipe):
        self.equipes.append(equipe)

    def ajouter_match(self, match):
        self.matchs.append(match)

    def afficher(self):
        print(f"Nom: {self.nom}")
        print(f"Date de début: {self.date_debut}")
        print(f"Date de fin: {self.date_fin}")
        print(f"Type de classement: {self.type_classement}")

    def afficher_classement(self):
        if self.type_classement == "par buts marqués":
            classement = sorted(self.equipes, key=lambda equipe: (equipe.points, equipe.but_marques), reverse=True)
        elif self.type_classement == "buts concédés":
            classement = sorted(self.equipes, key=lambda equipe: (equipe.points, equipe.but_concedes),reverse=True)
        elif self.type_classement == "différence de buts":
            classement = sorted(self.equipes, key=lambda equipe: (equipe.points, equipe.diff_goals), reverse=True)
        else:
            classement = sorted(self.equipes, key=lambda equipe: equipe.points, reverse=True)

        print("Classement:")
        print("Place\Pts\tEquipe")
        for i, equipe in enumerate(classement, 1):
            print(f"{i}\t{equipe.points}\t{equipe.nom}")


    def calculer_point(self, match):
        # Mise à jour des statistiques des équipes
        equipe_dom = match.equipe1
        equipe_ext = match.equipe2

        # Mise à jour des buts marqués et concédés
        equipe_dom.but_marques += match.score_equipe1
        equipe_dom.but_concedes += match.score_equipe2
        equipe_ext.but_marques += match.score_equipe2
        equipe_ext.but_concedes += match.score_equipe1

        # Mise à jour de la différence de buts
        equipe_dom.diff_goals = equipe_dom.but_marques - equipe_dom.but_concedes
        equipe_ext.diff_goals = equipe_ext.but_marques - equipe_ext.but_concedes

        if match.score_equipe1 > match.score_equipe2:  # Si l'équipe à domicile gagne
            equipe_dom.points += self.point_gagne
            equipe_ext.points += self.point_perdu
        elif match.score_equipe1 < match.score_equipe2:  # Si l'équipe à l'extérieur gagne
            equipe_dom.points += self.point_perdu
            equipe_ext.points += self.point_gagne
        else:  # En cas de match nul
            equipe_dom.points += self.point_nul
            equipe_ext.points += self.point_nul


class GestionChampionnat:
    def __init__(self):
        self.championnats = []

    def menu(self):
        print("Menu:")
        print("1. Ajouter un championnat")
        print("2. Ajouter une équipe à un championnat")
        print("3. Ajouter un match à un championnat")
        print("4. Afficher les détails d'un championnat")
        print("5. Afficher le classement d'un championnat")
        print("6. Quitter")

    def ajouter_championnat(self, championnat):
        self.championnats.append(championnat)

    def ajouter_equipe(self, championnat, equipe):
        championnat.ajouter_equipe(equipe)

    def ajouter_match(self, championnat, match):
        championnat.ajouter_match(match)
        championnat.calculer_point(match)

    def afficher_details_championnat(self, championnat):
        championnat.afficher()

    def afficher_classement(self, championnat):
        championnat.afficher_classement()