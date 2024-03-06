BLUE    = (   0,   0,   255)
RED = (   255,   0,   0)
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