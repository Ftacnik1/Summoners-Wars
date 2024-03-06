from eVyv import EVyvolavac
from oVyv import OVyvolavac
from pVyv import PVyvolavac
import eSpec
import zakladniFazeFce
import pocitactahy
import kartyterminal
import kresleni
class Mapa:
    def __init__(self):
        self.tah=0
        self.fazeHry=0
        self.mapa=list()
        x,y=kresleni.start()
        odpoved=x
        self.player1=EVyvolavac(1,self)if odpoved==0 else EVyvolavac(1,self)  if odpoved==1 else OVyvolavac(1,self) if odpoved==2 else PVyvolavac(1,self)
        odpoved=y
        self.player2=EVyvolavac(-1,self)if odpoved==0 else EVyvolavac(-1,self)  if odpoved==1 else OVyvolavac(-1,self) if odpoved==2 else PVyvolavac(-1,self)
        self.mapa=self.player1.mapa
        for i in range(6):
            for j in range(4):
                self.mapa[i].append(self.player2.mapa[i][j])
        self.tah=self.player1
        print(self.mapa)
        while True:
            self.zfaze()
            
    def np(self):
        panel=list()
        panel=kresleni.pridejdopanelu(panel,"Vyvolavac je mrtev hra konci")
        kresleni.novapoz(self.mapa,panel)
        kresleni.konec()


    def zfaze(self):
        kresleni.novapoz(self.mapa,list())
        self.fazeHry+=1
        if self.fazeHry==1:
            self.tah.start()
        
        elif self.fazeHry==2:
            kresleni.novapoz(self.mapa,list())
            if self.tah.utok!=0:
                print("V terminalu vyberte jednotku kterou chcete vyvolat.")
                print("Jednotku pak polozte na policko vyznacene pol.")
                kartyterminal.vyvolaniterminal(self.tah.balicekRuka,self.tah,self)
            else:
                pocitactahy.vyvzla(self.mapa, self.tah)

        elif self.fazeHry==3:
            zbytecnaPromena=1

        elif self.fazeHry==4:
            print("Pohyb")
            if self.tah.utok!=0:
                print("Klinknete na jednotku kterou chcete hybat.")
                print("Muzete ji posunout na vyznacena pole.")
                zakladniFazeFce.pohyb(self.mapa,self.tah)
            else:
                pocitactahy.pohybzla (self.mapa, self.tah)

        elif self.fazeHry==5:
            if self.tah.utok!=0:
                print("Utocna faze zmacknete jednotku kterou utocite a jednotku, kterou chcete napadnout.")
                print("Jednotku kterou pripravite musite pouzit")
                print("Pokud danou jednotkou nemuzete zautocit ukoncete tah - O")
                print("Po trech utocich pokracuje dalsi faze")
                zakladniFazeFce.utok(self.tah.smer, self.mapa)
            else:
                pocitactahy.utokzla(self.mapa, self.tah)

        elif self.fazeHry==7:
            self.tah.spec()

        elif self.fazeHry==8:
            self.fazeHry=0
            self.tah.konecTahu()
            if self.tah.utok!=0:
                kartyterminal.odhazovaniterminal(self.tah.balicekRuka,self.tah,self)
            self.tah= self.player1 if self.tah==self.player2 else self.player2

    def VyvolejMapa(self,fig,vyv):
        zakladniFazeFce.poloz(self.mapa,fig,vyv)

    def VyvolejZed(self,fig,vyv):
        zakladniFazeFce.zed(self.mapa,fig,vyv)



    def stazeni(self,cislojednotky):
        eSpec.stahni(self.mapa,self.tah.smer,cislojednotky)
mapA=Mapa()
while(True):
    zbytecnaPromena=1

            

