import random


# Oppgave 4

def trekke_vinnertall():
    alle_tall = list(range(1, 35))
    
    vinnertall = random.sample(alle_tall, 7)
    
    tilleggstall = random.randint(1, 34)
    
    return vinnertall + [tilleggstall]

def sjekk_lottokupong(kupong, vinnertall):
    antall_riktige = len(set(kupong).intersection(set(vinnertall)))
    
    return antall_riktige

def generer_tilfeldige_lottorekker(antall_rekker):
    lottorekker = []
    
    for _ in range(antall_rekker):
        lottorekke = random.sample(range(1, 35), 7)
        lottorekker.append(lottorekke)
    
    return lottorekker

if __name__ == "__main__":
    vinnertall = trekke_vinnertall()
    print("Vinnertall:", vinnertall)
    
    lottokupong = [6, 34, 12, 1, 2, 23, 27]
    antall_riktige = sjekk_lottokupong(lottokupong, vinnertall)
    print("Antall riktige på lottokupongen:", antall_riktige)
    
    antall_rekker = int(input("Hvor mange tilfeldige lottorekker vil du generere? "))
    tilfeldige_rekker = generer_tilfeldige_lottorekker(antall_rekker)
    print("Tilfeldige lottorekker:")
    for rekke in tilfeldige_rekker:
        print(rekke)
