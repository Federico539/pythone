class Letter:
    def __init__(self, letterFrom, letterTo) :
        self._letterFrom = letterFrom
        self._letterTo = letterTo
        self._line = ""
        
        
    def addLine(self, line):
        self._line += '\n'+line
    
    def getText(self):
        return f'Dear {self._letterTo}:\n' + self._line + f'\nSincerely,\n {self._letterFrom}'
    
        
missiva = Letter("Mary", "John")
missiva.addLine("bla bla bla")
    
print(missiva.getText)