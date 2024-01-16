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
    for i in range(0,(len(Sachovnice))):
        if Sachovnice[i]==1:
            Sachovnice[i]=0
    return(Sachovnice)
def colour(pozice):
    print(pozice)
    if pozice[0]==0:
        barvicka=RED
    else:
        barvicka=BLUE
    return(barvicka)

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
            print(j)
            print(type(j))
            if j!=0:
                font=pygame.font.Font("freesansbold.ttf",int(posunRad//2))
                if j==1:
                    print("HHH")
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
                        
                    if zedx<7:
                        Sachovnice[zedx+1][zedy]=1 if(Sachovnice[zedx+1][zedy]==0) else  Sachovnice[zedx+1][zedy]

                    if zedy>0:
                        Sachovnice[zedx][zedy-1]=1 if(Sachovnice[zedx][zedy-1]==0) else  Sachovnice[zedx][zedy-1]

                    if zedy<7:
                        Sachovnice[zedx][zedy+1]=1 if(Sachovnice[zedx][zedy+1]==0) else  Sachovnice[zedx][zedy+1]
    print("Hotovo")
    novapoz(Sachovnice)

    while done==False:                                     

        for event in pygame.event.get():
            if event.type == (pygame.MOUSEBUTTONDOWN or pygame.KEYDOWN) and zved==0:
                a=list(pygame.mouse.get_pos())
                x = a[0]
                y= a[1]
                pozx=(x//120)
                pozy=(y//60)
                if x>720 or y>480:
                    chyba=1
                else:
                    chyba=0
                if chyba!=1:
                    if Sachovnice[pozx][pozy]==1:
                        zved=1
                        Sachovnice[pozx][pozy]=co
                        print("Jednotka polozena")
                        novapoz(Sachovnice)
                        done=True

       
def pohyb(Sachovnice,vyv):
    zved=0
    chyba =0
    done=False
    pocitadlo=3
    while not done:
        for event in pygame.event.get():
            if pocitadlo==0:
                for i in Sachovnice:
                    for j in i:
                        if type(j)==int:
                            j=0
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
                pozx=(x//120)
                pozy=(y//60)
                if x>720 or y>480:
                    chyba=1
                else:
                    chyba=0
                if chyba==0:
                    if (type(Sachovnice[pozx][pozy])==int):
                        if  ((Sachovnice[pozx][pozy].smer==vyv.smer)and(Sachovnice[pozx][pozy].chuze>0)):
                            zved=1
                            prozprom=Sachovnice[totpoz]
                            print("Kamen zvednut")
                            pohybprom=1
                            if type(Sachovnice[pozx+1][pozy])==int and(pozx)%6!=5:
                                Sachovnice[pozx+1][pozy]=1
                            if type(Sachovnice[pozx-1][pozy])==int and(pozx)%6!=0:
                                Sachovnice[pozx-1][pozy]=1
                            if type(Sachovnice[pozx][pozy+1])==int and(pozy)%8!=7:
                                Sachovnice[pozx][pozy+1]=1
                            if type(Sachovnice[pozx][pozy-1])==int and(pozy)%8!=0:
                                Sachovnice[pozx][pozy-1]=1
                            novapoz(Sachovnice)
                            zved=1
                            prozprom=Sachovnice[totpoz]

       
                
            elif event.type == (pygame.MOUSEBUTTONDOWN or pygame.KEYDOWN) and zved==1:
                b=list(pygame.mouse.get_pos())
                c = b[0]
                d = b[1]
                pozc=(c//120)
                pozd=(d//60)
                if Sachovnice[c][d]==1:
                    print("Kamen polozen")
                    Sachovnice[pozx][pozy].chuze-=1
                    Sachovnice[pozc][pozd]=Sachovnice[pozx][pozy]
                    Sachovnice[pozx][pozy]=0
                    odznaceni(Sachovnice)
                    zved=0
                    novapoz(Sachovnice)
                         
                
        
            
def utok(tah, Sachovnice):
    zved=0
    chyba =0
    done=False
    pocitadlo=3
    while not done:
        for event in pygame.event.get():
            if pocitadlo==0:
                print("F")
                
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
                pozx=((x-30)//120)
                pozy=(y//60)
                totpoz=(pozx*1+pozy*6)
                if totpoz>len(Sachovnice):
                    chyba=1
                else:
                    chyba=0
                print(Sachovnice[totpoz])
                if chyba==0:
                    if (type(Sachovnice[totpoz]))==list and (tah==Sachovnice[totpoz][0]+1):
                        if  (Sachovnice[totpoz][8]>0) and   Sachovnice[totpoz][6]>0:
                            zved=1
                            prozprom=Sachovnice[totpoz]
                            print("Kamen pripraven")
                            pohybprom=1
                            if type(Sachovnice[totpoz+pohybprom])==list:
                                if Sachovnice[totpoz+pohybprom][0]!=(tah+1):
                                    Sachovnice[totpoz+pohybprom][9]=1
                            elif type(Sachovnice[totpoz+pohybprom])==int:
                                pohybprom=2
                                if type(Sachovnice[totpoz+pohybprom])==list:
                                    if Sachovnice[totpoz+pohybprom][0]!=(tah+1):
                                        Sachovnice[totpoz+pohybprom][9]=1
                            pohybprom=1      
                            if type(Sachovnice[totpoz-pohybprom])==list:
                                if (Sachovnice[totpoz-pohybprom][0]!=(tah+1)):
                                    Sachovnice[totpoz-pohybprom][9]=1
                            elif type(Sachovnice[totpoz-pohybprom])==int:
                                pohybprom=-2
                                if type(Sachovnice[totpoz+pohybprom])==list:
                                    if Sachovnice[totpoz+pohybprom][0]!=(tah+1):
                                        Sachovnice[totpoz+pohybprom][9]=1
                            pohybprom=6
                            if type(Sachovnice[totpoz+pohybprom])==list:
                                if Sachovnice[totpoz+pohybprom][0]!=(tah+1):
                                    Sachovnice[totpoz+pohybprom][9]=1
                            elif type(Sachovnice[totpoz+pohybprom])==int:
                                pohybprom=12
                                if type(Sachovnice[totpoz+pohybprom])==list:
                                    if Sachovnice[totpoz+pohybprom][0]!=(tah+1):
                                        Sachovnice[totpoz+pohybprom][9]=1
                            if type(Sachovnice[totpoz-pohybprom])==list:
                                if (Sachovnice[totpoz-pohybprom][0]!=(tah+1)):
                                    Sachovnice[totpoz-pohybprom][9]=1
                            elif type(Sachovnice[totpoz+pohybprom])==int:
                                pohybprom=-12
                                if type(Sachovnice[totpoz+pohybprom])==list:
                                    if Sachovnice[totpoz+pohybprom][0]!=(tah+1):
                                        Sachovnice[totpoz+pohybprom][9]=1
                            zved=1
                            prozprom=Sachovnice[totpoz]
                        elif  (Sachovnice[totpoz][8]>0) and   Sachovnice[totpoz][2]>0:
                            zved=1
                            prozprom=Sachovnice[totpoz]
                            print("Kamen pripraven")
                            pohybprom=1
                            if type(Sachovnice[totpoz+pohybprom])==list:
                                if Sachovnice[totpoz+pohybprom][0]!=(tah+1):
                                    Sachovnice[totpoz+pohybprom][9]=1
                            pohybprom=1      
                            if type(Sachovnice[totpoz-pohybprom])==list:
                                if (Sachovnice[totpoz-pohybprom][0]!=(tah+1)):
                                    Sachovnice[totpoz-pohybprom][9]=1
                            pohybprom=6
                            if type(Sachovnice[totpoz+pohybprom])==list:
                                if Sachovnice[totpoz+pohybprom][0]!=(tah+1):
                                    Sachovnice[totpoz+pohybprom][9]=1
                            if type(Sachovnice[totpoz-pohybprom])==list:
                                if (Sachovnice[totpoz-pohybprom][0]!=(tah+1)):
                                    Sachovnice[totpoz-pohybprom][9]=1
                            zved=1
                            prozprom=Sachovnice[totpoz]

       
                
            elif event.type == (pygame.MOUSEBUTTONDOWN or pygame.KEYDOWN) and zved==1:
                b=list(pygame.mouse.get_pos())
                c = b[0]
                d = b[1]
                pozc=((c-30)//120)
                pozd=(d//60)
                totpozb=(pozc*1+pozd*6)
                print(totpozb)
                if type(Sachovnice[totpozb])==int:
                    pozc=pozc
                elif Sachovnice[totpozb][9]==1:
                    print("Utok polozen")
                    if Sachovnice[totpoz][9]==1:
                        pocitadlo-=1
                    Sachovnice[totpoz][9]-=1
                    for i in range(Sachovnice[totpoz][2]):
                        if random.choice(kostka)>3:
                            Sachovnice[totpozb][4]-=1
                    if Sachovnice[totpozb][4]<0:
                       if Sachovnice [totpozb][1]==1:
                           print("Konec")
                           Sachovnice[totpozb]=0
                           while True:
                               pocitadlo=pocitadlo
                       Sachovnice[totpozb]=0
                    odznaceni(Sachovnice)
                    print(totpozb)
                    print(prozprom)
                    zved=0
                    novapoz(Sachovnice)
                          
                
        
        
