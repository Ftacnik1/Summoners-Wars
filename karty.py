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
