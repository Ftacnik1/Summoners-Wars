import pygame
import random
# Initialize the game engine
pygame.init()
kostka=[1,2,3,4,5,6]
BLACK    = (   0,   0,   0)
BLUE    = (   0,   0,   255)
RED = (   255,   0,   0)
WHITE    = ( 255, 255, 255)
GRAY   = ( 127, 127, 127)

pocetRad=8
posunRad=480/pocetRad
pocetSloupcu=6
posunSloupcu=(720/pocetSloupcu)

PI = 3.141592653
size = (760, 500)
screen = pygame.display.set_mode(size)

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
        barvicka=RED
    else:
        barvicka=BLUE
    return(barvicka)



def start():
    screen.fill(BLACK)
    font=pygame.font.Font("freesansbold.ttf",30)
    text=font.render("SW použijte terminál", True, BLUE, )
    textRect= text.get_rect()
    textRect.center=(360, 240)
    screen.blit(text,textRect)
    pygame.display.flip()

def novapoz(Sachovnice):
    screen.fill(WHITE)
    x=30-(posunSloupcu)
    y=30
    COLOUR=BLACK
    for i in range(pocetSloupcu):
        x+=posunSloupcu
        for j in range(pocetRad):
            pygame.draw.rect(screen, COLOUR, [int(x-30),int(y-30),posunSloupcu,posunRad])
            y+=posunRad
            if (COLOUR==WHITE):
                COLOUR=BLACK
            else:
                COLOUR=WHITE
        y=30
        if (COLOUR==WHITE and pocetRad%2==1) or (COLOUR==BLACK and pocetRad%2==0):
            COLOUR=WHITE
        else:
            COLOUR=BLACK
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
                    slovo=(f"{j.typ},{j.zivoty},{j.utok}")
                    barva=RED if j.smer==1 else BLUE
                    text=font.render(slovo, True, barva, )
                    textRect= text.get_rect()
                    textRect.center=((kresx*posunSloupcu)-posunSloupcu/2,(kresy*posunRad)-posunRad/2)
                    screen.blit(text,textRect)
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
                    print("Zed")    
                    if zedx>0:
                        Sachovnice[zedx-1][zedy]=1 if(Sachovnice[zedx-1][zedy]==0) else  Sachovnice[zedx-1][zedy]
                        
                    if zedx<pocetSloupcu-1:
                        Sachovnice[zedx+1][zedy]=1 if(Sachovnice[zedx+1][zedy]==0) else  Sachovnice[zedx+1][zedy]

                    if zedy>0:
                        Sachovnice[zedx][zedy-1]=1 if(Sachovnice[zedx][zedy-1]==0) else  Sachovnice[zedx][zedy-1]

                    if zedy<pocetRad-1:
                        Sachovnice[zedx][zedy+1]=1 if(Sachovnice[zedx][zedy+1]==0) else  Sachovnice[zedx][zedy+1]  
    
    while done==False:
        novapoz(Sachovnice)                                     
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and ((event.key)==111): 
                odznaceni(Sachovnice)
                done=True

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
                        novapoz(Sachovnice)
                        done=True

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
    
    while done==False:
        novapoz(Sachovnice)                                     
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and ((event.key)==111): 
                done=True
                odznaceni(Sachovnice)

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
                        novapoz(Sachovnice)
                        done=True

