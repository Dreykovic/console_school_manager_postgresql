from modeles.table_tuteur import TableTuteur as Tuteur 
from controller import Controller

class TuteurController(Controller):
    model = Tuteur
    def __init__(self,):
        print(cls.model)

t = TuteurController()
