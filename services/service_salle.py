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

    def modifier_salle(self, salle):
        if salle.code and salle.description and salle.categorie and salle.capacite:
            if salle.capacite >= 1:
                self.dao_salle.update_salle(salle)
                return True, "modifiée"
            else:
                return False, "Capacité invalide"
        return False, "il manque des donnees"

    def supprimer_salle(self, code):
        self.dao_salle.delete_salle(code)

    def rechercher_salle(self, code):
        return self.dao_salle.get_salle(code)

    def recuperer_salles(self):
        return self.dao_salle.get_salles()



