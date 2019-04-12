class Application:
    execution=True

    def __init__(self,nom):
        self.nom=nom

    def exec(self):
        i=0
        while self.execution:
            print("{}En cours d'exécution")
            i += 1
            if i > 10:
                self.execution = False
