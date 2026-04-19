import mysql.connector
import json
from models.salle import Salle

class Datasalle :
    def get_connection(self):
        with open("./data/config.json","r") as f:
            config = json.load(f)
        conn= mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )
        return conn
    def insert_salle(self,salle):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(" insert into salle values (%s, %s, %s, %s )",
               (salle.code, salle.description, salle.categorie, salle.capacite))
        conn.commit()
        cursor.close()
        conn.close()
