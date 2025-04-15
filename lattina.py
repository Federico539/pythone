class SodaCan:
    def __init__(self, raggio, altezza):
        self.raggio = 5
        self.altezza = 14
    
    def calcolaSuperficie(PI = 3.14, raggio):
        superficie = PI * (raggio ** 2)
        print(superficie)
        
    def calcolaVolume(superficie, altezza):
        volume = superficie * altezza
        print(volume)
    