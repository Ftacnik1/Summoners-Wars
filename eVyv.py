from ejed import *
from eVal import EVal
from karty import *
class EVyvolavac:
    def __init__(self,smer,map):
        self.voj=[]      
        self.balicekVoj=self.balik()
        self.balicekRuka=list()
        self.balicekMagicky=5

        self.slovnik={1: '1-Valecnik(2 utok, 1 zivot, cena 1)', 2: '2-Straz(1 utok(presny), 2 zivot, cena 2)', 3: '3-Lucistnik(1 utok(4 pole dostrel), 1 zivot, cena 1)'}
        self.chuze=2
        self.utok=2
        self.zivoty=5
        self.typ="V"
        self.cislo=7
        self.smer=smer
        self.rodic=map
        
        self.mapa=[[0,self.vyvolej(1),0,0],[0,0,self.vyvolej(2),0],[self,0,self.vyvolej(4),0],[self.vyvolej(3),0,0,0],[0,0,0,0],[0,self.vyvolej(3),0,0]]
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
        print(self.mapa)
                
                
                    
            
    def utok(self,enemy):
        enemy.zivoty-=self.zivoty

    def start(self):
        domich(self)

    def vyvolaniJednotek(self):
        nakup(self,self.rodic)



        

    def rechuz(self):
        for i in self.voj:
            if i.cislo!="4":
                if i.chuze<1:
                    i.chuze+=2
                elif i.chuze==1:
                    i+=1

    def konecTahu(self):
        self.rechuz()

    def vyvolej(self, cislo):
        return((EVal(self)) if cislo==1 else (EStraz(self)) if cislo==2 else (ELuc(self))if cislo==3 else (Zed(self)) if cislo==4 else (EHrdJed(self)))
    
    def ocen(self,cislo):
        return((EVal.cena) if cislo==1 else (EStraz.cena) if cislo==2 else (ELuc.cena)if cislo==3 else (Zed.cena) if cislo==4 else (EHrdJed.cena))

    def balik(self):
        balicek=list()
        for i in range(6):
            balicek.append(1)
            balicek.append(2)
            balicek.append(3)
        return(balicek)



    

            
        
