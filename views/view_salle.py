import customtkinter as ctk
from tkinter import ttk
from models.salle import Salle
from services.service_salle import ServiceSalle


class ViewSalle(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Gestion des Salles")
        self.geometry("900x700")


        self.service_salle = ServiceSalle()


        self.entry_code = ctk.CTkEntry(self, placeholder_text="Code")
        self.entry_code.pack(pady=5)

        self.entry_desc = ctk.CTkEntry(self, placeholder_text="Description")
        self.entry_desc.pack(pady=5)

        self.entry_cat = ctk.CTkEntry(self, placeholder_text="Categorie")
        self.entry_cat.pack(pady=5)

        self.entry_cap = ctk.CTkEntry(self, placeholder_text="Capacite")
        self.entry_cap.pack(pady=5)


        ctk.CTkButton(self, text="Ajouter", command=self.ajouter_salle).pack(pady=5)
        ctk.CTkButton(self, text="Modifier", command=self.modifier_salle).pack(pady=5)
        ctk.CTkButton(self, text="Supprimer", command=self.supprimer_salle).pack(pady=5)
        ctk.CTkButton(self, text="Rechercher", command=self.rechercher_salle).pack(pady=5)



        self.cadreList = ctk.CTkFrame(self, corner_radius=10, width=400)
        self.cadreList.pack(pady=10, padx=10, fill="both", expand=True)

        self.treeList = ttk.Treeview(
            self.cadreList,
            columns=("code", "description", "categorie", "capacite"),
            show="headings"
        )


        self.treeList.heading("code", text="CODE")
        self.treeList.heading("description", text="Description")
        self.treeList.heading("categorie", text="Catégorie")
        self.treeList.heading("capacite", text="Capacité")


        self.treeList.column("code", width=50)
        self.treeList.column("description", width=150)
        self.treeList.column("categorie", width=100)
        self.treeList.column("capacite", width=100)

        self.treeList.pack(expand=True, fill="both", padx=10, pady=10)


        self.lister_salles()


    def ajouter_salle(self):
        salle = Salle(
            self.entry_code.get(),
            self.entry_desc.get(),
            self.entry_cat.get(),
            int(self.entry_cap.get())
        )

        self.service_salle.ajouter_salle(salle)
        self.lister_salles()


    def modifier_salle(self):
        salle = Salle(
            self.entry_code.get(),
            self.entry_desc.get(),
            self.entry_cat.get(),
            int(self.entry_cap.get())
        )

        self.service_salle.modifier_salle(salle)
        self.lister_salles()


    def supprimer_salle(self):
        self.service_salle.supprimer_salle(self.entry_code.get())
        self.lister_salles()

    def rechercher_salle(self):
        salle = self.service_salle.rechercher_salle(self.entry_code.get())

        if salle:
            self.entry_desc.delete(0, "end")
            self.entry_desc.insert(0, salle.description)

            self.entry_cat.delete(0, "end")
            self.entry_cat.insert(0, salle.categorie)

            self.entry_cap.delete(0, "end")
            self.entry_cap.insert(0, salle.capacite)


    def lister_salles(self):

        self.treeList.delete(*self.treeList.get_children())


        liste = self.service_salle.recuperer_salles()

        for s in liste:
            self.treeList.insert("", "end", values=(s.code, s.description, s.categorie, s.capacite))