# PROJET QUESTIONNAIRE V3 : POO
#
# - Pratiquer sur la POO
# - Travailler sur du code existant
# - Mener un raisonnement
#
# -> Définir les entitées (données, actions)
#
# Question
#    - titre       - str
#    - choix       - (str)
#    - bonne_reponse   - str
#
#    - poser()  -> bool
#
# Questionnaire
#    - questions      - (Question)
#
#    - lancer()
#
from json_file import JsonfileService

"""type: soit choix soit réponse, l'utilisateur choisi entre des choix et des réponses """
def demander_reponse_numerique_utlisateur(min, max, type):
    reponse_str = input(f"Votre {type}(entre le {min} et {max}): ")
    try:
        reponse_int = int(reponse_str)
        if min <= reponse_int <= max:
            return reponse_int
        print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
    except:
        print("ERREUR : Veuillez rentrer uniquement des chiffres")
    return demander_reponse_numerique_utlisateur(min, max, type)

"""Fonction qui permet de lister des choix à partir des listes données puis renvoyer le choix """
def lister_les_choix_et_renvoyer_le_choix_de_l_utilisateur(choix):
    for i in range(0, len(choix)):
        print(f"{i+1}- {choix[i]}")
    choix_utilisateur = demander_reponse_numerique_utlisateur(1, len(choix), "choix")
    return choix_utilisateur
    
"""
Menu:
données: les différents fichiers Json
action: afficher et demander des choix et difficultés et renvoyer les questions
"""
class Menu:
    def __init__(self):
        self.json_file_service = JsonfileService()

    def afficher_et_demander_choix_et_difficulte_et_renvoyer_les_questions(self):
        print("+++++++++++++++++BIENVENU SUR LE JEUX QUESTIONNAIRE++++++++++++++++")
        print("Choisir le thème:")
        themes = self.json_file_service.file_json.get_themes()
        choix_themes = lister_les_choix_et_renvoyer_le_choix_de_l_utilisateur(themes)

        print("choisir le titre")
        titres = self.json_file_service.file_json.get_titres_from_theme(themes[choix_themes-1])
        choix_titre = lister_les_choix_et_renvoyer_le_choix_de_l_utilisateur(titres)

        print("choisir la difficulté")
        difficultes = ("débutant", "confirmé", "expert")
        choix_difficulte = lister_les_choix_et_renvoyer_le_choix_de_l_utilisateur(difficultes)

        questions = self.json_file_service.file_json.get_questions_from_theme_and_difficult_et_titre(themes[choix_themes-1],
                                                                                                     titres[choix_titre-1],
                                                                                                     difficultes[choix_difficulte-1])
        return questions


class Question:
    def __init__(self, titre, choix):
        self.titre = titre
        self.choix = choix

    def FromData(data):
        # ....
        q = Question(data[2], data[0], data[1])
        return q

    def poser(self):
        print("QUESTION")
        print("  " + self.titre)
        for i in range(len(self.choix)):
            print("  ", i+1, "-", self.choix[i][0])

        print()
        resultat_response_correcte = False
        reponse_int = demander_reponse_numerique_utlisateur(1, len(self.choix), "reponse")
        if self.choix[reponse_int-1][1] == True:
            print("Bonne réponse")
            resultat_response_correcte = True
        else:
            print("Mauvaise réponse")
            
        print()
        return resultat_response_correcte
    
class Questionnaire:
    def __init__(self, questions):
        self.questions = questions

    def lancer(self):
        score = 0
        for i in range(0, len(self.questions)):
            print(f"Question n°{i+1} sur {len(self.questions)}")
            if self.questions[i].poser():
                score += 1
        return score


# data = (("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris", "Quelle est la capitale de la France ?")
# q = Question.FromData(data)
# print(q.__dict__)

while True:
    questions = Menu().afficher_et_demander_choix_et_difficulte_et_renvoyer_les_questions()
    object_question = []
    for i in range(0, len(questions)):
        object_question.append(Question(questions[i]["titre"], questions[i]["choix"]))
    print("toto")
    score = Questionnaire(object_question).lancer()
    print(f"Score final: {score}/{len(object_question)}")
    print("++++++++++VOULEZ VOUS CONTINUER++++++++++++")
    print("1- oui\n2- Non")
    choix = demander_reponse_numerique_utlisateur(1, 2, "choix")
    if choix == 1:
        break


