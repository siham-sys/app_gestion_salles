from data.dao_salle import Datasalle
class ServiceSalle:
    def __init__(self):
        self.dao_salle=Datasalle()

    def ajouter_salle(self,salle):
        if salle.code and salle.description and salle.categorie and salle.capacite:
            if salle.categorie >= 1:
                self.dao_salle.insert_salle(salle)
                return True, "La salle a été ajoutée avec succès"
            else:
                return False, "La capacité doit être supérieure ou égale à 1"
        return False, "Veuillez remplir tous les champs"


