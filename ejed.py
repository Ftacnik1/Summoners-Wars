from eVal import EVal
class EStraz(EVal):
    cena=2
    def __init__(self,vyv):
        super().__init__(vyv)
        self.utok=1
        self.zivoty=2
        self.typ="A"
        self.cislo=2
        
    def boj(self,enemy):
        print("presny zasah")
        enemy.zivoty-=1
        if  enemy.zivoty<1:
            enemy.zemri()
            self.vyv.balicekMagicky+=1
            return(0)
        else:
            return(1)

import random
kostka=[1,2,3,4,5,6]
class EHrdJed(EVal):
    cena=5
    def __init__(self,vyv):
        super().__init__(vyv)
        self.chuze=2
        self.utok=2
        self.zivoty=5
        self.typ="H"
        self.cislo=5

    def boj(self,enemy):
        enemy.zivoty-=1
        for i in range(self.utok):
            if enemy.zivoty>0:               
                if random.choice(kostka)>4:
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

class ELuc(EVal):
    cena=1
    def __init__(self,vyv):
        super().__init__(vyv)
        self.strelba=4
        self.utok=1
        self.zivoty=1
        self.typ="C"
        self.cislo=3

class Zed():
    cena=0
    def __init__(self,vyv):
        vyv.voj.append(self)
        self.strelba=False
        self.chuze=0
        self.vyv=vyv
        self.utok=0
        self.zivoty=9
        self.typ="Z"
        self.cislo=4
        self.smer=vyv.smer
        self.moznostUtoku=0
    def zemri(self):
        self.vyv.voj.remove(self)
        