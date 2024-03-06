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
    for i in range (6):
        if type(Sachovnice[i][y])==int:
            Sachovnice[i][y]= vyv.vyvolej(1)