from random import randint
import codecs
import sys

#Podanie imienia

print("Podaj imię: ")
nick = input()

### Wybór poziomu trudności

print("Wybierz poziom trudności : ")
print("1 - Łatwy (wyrazy do 5 liter) ")
print("2 - Średni (wyrazy do 10 liter) ")
print("3 - Trudny (wyrazy do 15 liter) ")
print("4 - Niemożliwy (15 i więcej liter) ")
poziom = input()
poziom = int(poziom)

### Wczytywanie haseł z pliku ###
if poziom <1 or poziom >4:
    print("Nie wybrałeś żadnego poziomu trudności! Następny błąd będzie skutkował wyłączeniem się programu!")
    poziom = input()
    poziom = int(poziom)
if poziom == 1:
    plik_z_haslami = codecs.open("hasla1.txt", 'r', 'utf-8')
if poziom == 2:
    plik_z_haslami = codecs.open("hasla2.txt", 'r', 'utf-8')
if poziom == 3:
    plik_z_haslami = codecs.open("hasla3.txt", 'r', 'utf-8')
if poziom == 4:
    plik_z_haslami = codecs.open("hasla4.txt", 'r', 'utf-8')

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
tablica = list(haslo)
tablica1= list(haslo)
print(tablica)
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
        print("Popelniłeś błąd! Podaj WYŁĄCZNIE JEDNĄ litere! Następny błąd będzie skutkował utratą życia!")
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
            print("Poprawna odpowiedź to: ")
            print("".join(tablica1))
