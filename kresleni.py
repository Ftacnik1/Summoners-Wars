import pygame
import random
import os
import webbrowser
import sys
# Initialize the game engine
pygame.init()
pygame.mixer.init()
kostka=[1,2,3,4,5,6]
BLACK    = (   0,   0,   0)
BLUE    = (   0,   0,   255)
RED = (   255,   0,   0)
WHITE    = ( 255, 255, 255)
GRAY   = ( 127, 127, 127)
LBLUE =(173, 216, 230)

zvuk=1
pygame.mixer.music.load('music3.mp3')
"""nekonecna smicka"""
pygame.mixer.music.play(-1)  



pocetRad=8
posunRad=480/pocetRad
pocetSloupcu=6
posunSloupcu=(720/pocetSloupcu)

PI = 3.141592653
size = (1025, 540)
screen = pygame.display.set_mode(size)
help = pygame.image.load('help.jpg')
help = pygame.transform.scale(help, (40, 40))
sound = pygame.image.load('sound.jpg')
sound = pygame.transform.scale(sound, (40, 40))
skip = pygame.image.load('skip.jpg')
skip = pygame.transform.scale(skip, (80, 40))


"""Navod"""
# Get the current directory of the Python script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Path to your HTML file (assuming it's named 'example.html')
html_file_path = os.path.join(current_dir, 'SWnavod.html')



"""Jmeno okna"""
pygame.display.set_caption("Valky vyvolavacu")
done = False
screen.fill(WHITE)
def odznaceni(Sachovnice):
    for j in range(len((Sachovnice))):
        for i in range(len(Sachovnice[j])):
            if Sachovnice[j][i]==1:
                Sachovnice[j][i]=0
    return(Sachovnice)
def colour(pozice):
    print(pozice)
    if pozice[0]==0:
        barva=RED
    else:
        barva=BLUE
    return(barva)

def pridejdopanelu(panel,text):
    pocitadlo=0
    kus=""
    slovo=""
    delka=44
    for i in text:
        pocitadlo+=1
        slovo+=i
        if ord(i)==32:
            if pocitadlo>delka:
                pocitadlo-=len(kus)
                panel.append(kus)
                kus=""
            kus+=slovo
            slovo=""
    if len(kus)+len(slovo)>delka:
        panel.append(kus)
        panel.append(slovo)
    else:
        kus+=slovo
        panel.append(kus)
    return(panel)





def pozadi():
    elist=list()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == (pygame.MOUSEBUTTONDOWN or pygame.KEYDOWN):
            a=list(pygame.mouse.get_pos())
            x = a[0]
            y= a[1]
            if x>970 and 1010>x:
                if y>490 and 530>y:
                    webbrowser.open_new_tab('file://' + html_file_path)

            elif 41>x:
                if y>490 and 530>y:
                    global zvuk
                    if zvuk==0:
                        pygame.mixer.music.set_volume(1.0)
                        zvuk=1
                    else:
                        pygame.mixer.music.set_volume(0.0)
                        zvuk=0
            elif x>465 and 545>x:
                if y>490 and 530>y:
                    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_o, 'mod': 0}))

        elist.append(event)
    try:
        return(elist+[])
    except:
        return(None)


def vyvolaniterminal(ruka,vyv,mapA):
    Moznost=1
    done=False
    while not done:
            panel=list()
            panel=pridejdopanelu(panel,str(f"Pocet karet v magickem balicku: {vyv.balicekMagicky}"))
            for i in (ruka):
                panel=pridejdopanelu(panel,str(vyv.slovnik[i]))
            panel=pridejdopanelu(panel,"Zmacknete cislo karty, kterou chcete vyvolat")
            Moznost=11
            while(Moznost>8):
                novapoz(mapA.mapa,panel)
                elist=pozadi()                                     
                for event in elist:
                    try:
                        if (event.type == pygame.KEYDOWN and ((event.key)==111)):
                            Moznost=0
                            break 
                        else:  
                            asciicislo=event.key
                            Moznost=int(chr(asciicislo))

                    except:
                        Moznost=11
                       
                  
            if Moznost in ruka:
                  if vyv.balicekMagicky<vyv.ocen(Moznost):
                        panel=pridejdopanelu(panel,"Nedostatek penez v magickem balicku")
                  else: 
                        vyv.balicekMagicky-=vyv.ocen(Moznost)
                        if Moznost!=4:
                              mapA.VyvolejMapa(vyv.vyvolej(Moznost),vyv)
                        else:
                              mapA.VyvolejZed(vyv.vyvolej(Moznost),vyv)
                        vyv.balicekRuka.remove(Moznost)
            if Moznost==0:
                done=True
                              
