import random
def domich(vyv):
    done=False
    while (len(vyv.balicekRuka)<5 and not done):
            if len(vyv.balicekVoj)==0:
                 done=True
            else:
                  los=random.choice(range(len(vyv.balicekVoj)))
                  karta=vyv.balicekVoj[los]
                  del vyv.balicekVoj[los]
                  vyv.balicekRuka.append(karta)

def nakup(vyv,mapA):
      print(f"Pocet karet v magickem balicku: {vyv.balicekMagicky}")
      print(vyv.balicekRuka)
      Moznost=1
      while Moznost!=0:
            print(f"Pocet karet v magickem balicku: {vyv.balicekMagicky}")
            for i in vyv.balicekRuka:
                  print(vyv.slovnik[i])
            Moznost=0
            a=input("Napiste cislo karty, kterou chcete vyvolat: ")
            if a!="":
                  try:
                        Moznost=int(a)
                  except:
                       Moznost==6
                       print("Spatna odpoved")
                       
                  
            if Moznost in vyv.balicekRuka:
                  if vyv.balicekMagicky<vyv.ocen(Moznost):
                        print("Nedostatek penez v magickem balicku")
                  else: 
                        vyv.balicekMagicky-=vyv.ocen(Moznost)
                        if Moznost!=4:
                              mapA.VyvolejMapa(vyv.vyvolej(Moznost),vyv)
                        else:
                              mapA.VyvolejZed(vyv.vyvolej(Moznost),vyv)
                        vyv.balicekRuka.remove(Moznost)
                              

def odhoz(vyv):
    Moznost=1
    while Moznost!=0:
        print(f"Pocet karet v magickem balicku: {vyv.balicekMagicky}")
        for i in vyv.balicekRuka:
            print(vyv.slovnik[i])
        Moznost=0
        a=input("Napiste cislo karty, kterou chcete odhodit: ")
        if a!="":
            try:
                Moznost=int(a)
                if Moznost in vyv.balicekRuka:
                    print("Karta odhozena")
                    vyv.balicekRuka.remove(Moznost)
                    vyv.balicekMagicky+=1
                    
                    
            except:
                print("Spatna odpoved")
                Moznost=6
    



