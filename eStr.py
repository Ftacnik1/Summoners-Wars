from eVal import EVal
class EStraz():
    cena=2
    def __init__(self,vyv):
        super().__init__()
        vyv.voj.append(self)
        self.utok=1
        self.zivoty=2
        self.typ="S"
        self.cislo=2
        
    def utok(self,enemy):
        print("presny zasah")
        enemy.zivoty-=self.zivoty


