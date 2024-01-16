from eVyv import EVyvolavac
import kresleni
class Mapa:
    def __init__(self):
        self.tah=0
        self.fazeHry=0
        self.mapa=list()
        odpoved=""
        while odpoved not in [0,1]:
            odpovedText="1 Elf"
            odpoved=int(input(odpovedText))
            self.player1=EVyvolavac(1,self)if odpoved==0 else EVyvolavac(1,self)  if odpoved==1 else EVyvolavac(1,self)
        odpoved="A"
        while odpoved not in [0,1]:
            odpoved=int(input(odpovedText))
            self.player2=EVyvolavac(-1,self)if odpoved==0 else EVyvolavac(-1,self) if odpoved==1 else EVyvolavac(-1,self)
        self.mapa=self.player1.mapa
        for i in range(6):
            for j in range(4):
                self.mapa[i].append(self.player2.mapa[i][j])
        self.tah=self.player1
        while True:
            self.zfaze()
            
            

    def zfaze(self):
        kresleni.novapoz(self.mapa)
        self.fazeHry+=1
        if self.fazeHry==1:
            self.tah.start()
        
        elif self.fazeHry==2:
            self.tah.vyvolaniJednotek()

        elif self.faze==3:
            zbytecnaPromena=1

        elif self.faze==4:
            kresleni.pohyb(self.mapa,vyv)

        if self.fazeHry==8:
            self.fazeHry=0
            self.tah= self.player1 if self.tah==self.player2 else self.player2

    def VyvolejMapa(self,fig,vyv):
        kresleni.poloz(self.mapa,fig,vyv)
mapA=Mapa()
while(True):
    zbytecnaPromena=1

            

