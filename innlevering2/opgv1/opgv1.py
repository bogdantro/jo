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
