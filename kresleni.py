import pygame
import os
import webbrowser
from kresleniMaleFce import *
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
zoom=1
soucSachovnice=list()


PI = 3.141592653
size = (1025, 540)
sirka=1025
screen = pygame.display.set_mode(size)
help = pygame.image.load('help.jpg')
help = pygame.transform.scale(help, (40, 40))
sound = pygame.image.load('sound.jpg')
sound = pygame.transform.scale(sound, (40, 40))
skip = pygame.image.load('skip.jpg')
skip = pygame.transform.scale(skip, (80, 40))
big = pygame.image.load('bigger.jpg')
big = pygame.transform.scale(big, (80, 40))


"""Navod"""
current_dir = os.path.dirname(os.path.abspath(__file__))

html_file_path = os.path.join(current_dir, 'SWnavod.html')



"""Jmeno okna"""
pygame.display.set_caption("Valky vyvolavacu")
done = False
screen.fill(WHITE)




def pozadi():
    elist=list()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == (pygame.MOUSEBUTTONDOWN or pygame.KEYDOWN):
            a=list(pygame.mouse.get_pos())
            global zoom
            global sirka
            x = a[0]
            y= a[1]
            
            if y<481 and event.touch==False:
                x=int(x/zoom)
                nevent=event
                nevent.pos=(x,y)              
                pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'pos':(x, y), 'button': event.button, 'touch': True, 'window': None}))
                continue  




            if x>970 and 1010>x:
                if y>490 and 530>y:
                    webbrowser.open_new_tab('file://' + html_file_path)

            elif x<131:
                if 41>x:
                    if y>490 and 530>y:
                        global zvuk
                        if zvuk==0:
                            pygame.mixer.music.set_volume(1.0)
                            zvuk=1
                        else:
                            pygame.mixer.music.set_volume(0.0)
                            zvuk=0
                elif x>50 and 131>x:
                   if y>490 and 530>y:
                        if zoom!=1:
                            zoom=1
                        else:
                            zoom=sirka/720
                        novapoz(soucSachovnice,panelsoucobsah)

            
            elif x>465 and 545>x:
                if y>490 and 530>y:
                    pygame.event.post(pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_o, 'mod': 0}))

        elist.append(event)
    try:
        return(elist+[])
    except:
        return(None)
    
def konec():
    while True:
        pozadi()


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
    global zoom
    
    screen.fill(WHITE)
    x=30-(posunSloupcu)
    y=30
    barva=BLACK
    for i in range(pocetSloupcu):
        x+=posunSloupcu
        for j in range(pocetRad):
            if type(Sachovnice[i][j])==int: 
                pygame.draw.rect(screen, barva, [int(x-30)*zoom,int(y-30),posunSloupcu*zoom,posunRad])
            y+=posunRad
            if (barva==WHITE):
                barva=BLACK
            else:
                barva=WHITE
            if type(Sachovnice[i][j])!=int:
                pozadikarty = Sachovnice[i][j].vyv.pozadi
                pozadikarty = pygame.transform.scale(pozadikarty, (posunSloupcu*zoom, posunRad))
                if Sachovnice[i][j].vyv.smer==1:
                    pozadikarty = pygame.transform.rotate(pozadikarty, 180)
                screen.blit(pozadikarty, ((x-30)*zoom, y-posunRad-30))

        y=30
        if (barva==WHITE and pocetRad%2==1) or (barva==BLACK and pocetRad%2==0):
            barva=WHITE
        else:
            barva=BLACK
    pygame.draw.line(screen,BLACK, [0,0],[720*zoom,0],2)
    pygame.draw.line(screen,BLACK, [720*zoom,0],[720*zoom,480],2)
    pygame.draw.line(screen,BLACK, [720*zoom,480],[0,480],2)
    pygame.draw.line(screen,BLACK, [0,480],[0,0],2)
    proma=-1

    kresx=0
    global soucSachovnice
    soucSachovnice=Sachovnice
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
                    textRect.center=((kresx*posunSloupcu*zoom)-posunSloupcu*zoom/2,(kresy*posunRad)-posunRad/2)
                    screen.blit(text,textRect)
                elif type(j)!=int:
                    font=pygame.font.Font("gothicfont.ttf",int((posunRad//5)*4))
                    slovo=(f"{j.typ}{j.zivoty},{j.utok}")
                    barva=RED if j.smer==1 else BLUE
                    text=font.render(slovo, True, barva, )
                    textRect= text.get_rect()
                    textRect.center=((kresx*posunSloupcu*zoom)-posunSloupcu*zoom/2,(kresy*posunRad)-posunRad/2)
                    screen.blit(text,textRect)

        """Tvorba okna pro komunikaci"""
    kde=0
    global panelsoucobsah
    panelsoucobsah=obsah
    if zoom==1:
        pygame.draw.rect(screen, LBLUE, [int(735),int(0),275,480])
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
    screen.blit(big, (50, 490))
    screen.blit(skip, (465, 490))

    pygame.display.flip()   
