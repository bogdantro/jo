import time
import os
import sys
import random

os.system('cls')


# Oppgave a
tall = [3, 1, 2, 6, 8, 2, 7, 7, 6, 8, 2, 7, 5, 8, 6, 3, 5, 4, 1, 6]
sju = tall.count(7)
print(f"Antall forekomster av tallet 7 i listen tall: {sju}")

# Oppgave b
mellom_2_5 = sum(1 for num in tall if 2 <= num <= 5)
print(f"Antall tall i intervallet [2, 5] i listen tall: {mellom_2_5}")

# Oppgave c
ord = ["xax", "er", "foff", "and", "em", "nu", "nei", "nuet", "nan", "momom", "sopp", "ost", "yax"]
minst_3 = sum(1 for word in ord if len(word) >= 3)

# Oppgave d
første_siste = sum(1 for word in ord if len(word) >= 3 and word[0] == word[-1])

print(f"Antall ord med tre eller flere tegn i listen ord: {minst_3}")
print(f"Antall ord med tre eller flere tegn og like første og siste bokstav: {første_siste}")

def random_tall(tall):
    return random.choice(tall)

# Example usage:
random_number = random_tall(tall)
print(f"{random_number}")