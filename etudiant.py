#!/bin/python3


import datetime as dt
from connexion import Connexion
# from orm import Linker


class Etudiant(Linker):
    def __init__(self, connexion, nom=None, prenom=None, date_naissance=None, contact=None, genre=None, adresse=None, classe=None, tuteur=None):
        # Linker.__init__(self, connexion, 'eleve')
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.contact = contact
        self.table = "eleve"
        self.genre = genre
        self.adresse = adresse
        self.classe = classe
        self.tuteur = tuteur
    
    def column_names(self):
        return [self.adresse, self.contact, self.classe, self.date_naissance, self.genre, self.nom, self.prenom]
