import time
import os
import sys

# os.system('cls')



number = 1
print(number)
while number > 0:
    time.sleep(0.7)
    number = number + 1
    if number > 20:
        print('Du har nådd grensen...')
        time.sleep(1)
        print('Fast mode aktivert')
        while number > 20:
            time.sleep(0.1)
            number = number + 1

            print(number)
    print(number)