def pohyb(Sachovnice,vyv):
    zved=0
    chyba =0
    done=False
    pocitadlo=3
    Sachovnice=odznaceni(Sachovnice)
    print("Zmacknete O pro ukonceni faze")
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("User asked to quit.")
                done=True
            elif event.type == pygame.KEYDOWN and ((event.key)==111): 
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
                    print(type(Sachovnice[pozx]))
                    if (type(Sachovnice[pozx][pozy])!=int):
                        if  ((Sachovnice[pozx][pozy].smer==vyv.smer)and(Sachovnice[pozx][pozy].chuze>0) and ((pocitadlo>0)or Sachovnice[pozx][pozy].chuze==1 )):
                            zved=1
                            prozprom=Sachovnice[pozx][pozy]
                            print("Kamen zvednut")
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
                            novapoz(Sachovnice)
                            zved=1
                            prozprom=Sachovnice[pozx][pozy]

       
                
            elif event.type == (pygame.MOUSEBUTTONDOWN or pygame.KEYDOWN) and zved==1:
                b=list(pygame.mouse.get_pos())
                c = b[0]
                d = b[1]
                pozc=(c//(720//pocetSloupcu))
                pozd=(d//(480//pocetRad))
                if Sachovnice[pozc][pozd]==1:
                    print("Kamen polozen")
                    if Sachovnice[pozx][pozy].chuze==2:
                        pocitadlo-=1
                    Sachovnice[pozx][pozy].chuze-=1
                    Sachovnice[pozc][pozd]=Sachovnice[pozx][pozy]
                    Sachovnice[pozx][pozy]=0
                    odznaceni(Sachovnice)
                    zved=0
                    novapoz(Sachovnice)
                         
                
        
            
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
    while not done:
        for event in pygame.event.get():
            if pocitadlo==0:
                done=True
                
            if event.type == pygame.QUIT:
                print("User asked to quit.")
                done=True
            elif event.type == pygame.KEYDOWN and ((event.key)==111): 
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
                            prozprom=Sachovnice[pozx][pozy]
                            print("Kamen pripraven")


       
                
            elif event.type == (pygame.MOUSEBUTTONDOWN or pygame.KEYDOWN) and zved==1:
                b=list(pygame.mouse.get_pos())
                c = b[0]
                d = b[1]

                pozc=c//(720//pocetSloupcu)
                pozd=(d//(480//pocetRad))
                if type(Sachovnice[pozc][pozd])==int:
                    pozc=pozc
                elif (Sachovnice[pozc][pozd].smer!=tah)and(((pozc+1+Sachovnice[pozx][pozy].strelba>pozx)and(pozc<pozx)and(pozy==pozd)) or ((pozc-1-Sachovnice[pozx][pozy].strelba<pozx)and(pozc>pozx)and(pozy==pozd)) or ((pozd-1-Sachovnice[pozx][pozy].strelba<pozy)and(pozd>pozy)and(pozx==pozc)) or ((pozd+1+Sachovnice[pozx][pozy].strelba>pozy)and(pozd<pozy)and(pozx==pozc))):
                    print("Utok polozen")
                    Sachovnice[pozx][pozy].moznostUtoku-=1
                    pocitadlo-=1
                    prezil=Sachovnice[pozx][pozy].boj(Sachovnice[pozc][pozd])
                    if prezil==0:
                        Sachovnice[pozc][pozd]=0
                    
                    odznaceni(Sachovnice)
                    print(prozprom)
                    zved=0
                    novapoz(Sachovnice)

def stahni(Sachovnice,smer,kdo):
    zved=0
    chyba =0
    done=False
    pocitadlo=3
    Sachovnice=odznaceni(Sachovnice)
    print("Zmacknete O pro ukonceni faze")
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("User asked to quit.")
                done=True
            elif event.type == pygame.KEYDOWN and ((event.key)==111): 
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
                    if (type(Sachovnice[pozx][pozy])!=int):
                        print(Sachovnice[pozx][pozy].cislo)
                        if  (Sachovnice[pozx][pozy].smer==smer)and(Sachovnice[pozx][pozy].cislo==kdo):
                            zved=1
                            prozprom=Sachovnice[pozx][pozy]
                            print("Kamen zvednut")
                            pohybprom=1
                            zedx=-1
                            for i in Sachovnice:
                                zedx+=1
                                zedy=-1
                                for j in i:
                                    zedy+=1
                                    if type(j)!=int:
                                        if j.smer==smer and j.cislo==4:
                                            print("Zed")   
                                            if zedx>0:
                                                Sachovnice[zedx-1][zedy]=1 if(Sachovnice[zedx-1][zedy]==0) else  Sachovnice[zedx-1][zedy]
                        
                                            if zedx<5:
                                                Sachovnice[zedx+1][zedy]=1 if(Sachovnice[zedx+1][zedy]==0) else  Sachovnice[zedx+1][zedy]

                                            if zedy>0:
                                                Sachovnice[zedx][zedy-1]=1 if(Sachovnice[zedx][zedy-1]==0) else  Sachovnice[zedx][zedy-1]

                                            if zedy<7:
                                                Sachovnice[zedx][zedy+1]=1 if(Sachovnice[zedx][zedy+1]==0) else  Sachovnice[zedx][zedy+1]
                            novapoz(Sachovnice)
                            zved=1
                            prozprom=Sachovnice[pozx][pozy]

       
                
            elif event.type == (pygame.MOUSEBUTTONDOWN or pygame.KEYDOWN) and zved==1:
                b=list(pygame.mouse.get_pos())
                c = b[0]
                d = b[1]
                pozc=(c//(720//pocetSloupcu))
                pozd=(d//(480//pocetRad))
                if Sachovnice[pozc][pozd]==1:
                    print("Kamen polozen")
                    Sachovnice[pozc][pozd]=Sachovnice[pozx][pozy]
                    Sachovnice[pozx][pozy]=0
                    odznaceni(Sachovnice)
                    zved=0
                    novapoz(Sachovnice)
                          
                
        
        
