from kresleni  import*
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
                              
