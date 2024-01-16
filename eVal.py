import random
kostka=[1,2,3,4,5,6]
class EVal():
    cena=1
    def __init__(self,vyv):
        vyv.voj.append(self)
        self.strelba=1
        self.chuze=2
        self.utok=2
        self.moznostUtoku=1
        self.zivoty=1
        self.typ="B"
        self.cislo=1
        self.smer=vyv.smer
        
    def utok(self,enemy):
        for i in range(self.utok):
            if enemy.zivoty>0:               
                if random.choice(kostka)>4:
                    enemy.zivoty-=1
                    print("Zasah")
                else:
                    print("Minul")
        
    
