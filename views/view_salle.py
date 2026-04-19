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

        self.frame_info = ctk.CTkFrame(self)
        self.frame_info.pack(pady=10)

        self.entry_code = ctk.CTkEntry(self.frame_info, placeholder_text="Code")
        self.entry_code.grid(row=0, column=0)

        self.entry_desc = ctk.CTkEntry(self.frame_info, placeholder_text="Description")
        self.entry_desc.grid(row=0, column=1)

        self.entry_cat = ctk.CTkEntry(self.frame_info, placeholder_text="Categorie")
        self.entry_cat.grid(row=0, column=2)

        self.entry_cap = ctk.CTkEntry(self.frame_info, placeholder_text="Capacite")
        self.entry_cap.grid(row=0, column=3)


