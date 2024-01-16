import random
kostka=[1,2,3,4,5,6]
class EHrdJed():
    def __init__(self,vyv):
        vyv.voj.append(self)
        self.strelba=False
        self.chuze=2
        self.utok=2
        self.zivoty=5
        self.typ="H"
        self.cislo=5
        
    def utok(self,enemy):
        for i in range(self.utok):
            if enemy.zivoty>0:               
                if random.choice(kostka)>4:
                    enemy.zivoty-=2
                    print("Zasah")
                else:
                    print("Minul")
