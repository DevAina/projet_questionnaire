import json
"""
question_json:
  - filename: fichiers qui comporte les caractéristiques du question
"""
class question_json:
    categorie = ""
    difficulte = ""
    nb_question = 0
    data = None

    def __init__(self, filename):
        self.filename = filename
        self.load_file()

    def load_file(self):
        try:
            file = open(self.filename, 'r')
        except FileNotFoundError:
            return
        else:
            read_file = file.read()
            file.close()
        #dictionnaire
        self.data = json.loads(read_file)
        
"""
Questions:
    -contient une liste de question_json

    action: obtenir les différents thèmes, tiitres et question à partir du titre et thème et difficultés
"""        
class Questions:
    question_json =  (question_json("animaux_leschats_debutant.json"),
                     question_json("arts_museedulouvre_debutant.json"),
                     question_json("bandedessinnee_tintin_debutant.json"),
                     question_json("cinema_alien_debutant.json"),
                     question_json("cinema_starwars_debutant.json"),
                     question_json("animaux_leschats_confirme.json"),
                     question_json("arts_museedulouvre_confirme.json"),
                     question_json("bandedessinnee_tintin_confirme.json"),
                     question_json("cinema_alien_confirme.json"),
                     question_json("cinema_starwars_confirme.json"),
                     question_json("animaux_leschats_expert.json"),
                     question_json("arts_museedulouvre_expert.json"),
                     question_json("bandedessinnee_tintin_expert.json"),
                     question_json("cinema_alien_expert.json"),
                     question_json("cinema_starwars_expert.json"))   

    def get_themes(self):
        themes = []
        for i in range(0, len(self.question_json)):
            theme = self.question_json[i].data["categorie"]
            if not theme in themes:
                themes.append(theme)
        return themes
    
    def get_titres_from_theme(self, theme):
        titres = []
        for i in range(0, len(self.question_json)):
            if self.question_json[i].data["categorie"] == theme:
                titre = self.question_json[i].data["titre"]
                if not titre in titres:
                    titres.append(titre)
        return titres

    def get_questions_from_theme_and_difficult_et_titre(self, theme, titre, difficult):
        for i in range(0, len(self.question_json)):
            if self.question_json[i].data["categorie"] == theme and self.question_json[i].data["titre"] == titre and self.question_json[i].data["difficulte"] == difficult:
                return self.question_json[i].data["questions"]
        
    

class JsonfileService:
    file_json = Questions()  





    

    
