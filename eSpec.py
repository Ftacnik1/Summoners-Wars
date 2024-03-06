from kresleni import *
def stahni(Sachovnice,smer,kdo):
    zved=0
    chyba =0
    done=False
    Sachovnice=odznaceni(Sachovnice)
    infopanel=list()
    infopanel=pridejdopanelu(infopanel,"V teto fazi muzete valecniky(B) stahnout ke zdi. Stisknete vybranou kartu a pak ji umistete na pole vyznacene pol")
    infopanel=pridejdopanelu(infopanel,"Pro ukonceni faze zmacknete O")
    novapoz(Sachovnice,infopanel)
    while not done:
        elist=pozadi()                                   
        for event in elist:
            try:
                if event.type == pygame.KEYDOWN and ((event.key)==111) and zved==0: 
                    done=True

                elif event.type == pygame.KEYDOWN and ((event.key)==111) and zved==1: 
                    odznaceni(Sachovnice)
                    zved=0
                    novapoz(Sachovnice,infopanel)

                elif event.type == (pygame.MOUSEBUTTONDOWN or pygame.KEYDOWN) and zved==0:
                    prozprom=0
                    a=list(event.pos)
                    x = a[0]
                    y= a[1]
                    pozx=(x//(720//pocetSloupcu))
                    pozy=(y//(480//pocetRad))
                    if x>720 or y>480:
                        chyba=1
                    else:
                        chyba=0
                    if chyba==0:
                        if (type(Sachovnice[pozx][pozy])!=int):
                            if  (Sachovnice[pozx][pozy].smer==smer)and(Sachovnice[pozx][pozy].cislo==kdo):
                                zved=1
                                prozprom=Sachovnice[pozx][pozy]
                                panel=pridejdopanelu(infopanel+[],"Vybranou jednotku nyni muzete umistit ke zdi.")
                                pohybprom=1
                                zedx=-1
                                for i in Sachovnice:
                                    zedx+=1
                                    zedy=-1
                                    for j in i:
                                        zedy+=1
                                        if type(j)!=int:
                                            if j.smer==smer and j.cislo==4:   
                                                if zedx>0:
                                                    Sachovnice[zedx-1][zedy]=1 if(Sachovnice[zedx-1][zedy]==0) else  Sachovnice[zedx-1][zedy]
                        
                                                if zedx<pocetSloupcu-1:
                                                    Sachovnice[zedx+1][zedy]=1 if(Sachovnice[zedx+1][zedy]==0) else  Sachovnice[zedx+1][zedy]

                                                if zedy>0:
                                                    Sachovnice[zedx][zedy-1]=1 if(Sachovnice[zedx][zedy-1]==0) else  Sachovnice[zedx][zedy-1]

                                                if zedy<pocetRad-1:
                                                    Sachovnice[zedx][zedy+1]=1 if(Sachovnice[zedx][zedy+1]==0) else  Sachovnice[zedx][zedy+1]
                                novapoz(Sachovnice,panel)
                                zved=1
                                prozprom=Sachovnice[pozx][pozy]

       

                elif(event.type == (pygame.MOUSEBUTTONDOWN or pygame.KEYDOWN)) and zved==1:
                    b=list(event.pos)
                    c = b[0]
                    d = b[1]
                    pozc=(c//(720//pocetSloupcu))
                    pozd=(d//(480//pocetRad))
                    if Sachovnice[pozc][pozd]==1:
                        Sachovnice[pozc][pozd]=Sachovnice[pozx][pozy]
                        Sachovnice[pozx][pozy]=0
                        odznaceni(Sachovnice)
                        zved=0
                        novapoz(Sachovnice,infopanel)
                        print(event.type)
            except:
                continue