def odhazovaniterminal(ruka,vyv,mapA):
    Moznost=1
    done=False
    while not done:
            panel=list()
            panel=pridejdopanelu(panel,str(f"Pocet karet v magickem balicku: {vyv.balicekMagicky}"))
            for i in (ruka):
                panel=pridejdopanelu(panel,str(vyv.slovnik[i]))
            panel=pridejdopanelu(panel,"Zmacknete cislo karty, kterou chcete odhodit")
            Moznost=11
            while(Moznost>8):
                novapoz(mapA.mapa,panel)
                elist=pozadi()                                     
                for event in elist:
                    try:
                        if event.type == pygame.KEYDOWN and((event.key)==111):
                            Moznost=0
                            break 
                        elif event.type == pygame.KEYDOWN:
                            asciicislo=event.key
                            Moznost=int(chr(asciicislo))
                            break

                    except:
                        Moznost=11
                       
                  
            if Moznost in ruka:
                vyv.balicekRuka.remove(Moznost)
                vyv.balicekMagicky+=1

            if Moznost==0:
                done=True
                              

def start():
    Odpoved=""
    screen.fill(BLACK)
    font=pygame.font.Font("freesansbold.ttf",30)
    text=font.render("1 Elf, 2 Orc,3 pocitac rychly: ", True, BLUE, )
    textRect= text.get_rect()
    textRect.center=(360, 240)
    screen.blit(text,textRect)
    pygame.display.flip()
    while Odpoved not in [0,1,2,3]:
        elist=pozadi()                                     
        for event in elist:
            try:
                if (event.type == pygame.KEYDOWN):
                    asciicislo=event.key
                    Odpoved=int(chr(asciicislo))
            except: 
                continue
    x=Odpoved
    Odpoved=""
    screen.fill(BLACK)
    font=pygame.font.Font("freesansbold.ttf",30)
    text=font.render("1 Elf, 2 Orc,3 pocitac pomaly: ", True, BLUE, )
    textRect= text.get_rect()
    textRect.center=(360, 240)
    screen.blit(text,textRect)
    pygame.display.flip()
    while Odpoved not in [0,1,2,3]:
        elist=pozadi()                                     
        for event in elist:
            try:
                if (event.type == pygame.KEYDOWN):
                    asciicislo=event.key
                    Odpoved=int(chr(asciicislo))
            except: 
                continue
    return(x,Odpoved)

