import random



# Oppgave 1

vits = "Why did the programmer quit his job? Because he didn't get arrays."

def dagens_vits():
    print(vits)

dagens_vits()

def dagens_vits2(parameter):
    print(parameter)

dagens_vits2(vits)

def dagens_vits3(parameter):
    print(parameter)
    return parameter

resultat = dagens_vits3(vits)

# Oppagave 2

# Den printer ikke hei fordi ord er funkjson, ikke hei

# Oppagave 3

# Data om eliteserielag
eliteserielag = [
  { "lag": "Lillestrøm", "seriemesterskap": [1976, 1977, 1986, 1989], "norgesmesterskap": [1977, 1978, 1981, 1985, 2007, 2017] },
  { "lag": "Molde", "seriemesterskap": [2011, 2012, 2014, 2019], "norgesmesterskap": [1994, 2005, 2013, 2014, 2021] },
  { "lag": "Viking", "seriemesterskap": [1972, 1973, 1974, 1975, 1979, 1982, 1991], "norgesmesterskap": [1979, 1989, 2001, 2019] },
  { "lag": "Strømsgodset", "seriemesterskap": [1970, 2013], "norgesmesterskap": [1969, 1970, 1973, 1991, 2010] },
  { "lag": "Aalesund", "seriemesterskap": [], "norgesmesterskap": [2009, 2011] },
  { "lag": "Rosenborg", "seriemesterskap": [1967, 1969, 1971, 1985, 1988, 1990, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2006, 2009, 2010, 2015, 2016, 2017, 2018], "norgesmesterskap": [1964, 1971, 1988, 1990, 1992, 1995, 1999, 2003, 2015, 2016, 2018] },
  { "lag": "Sarpsborg", "seriemesterskap": [], "norgesmesterskap": [] },
  { "lag": "Bodø/Glimt", "seriemesterskap": [2020, 2021], "norgesmesterskap": [1975, 1993] },
  { "lag": "Odd", "seriemesterskap": [], "norgesmesterskap": [2000] },
  { "lag": "Tromsø", "seriemesterskap": [], "norgesmesterskap": [1986, 1996] },
  { "lag": "Vålerenga", "seriemesterskap": [1965, 1981, 1983, 1984, 2005], "norgesmesterskap": [1980, 1997, 2002, 2008] },
  { "lag": "HamKam", "seriemesterskap": [], "norgesmesterskap": [] },
  { "lag": "Sandefjord", "seriemesterskap": [], "norgesmesterskap": [] },
  { "lag": "Haugesund", "seriemesterskap": [], "norgesmesterskap": [] },
  { "lag": "Jerv", "seriemesterskap": [], "norgesmesterskap": [] },
  { "lag": "Kristiansund", "seriemesterskap": [], "norgesmesterskap": [] }
]

lag_med_seriemesterskap = [lag["lag"] for lag in eliteserielag if lag["seriemesterskap"]]
print("Lag med minst ett seriemesterskap:", lag_med_seriemesterskap)

lag_med_seriemesterskap_og_norgesmesterskap = [lag["lag"] for lag in eliteserielag if lag["seriemesterskap"] and lag["norgesmesterskap"]]
print("Lag med både seriemesterskap og norgesmesterskap:", lag_med_seriemesterskap_og_norgesmesterskap)

lag_med_flest_seriemesterskap = max(eliteserielag, key=lambda lag: len(lag["seriemesterskap"]))
print("Laget med flest seriemesterskap:", lag_med_flest_seriemesterskap["lag"])

lag_med_første_seriemesterskap = min(eliteserielag, key=lambda lag: min(lag["seriemesterskap"]) if lag["seriemesterskap"] else float('inf'))
print("Laget som vant serien første gang:", lag_med_første_seriemesterskap["lag"])

lag_med_siste_seriemesterskap = max(eliteserielag, key=lambda lag: max(lag["seriemesterskap"]) if lag["seriemesterskap"] else 0)
print("Laget som vant serien sist:", lag_med_siste_seriemesterskap["lag"])



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
