from controller import Controller


class PersonneController(Controller):
    def editer_profession(cls):
        attr = ["matricule", "nom","prenoms","adresse","profession"]
        data = cls.show_attr_of(Tuteur, attr)
        matricule = cls.write_number("matricule")
        print("Etes vous sur de vouloir mettre à jour les donnée du tuteur  :")
        while not cls.show_attr_where_id(Tuteur, attr, matricule, data):
                matricule = cls.write_number("matricule")
        print("?")
        Tuteur.update_profession(matricule, cls.write_text("profession"))
    @classmethod
    def editer_nom(cls):
        attr = ["matricule", "nom","prenoms","adresse"]
        data = cls.show_attr_of(cls.model, attr)
        matricule = cls.write_number("matricule")
        print("Etes vous sur de vouloir mettre à jour les donnée du tuteur  :")
        while not cls.show_attr_where_id(Tuteur, attr, matricule, data):
                matricule = cls.write_number("matricule")
        print("?")
        cls.model.update_nom(matricule, cls.write_text("nom"))

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


