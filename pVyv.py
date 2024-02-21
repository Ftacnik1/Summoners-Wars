from pVal import PVal
from karty import *
class PVyvolavac:
    def __init__(self,smer,map):
        self.voj=[self]      
        self.balicekVoj=self.balik()
        self.balicekRuka=list()
        self.balicekMagicky=5

        self.slovnik={1: '1-Valecnik(2 utok, 1 zivot, cena 1)', 2: '2-Straz(1 utok(presny), 2 zivot, cena 2)',}
        self.chuze=0
        self.strelba=0
        self.utok=0
        self.zivoty=12
        self.typ="V"
        self.cislo=7
        self.smer=smer
        self.rodic=map
        self.moznostUtoku=1
        
        self.mapa=[[0,self.vyvolej(1),0,0],[0,0,self.vyvolej(1),0],[self,0,self.vyvolej(1),0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.otoc(smer)
        
    def otoc(self,smer):
        if smer!=1:
            nlist=[]
            for i in reversed(self.mapa):
                alist=[]
                promenaA=4
                for j in reversed(i):
                    alist.append(j)
                nlist.append(alist)
            self.mapa=nlist
                
                
                    
            
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
            self.balicekMagicky+=1
            return(0)
        else:
            return(1)
        
    def start(self):
        domich(self)

    def vyvolaniJednotek(self):
        nakup(self,self.rodic)
        """Fce je v souboru karty"""



        

    def rechuz(self):
        for i in self.voj:
            if i.cislo!="7":
                if i.chuze<1:
                    i.chuze+=2
                elif i.chuze==1:
                    i=2

    def reboj(self):
        for i in self.voj:
            if i.cislo!="7":
                if i.moznostUtoku<1:
                    i.moznostUtoku+=1
                elif i.moznostUtoku==1:
                    i=i

    def spec(self):
        a=1
    
    
    def konecTahu(self):
        self.rechuz()
        self.reboj()

    def vyvolej(self, cislo):
        return((PVal(self)) if cislo==1 else (PVal(self)) )
    
    def ocen(self,cislo):
        return((EVal.cena) if cislo==1 else (EStraz.cena) if cislo==2 else (ELuc.cena)if cislo==3 else (Zed.cena) if cislo==4 else (EHrdJed.cena) if cislo==5 else (EHrdJed.cena))

    def balik(self):
        balicek=list()
        for i in range(6):
            balicek.append(1)
            balicek.append(2)
            balicek.append(3)
        for i in range(4):
            balicek.append(4)
        balicek.append(5)
        return(balicek)
    
    def zemri(self):
        print("Hra konci vyvolavac je mrtev")
        self.rodic.np()
        while True:
            continue



    

            
        
