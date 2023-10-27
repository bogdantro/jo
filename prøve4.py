import random

spillvindu_bredde = 700
spillvindu_hoyde = 600

tekst_spørsmål = "Enter the number of racers (2-10): "
tekst_ugyldig_inndata = "Input is not numeric…Try Again!"
tekst_utenfor_rekkevidde = "Number not in range 2-10. Try Again!"

racers = 0
while True:
    inndata = input(tekst_spørsmål)
    if inndata.isdigit():
        antall_spillere = int(inndata)
        if 2 <= antall_spillere <= 10:
            break
        else:
            print(tekst_utenfor_rekkevidde)
    else:
        print(tekst_ugyldig_inndata)

gyldige_antall_spillere = [2, 3, 4, 5, 6, 7, 8, 9, 10]

if antall_spillere in gyldige_antall_spillere:
    print("Antall spillere er innenfor rekkevidde.")
else:
    print("Antall spillere er utenfor rekkevidde.")

COLORS = ["red", "green", "blue", "orange", "yellow", "black", "purple", "pink", "brown", "cyan"]
COLORS.append("lime")

if "cyan" in COLORS:
    COLORS.remove("cyan")

tilfeldig_farge = random.choice(COLORS)
print("Tilfeldig valgt farge:", tilfeldig_farge)

antall_spillere = 5
colors = COLORS.copy()
random.shuffle(colors)
valgte_farger = colors[:antall_spillere]

print("Valgte farger for spillerne:", valgte_farger)

pace = [random.randint(1, 6) for _ in colors]

max_pace = max(pace)
winner_index = pace.index(max_pace)
winner = valgte_farger[winner_index]

print("Vinneren er spilleren med farge", winner, "og pace", max_pace)

winners = [valgte_farger[i] for i, pace_value in enumerate(pace) if pace_value == max_pace]

if len(winners) > 1:
    random_winner = random.choice(winners)
    print("Det er flere spillere med samme poengsum. Den endelige vinneren er", random_winner)
