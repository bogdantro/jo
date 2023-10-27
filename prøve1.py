import time

number = input('Skriv in et tall: ')

binary = bin(int(number))

if number.isnumeric():
    print(number, 'i titalsystemet er', binary,'binært')
    while number != 'slutt':
        if number.isnumeric():
            number = input('Skriv in et tall: ')
            if number.isnumeric():
                binary = bin(int(number))
            print(number, 'i titalsystemet er', binary,'binært')
        else:
            print(number, 'er ikke et tall')
else:
    print(number, 'er ikke et tall')
    