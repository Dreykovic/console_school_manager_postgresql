from controller import Controller


class PersonneController(Controller):
    @classmethod
    def editer_nom(cls):
        value = cls.write_text("nom")
        cls.model.update_nom(cls.write_number("matricule"), value)

    @classmethod
    def editer_prenom(cls):
        value = cls.write_text("prenom")
        cls.model.update_prenoms(cls.write_number("matricule"), value)

    @classmethod
    def editer_date_naissance(cls):
        value = cls.write_date("date de naissance")
        cls.model.update_date_naissance(cls.write_number("matricule"), value)

    @classmethod
    def editer_contact(cls):
        value = cls.write_phone_number("contact")
        cls.model.update_contact(cls.write_number("matricule"), value)

    @classmethod
    def editer_genre(cls):
        value = Controller.write_gender()
        cls.model.update_genre(cls.write_number("matricule"), value)

    @classmethod
    def editer_adresse(cls):
        value = cls.write_text("adresse")
        cls.model.update_adresse(cls.write_number("matricule"), value)


