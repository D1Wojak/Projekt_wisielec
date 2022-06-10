from random import randint
import codecs
import sys

### Wczytywanie haseł z pliku ###
plik_z_haslami = codecs.open("hasla.txt", 'r', 'utf-8')
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

### Wczytywanie wylosownaego hasła ###
haslo = []
licznik1 = 0

for i in hasla:
    if i == ".":
        licznik1 +=1
    if licznik1 == nr_wylosowanego_hasla:
        haslo += i
haslo.remove(".")
for i in haslo:
    if i == "\n":
        haslo.remove("\n")
for i in haslo:
    if i == "\r":
        haslo.remove("\r")

### Wisielec ###
grafika = [ """
#                   #
#                   #
#                   #
#                   #
#                   #
#                   #
#     _____         #""","""
#                   #
#       |           #
#       |           #
#       |           #
#       |           #
#       |           #
#     _____         #""","""
#       _________   #
#       |           #
#       |           #
#       |           #
#       |           #
#       |           #
#     _____         #""","""
#       _________   #
#       | /         #
#       |/          #
#       |           #
#       |           #
#       |           #
#     _____         #""","""
#       _________   #
#       | /     |   #
#       |/          #
#       |           #
#       |           #
#       |           #
#     _____         #""","""
#       _________   #
#       | /     |   #
#       |/      o   #
#       |           #
#       |           #
#       |           #
#     _____         #""","""
#       _________   #
#       | /    |    #
#       |/     o    #
#       |      |    #
#       |           #
#       |           #
#     _____         #""","""
#       _________   #
#       | /    |    #
#       |/     o    #
#       |      |    #
#       |     / \   #
#       |           #
#     _____         #""","""
#       _________   #
#       | /    |    #
#       |/     o    #
#       |     /|\   #
#       |     / \   #
#       |           #
#     _____         #"""]

print("Podaj imię: ")
nick = input()

tablica = list(haslo)
zycia = 0
for i in range(len(haslo)):
    if tablica[i] == " ":
        tablica[i]=" "
    else:
        tablica[i] = "_"


while zycia < 9:
    print(nick + " pozostało Ci :"+ str(9-zycia) + " zyc.")
    print(" ".join(tablica))

    print("Podaj JEDNA litere " + str(nick) + " :")
    litera = input()
    if len(litera) > 1:
        print("Popelniłeś błąd! Podaj WYŁĄCZNIE JEDNĄ litere!")
        litera = input()
    if litera in haslo:
        for i in range(len(haslo)):
            if haslo[i] == litera:
                tablica[i] = litera
        if tablica == haslo:
            print(nick, "Brawo, wygrałeś!")
            break

    else:
        zycia +=1
        print(grafika[zycia-1])
        if zycia == 9:
            print("Przegrałeś " + nick)
