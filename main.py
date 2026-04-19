from data.dao_salle import Datasalle
from models.salle import Salle

dao=Datasalle()

s1=  Salle("C250","Programmation","Laboratoire",30)
dao.insert_salle(s1)

for d in dao.get_salles():
    d.afficher_infos()

d=dao.get_salle("C250")
if d:
   d.afficher_infos()

s1.capacite=50
dao.update_salle(s1)

dao.delete_salle("C250")

from services.service_salle import  ServiceSalle
from models.salle import Salle
service = ServiceSalle()

salle1=Salle("A207","Informatique","Lab",35)
print(service.ajouter_salle(salle1))

for d in service.recuperer_salles():
    d.afficher_infos()

d=service.rechercher_salle("A207")
if d:
    d.afficher_infos()

salle1.capacite=50
service.modifier_salle(salle1)

service.supprimer_salle("A207")