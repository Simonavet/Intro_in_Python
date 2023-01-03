class Angajat:
    def __init__(self, numeAngajat, functie, varsta):
        self.numeAngajat = numeAngajat
        self.functie = functie
        self.varsta = varsta
        self.salar = 5000
        print('Angajatul este', self.numeAngajat, 'cu functia de', self.functie, 'in varsta de', self.varsta, 'ani')
    def angajare(self):
        print('Angajat nou', self.numeAngajat)
        print('In varsta de', self.varsta)
        print('Cu functia de', self.functie)
    def stabilireSalar(self, vechime):
        if vechime < 5:
            print('Salarul este de', self.salar)
        elif vechime <= 10:
            print('Salarul este de', (self.salar + 500))
        else:
            print('Salarul este de', (self.salar + 700))

