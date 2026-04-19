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