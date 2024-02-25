from ojed import *
from oVal import OVal
from karty import *
import pygame
class OVyvolavac:
    def __init__(self,smer,map):
        self.voj=[self]      
        self.balicekVoj=self.balik()
        self.balicekRuka=list()
        self.balicekMagicky=5

        self.slovnik={1: '1-Bojovnik 2 utok, 1 zivot, cena 1', 2: '2-Hromotluk 2 utok, 4 zivoty, cena 4', 3: '3-Lucistnik 2 utok ,3 pole dostrel, 2 zivoty, cena 1', 4: '4-Zed', 5: '5-Hrdina 2 utok, 5 zivotu, cena 5'}
        self.chuze=2
        self.vyv=self
        self.pozadi = pygame.image.load('Ocard.jpg')
        self.strelba=1
        self.utok=4
        self.zivoty=7
        self.typ="V"
        self.cislo=7
        self.smer=smer
        self.rodic=map
        self.moznostUtoku=1
        
        self.mapa=[[0,0,0,0],[0,0,self.vyvolej(2),0],[0,self.vyvolej(1),0,0],[self,0,self.vyvolej(4),0],[0,self.vyvolej(3),0,0],[0,0,0,self.vyvolej(1)]]
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




        

    def rechuz(self):
        for i in self.voj:
            if i.cislo!="4":
                if i.chuze<1:
                    i.chuze+=2
                elif i.chuze==1:
                    i.chuze+=1

    def reboj(self):
        for i in self.voj:
            if i.cislo!="4":
                if i.moznostUtoku<1:
                    i.moznostUtoku+=1
                elif i.moznostUtoku==1:
                    i=i

    def spec(self):
        pass
    
    
    def konecTahu(self):
        self.rechuz()
        self.reboj()

    def vyvolej(self, cislo):
        return((OVal(self)) if cislo==1 else (OStraz(self)) if cislo==2 else (OLuc(self))if cislo==3 else (Zed(self)) if cislo==4 else (OHrdJed(self)))
    
    def ocen(self,cislo):
        return((OVal.cena) if cislo==1 else (OStraz.cena) if cislo==2 else (OLuc.cena)if cislo==3 else (Zed.cena) if cislo==4 else (OHrdJed.cena))

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
        self.rodic.np()
        while True:
            continue



    

            
        
