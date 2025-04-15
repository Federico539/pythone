class Student:
    def__init__(self, nome, cognome):
        self._nome = nome
        self._cognome = cognome
        self._punteggio = 0.0
        self._numeroQuestionari = 0
        self._totPunteggio = 0
        self._mediaPunteggio = 0
    
    def getName(self):
        self._nome = input("inserisci il nome: ")
        self._cognome = input("inserisci il cognome: ")
        return f'(self._nome) (self._cognome)'
    
    def addQuiz(self, punteggio):
        self._totPunteggio += punteggio
        self._numeroQuestionari += 1
    
    def getAvarageScore(self):
        return self._totPunteggio / self._numeroQuestionari
        