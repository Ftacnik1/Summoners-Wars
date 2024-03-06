from kresleni import *
def poloz(Sachovnice,co,vyv):
    zved=0
    chyba =0
    done=False
    zedx=-1
    for i in Sachovnice:
        zedx+=1
        zedy=-1
        for j in i:
            zedy+=1
            if type(j)!=int:
                if j.smer==vyv.smer and j.cislo==4:    
                    if zedx>0:
                        Sachovnice[zedx-1][zedy]=1 if(Sachovnice[zedx-1][zedy]==0) else  Sachovnice[zedx-1][zedy]
                        
                    if zedx<pocetSloupcu-1:
                        Sachovnice[zedx+1][zedy]=1 if(Sachovnice[zedx+1][zedy]==0) else  Sachovnice[zedx+1][zedy]

                    if zedy>0:
                        Sachovnice[zedx][zedy-1]=1 if(Sachovnice[zedx][zedy-1]==0) else  Sachovnice[zedx][zedy-1]

                    if zedy<pocetRad-1:
                        Sachovnice[zedx][zedy+1]=1 if(Sachovnice[zedx][zedy+1]==0) else  Sachovnice[zedx][zedy+1]  
    panel=list()
    panel=pridejdopanelu(panel,"Na policka na kterych je napis pol muzete polozit vasi kartu. ")
    while done==False:
        
        novapoz(Sachovnice, panel)
        elist=pozadi()                                     
        for event in elist:
            try:
                if event.type == pygame.KEYDOWN and ((event.key)==111): 
                    odznaceni(Sachovnice)
                    done=True
                    co.vyv.balicekMagicky+=co.cena
                    co.vyv.balicekRuka.append(co.cislo)

                elif event.type == (pygame.MOUSEBUTTONDOWN or pygame.KEYDOWN) and zved==0:
                    a=list(event.pos)
                    x = a[0]
                    y= a[1]
                    print(event)
                    pozx=(x//(720//pocetSloupcu))
                    pozy=(y//(480//pocetRad))
                    if x>720 or y>480:
                        chyba=1
                    else:
                        chyba=0
                    if chyba!=1:
                        if Sachovnice[pozx][pozy]==1:
                            zved=1
                            Sachovnice[pozx][pozy]=co
                            odznaceni(Sachovnice)
                            done=True
            except:
                continue

def zed(Sachovnice,co,vyv):
    zved=0
    chyba =0
    done=False
    zedx=-1
    for i in Sachovnice:
        zedx+=1
        zedy=-1
        for j in i:
            zedy+=1
            if type(j)==int:
                if vyv.smer==1:
                    if zedy<4:
                        Sachovnice[zedx][zedy]=1
                else:
                    if zedy>3:
                        Sachovnice[zedx][zedy]=1  
    panel=list()
    panel=pridejdopanelu(panel,"Na policka na kterych je napis pol muzete polozit vasi zed. ")
    while done==False:
        novapoz(Sachovnice, panel)                                     
        elist=pozadi()                                     
        for event in elist:
            try:
                if event.type == pygame.KEYDOWN and ((event.key)==111): 
                    done=True
                    odznaceni(Sachovnice)
                    co.vyv.balicekRuka.append(co.cislo)

                elif event.type == (pygame.MOUSEBUTTONDOWN or pygame.KEYDOWN) and zved==0:
                    a=list(event.pos)
                    x = a[0]
                    y= a[1]
                    pozx=(x//(720//pocetSloupcu))
                    pozy=(y//(480//pocetRad))
                    if x>720 or y>480:
                        chyba=1
                    else:
                        chyba=0
                    if chyba!=1:
                        if Sachovnice[pozx][pozy]==1:
                            zved=1
                            Sachovnice[pozx][pozy]=co
                            print("Jednotka polozena")
                            odznaceni(Sachovnice)
                            done=True
            except:
                continue

def pohyb(Sachovnice,vyv):
    zved=0
    chyba =0
    done=False
    pocitadlo=3
    infopanel=list()
    infopanel=pridejdopanelu(infopanel,"Klinete na jednotku kterou chcete pohybovat.")
    infopanel=pridejdopanelu(infopanel,"Jednotkou je mozne udelat az dva pohyby za fazi.")
    infopanel=pridejdopanelu(infopanel,"Pro ukonceni faze stisknete klavesu O")
    novapoz(Sachovnice,infopanel)
    Sachovnice=odznaceni(Sachovnice)
    while not done:
        elist=pozadi()                                     
        for event in elist:
            try:
                if event.type == pygame.KEYDOWN and ((event.key)==111) and zved==0: 
                    done=True

                elif event.type == pygame.KEYDOWN and ((event.key)==111) and zved==1: 
                        odznaceni(Sachovnice)
                        novapoz(Sachovnice,infopanel)
                        zved=0               
            
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
                        panel=list()
                        if (type(Sachovnice[pozx][pozy])!=int):
                            if  ((Sachovnice[pozx][pozy].smer==vyv.smer)and(Sachovnice[pozx][pozy].chuze>0) and ((pocitadlo>0)or Sachovnice[pozx][pozy].chuze==1 )):
                                zved=1
                                prozprom=Sachovnice[pozx][pozy]
                                panel=pridejdopanelu(infopanel+[],"Vybranou jednotkou se nyni muzete posunout na pole, oznacene pol")
                                pohybprom=1
                                if(pozx)%pocetSloupcu!=pocetSloupcu-1:
                                    if type(Sachovnice[pozx+1][pozy])==int:
                                        Sachovnice[pozx+1][pozy]=1
                                if(pozx)%pocetSloupcu!=0:
                                    if type(Sachovnice[pozx-1][pozy])==int:
                                        Sachovnice[pozx-1][pozy]=1
                                if (pozy)%pocetRad!=pocetRad-1:
                                    if type(Sachovnice[pozx][pozy+1])==int:
                                        Sachovnice[pozx][pozy+1]=1
                                if (pozy)%pocetRad!=0:
                                    if type(Sachovnice[pozx][pozy-1])==int:
                                        Sachovnice[pozx][pozy-1]=1
                                novapoz(Sachovnice,panel)
                                zved=1
                                prozprom=Sachovnice[pozx][pozy]

       
                
                elif event.type == (pygame.MOUSEBUTTONDOWN or pygame.KEYDOWN) and zved==1:
                    b=list(event.pos)
                    c = b[0]
                    d = b[1]
                    pozc=(c//(720//pocetSloupcu))
                    pozd=(d//(480//pocetRad))
                    if Sachovnice[pozc][pozd]==1:
                        if Sachovnice[pozx][pozy].chuze==2:
                            pocitadlo-=1
                        Sachovnice[pozx][pozy].chuze-=1
                        Sachovnice[pozc][pozd]=Sachovnice[pozx][pozy]
                        Sachovnice[pozx][pozy]=0
                        odznaceni(Sachovnice)
                        novapoz(Sachovnice,infopanel)
                        zved=0
            except:
                continue
                         
                
        

                                
                        
                    
            
                
        
            
def utok(tah, Sachovnice):
    zved=0
    chyba =0
    done=False
    pocitadlo=3
    infopanel=list()
    infopanel=pridejdopanelu(infopanel,"V utocne fazi muzete zautocit az tremi jednotkami. Kliknete na jednotku, kterou chcete zautocit a pak kliknete na jednotku, kterou chcete napadnout. Pro ukonceni faze zmacknete O.")
    novapoz(Sachovnice,infopanel)
    while not done:
        elist=pozadi()                                     
        for event in elist:
            try:
                if pocitadlo==0:
                    done=True
            
                elif event.type == pygame.KEYDOWN and ((event.key)==111) and zved==0: 
                    done=True

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
                        if (type(Sachovnice[pozx][pozy]))!=int:
                            if  ((Sachovnice[pozx][pozy].smer==tah)and(Sachovnice[pozx][pozy].moznostUtoku>0)):
                                zved=1
                                panel=pridejdopanelu(infopanel+[],"Jednotka kterou chcete utocit byla vybrana.")
                                novapoz(Sachovnice,panel)

       
                elif (event.type == pygame.KEYDOWN and ((event.key)==111)) and zved==1:
                    zved=0
                    novapoz(Sachovnice,infopanel)

                elif event.type == (pygame.MOUSEBUTTONDOWN or pygame.KEYDOWN) and zved==1:
                    b=list(event.pos)
                    c = b[0]
                    d = b[1]

                    pozc=c//(720//pocetSloupcu)
                    pozd=(d//(480//pocetRad))
                    if type(Sachovnice[pozc][pozd])==int:
                        pozc=pozc
                    elif (Sachovnice[pozc][pozd].smer!=tah)and(((pozc+1+Sachovnice[pozx][pozy].strelba>pozx)and(pozc<pozx)and(pozy==pozd)) or ((pozc-1-Sachovnice[pozx][pozy].strelba<pozx)and(pozc>pozx)and(pozy==pozd)) or ((pozd-1-Sachovnice[pozx][pozy].strelba<pozy)and(pozd>pozy)and(pozx==pozc)) or ((pozd+1+Sachovnice[pozx][pozy].strelba>pozy)and(pozd<pozy)and(pozx==pozc))):
                        Sachovnice[pozx][pozy].moznostUtoku-=1
                        pocitadlo-=1
                        prezil=Sachovnice[pozx][pozy].boj(Sachovnice[pozc][pozd])
                        if prezil==0:
                            Sachovnice[pozc][pozd]=0
                    
                        odznaceni(Sachovnice)
                        zved=0
                        panel=list()
                        panel=pridejdopanelu(infopanel+[],"Vas utok byl proveden")
                        novapoz(Sachovnice,panel)
            except:
                continue