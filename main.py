from eVyv import EVyvolavac
from oVyv import OVyvolavac
from pVyv import PVyvolavac
import kresleni
class Mapa:
    def __init__(self):
        self.tah=0
        self.fazeHry=0
        self.mapa=list()
        kresleni.start()
        odpoved=""
        while odpoved not in [0,1,2,3]:
            odpovedText1="1 Elf, 2 Orc,3 pocitac rychly: "
            try:
                odpoved=int(input(odpovedText1))
            except: 
                odpoved=6
            self.player1=EVyvolavac(1,self)if odpoved==0 else EVyvolavac(1,self)  if odpoved==1 else OVyvolavac(1,self) if odpoved==2 else PVyvolavac(1,self)
        odpoved="A"
        odpovedText2="1 Elf, 2 Orc,3 pocitac pomaly: "
        while odpoved not in [0,1,2,3]:
            try:
                odpoved=int(input(odpovedText2))
            except: 
                odpoved=6
            self.player2=EVyvolavac(-1,self)if odpoved==0 else EVyvolavac(-1,self)  if odpoved==1 else OVyvolavac(-1,self) if odpoved==2 else PVyvolavac(-1,self)
        self.mapa=self.player1.mapa
        for i in range(6):
            for j in range(4):
                self.mapa[i].append(self.player2.mapa[i][j])
        self.tah=self.player1
        while True:
            self.zfaze()
            
    def np(self):
        kresleni.novapoz(self.mapa)


    def zfaze(self):
        kresleni.novapoz(self.mapa)
        self.fazeHry+=1
        if self.fazeHry==1:
            self.tah.start()
        
        elif self.fazeHry==2:
            kresleni.novapoz(self.mapa)
            if self.tah.utok!=0:
                print("V terminalu vyberte jednotku kterou chcete vyvolat.")
                print("Jednotku pak polozte na policko vyznacene pol.")
                self.tah.vyvolaniJednotek()
            else:
                kresleni.vyvzla(self.mapa, self.tah)

        elif self.fazeHry==3:
            zbytecnaPromena=1

        elif self.fazeHry==4:
            print("Pohyb")
            if self.tah.utok!=0:
                print("Klinknete na jednotku kterou chcete hybat.")
                print("Muzete ji posunout na vyznacena pole.")
                kresleni.pohyb(self.mapa,self.tah)
            else:
                kresleni.pohybzla (self.mapa, self.tah)

        elif self.fazeHry==5:
            if self.tah.utok!=0:
                print("Utocna faze zmacknete jednotku kterou utocite a jednotku, kterou chcete napadnout.")
                print("Jednotku kterou pripravite musite pouzit")
                print("Pokud danou jednotkou nemuzete zautocit ukoncete tah - O")
                print("Po trech utocich pokracuje dalsi faze")
                kresleni.utok(self.tah.smer, self.mapa)
            else:
                kresleni.utokzla(self.mapa, self.tah)

        elif self.fazeHry==7:
            self.tah.spec()

        elif self.fazeHry==8:
            self.fazeHry=0
            self.tah.konecTahu()
            self.tah= self.player1 if self.tah==self.player2 else self.player2

    def VyvolejMapa(self,fig,vyv):
        kresleni.poloz(self.mapa,fig,vyv)

    def VyvolejZed(self,fig,vyv):
        kresleni.zed(self.mapa,fig,vyv)


    def stazeni(self,kdo):
        kresleni.stahni(self.mapa,self.tah.smer,kdo)
mapA=Mapa()
while(True):
    zbytecnaPromena=1

            