def novapoz(Sachovnice,obsah):
    global help
    screen.fill(WHITE)
    x=30-(posunSloupcu)
    y=30
    barva=BLACK
    for i in range(pocetSloupcu):
        x+=posunSloupcu
        for j in range(pocetRad):
            if type(Sachovnice[i][j])==int: 
                pygame.draw.rect(screen, barva, [int(x-30),int(y-30),posunSloupcu,posunRad])
            y+=posunRad
            if (barva==WHITE):
                barva=BLACK
            else:
                barva=WHITE
            if type(Sachovnice[i][j])!=int:
                pozadikarty = Sachovnice[i][j].vyv.pozadi
                pozadikarty = pygame.transform.scale(pozadikarty, (posunSloupcu, posunRad))
                if Sachovnice[i][j].vyv.smer==1:
                    pozadikarty = pygame.transform.rotate(pozadikarty, 180)
                screen.blit(pozadikarty, (x-30, y-posunRad-30))

        y=30
        if (barva==WHITE and pocetRad%2==1) or (barva==BLACK and pocetRad%2==0):
            barva=WHITE
        else:
            barva=BLACK
    pygame.draw.line(screen,BLACK, [0,0],[720,0],2)
    pygame.draw.line(screen,BLACK, [720,0],[720,480],2)
    pygame.draw.line(screen,BLACK, [720,480],[0,480],2)
    pygame.draw.line(screen,BLACK, [0,480],[0,0],2)
    proma=-1

    kresx=0
    for i in Sachovnice:
        kresx+=1

        kresy=0
        for j in i:
            kresy+=1
            if j!=0:
                font=pygame.font.Font("freesansbold.ttf",int(posunRad//2))
                if j==1:
                    text=font.render("Pol", True, GRAY, )
                    textRect= text.get_rect()
                    textRect.center=((kresx*posunSloupcu)-posunSloupcu/2,(kresy*posunRad)-posunRad/2)
                    screen.blit(text,textRect)
                elif type(j)!=int:
                    font=pygame.font.Font("gothicfont.ttf",int((posunRad//5)*4))
                    slovo=(f"{j.typ}{j.zivoty},{j.utok}")
                    barva=RED if j.smer==1 else BLUE
                    text=font.render(slovo, True, barva, )
                    textRect= text.get_rect()
                    textRect.center=((kresx*posunSloupcu)-posunSloupcu/2,(kresy*posunRad)-posunRad/2)
                    screen.blit(text,textRect)

        """Tvorba okna pro komunikaci"""
    pygame.draw.rect(screen, LBLUE, [int(735),int(0),275,480])
    kde=0
    global panelsoucobsah
    panelsoucobsah=obsah
    for i in obsah:
        kde+=40
        font=pygame.font.SysFont("Calibri", 15)
        text=font.render(i, BLACK, BLACK, )
        textRect= pygame.Rect(int(735),kde,275,kde+30)
        textRect.center=(872,kde)
        screen.blit(text,textRect)

        """Napoveda"""
    screen.blit(help, (970, 490))
    screen.blit(sound, (0, 490))
    screen.blit(skip, (465, 490))

    pygame.display.flip()
    
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
                    a=list(pygame.mouse.get_pos())
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
                    a=list(pygame.mouse.get_pos())
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
                    a=list(pygame.mouse.get_pos())
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
                    b=list(pygame.mouse.get_pos())
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
                         
                
        
            
def pohybzla(Sachovnice,vyv):
    chyba =0
    x=-1
    for i in Sachovnice:
        x+=1
        y=-1
        for j in i:
            y+=1
            if type((Sachovnice[x][y]))!=int:
                if Sachovnice[x][y].smer==vyv.smer and Sachovnice[x][y].chuze>0:
                    if (vyv.smer==1 and y==7) or (vyv.smer==-1 and y==0):
                        Sachovnice[x][y].zemri()
                        Sachovnice[x][y]=0

                        
                    else:
                        if type(Sachovnice[x][y+(Sachovnice[x][y].smer)])==int and(Sachovnice[x][y].cislo)!=7 :
                            Sachovnice[x][y].chuze-=1
                            Sachovnice[x][y+(Sachovnice[x][y].smer)]=Sachovnice[x][y]
                            Sachovnice[x][y]=0

def utokzla(Sachovnice,vyv):
    x=-1
    for i in Sachovnice:
        x+=1
        y=-1
        for j in i:
            y+=1
            if type(Sachovnice[x][y])!=int:
                if Sachovnice[x][y].smer==vyv.smer and Sachovnice[x][y].utok>0:
                    if type(Sachovnice[x][y+(Sachovnice[x][y].smer)])!=int:
                        if  Sachovnice[x][y+(Sachovnice[x][y].smer)].smer!=vyv.smer:
                            prezil=Sachovnice[x][y].boj(Sachovnice[x][y+(Sachovnice[x][y].smer)])
                            if prezil==0:
                                Sachovnice[x][y+(Sachovnice[x][y].smer)]=0


def vyvzla(Sachovnice, vyv):
    if vyv.smer==1:
        y=0
    else:
        y=7
    for i in range (pocetSloupcu):
        if type(Sachovnice[i][y])==int:
            Sachovnice[i][y]= vyv.vyvolej(1)

                                
                        
                    
            
                
        
            
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
                    a=list(pygame.mouse.get_pos())
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
                    b=list(pygame.mouse.get_pos())
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
                    a=list(pygame.mouse.get_pos())
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

       
                
                elif event.type == (pygame.MOUSEBUTTONDOWN or pygame.KEYDOWN) and zved==1:
                    b=list(pygame.mouse.get_pos())
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
            except:
                continue
                          
                
        
        
