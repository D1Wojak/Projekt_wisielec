from random import randint
import re

### Wczytywanie haseł z pliku ###
plik_z_haslami = open("hasla.txt", "r")
haslaa = plik_z_haslami.read()
plik_z_haslami.close()


### Licznik haseł ###
hasla = str(haslaa.lower())
licznik = 0
for i in hasla:
    if  i == ".":
        licznik += 1


### Losowanie hasła ###
nr_wylosowanego_hasla = randint(1, licznik)
print(nr_wylosowanego_hasla)

### Wczytywanie wylosownaego hasła ###
haslo = []
licznik1 = 0

for i in hasla:
    if i == ".":
        licznik1 +=1
    if licznik1 == nr_wylosowanego_hasla:
        haslo += i

print(haslo)