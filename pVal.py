import random
kostka=[1,2,3,4,5,6]
class PVal():
    cena=1
    def __init__(self,vyv):
        self.vyv=vyv
        vyv.voj.append(self)
        self.strelba=1
        self.chuze=2
        self.utok=2
        self.moznostUtoku=1
        self.zivoty=1
        self.typ="B"
        self.cislo=1
        self.smer=vyv.smer
        
    def boj(self,enemy):
        for i in range(self.utok):
            if enemy.zivoty>0:               
                if random.choice(kostka)>2:
                    enemy.zivoty-=1
                    print("Zasah")
                else:
                    print("Minul")
        if  enemy.zivoty<1:
            enemy.zemri()
            self.vyv.balicekMagicky+=1
            return(0)
        else:
            return(1)

    def zemri(self):
        self.vyv.voj.remove(self)
        
        
    
