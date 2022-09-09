from random import randint
import codecs
import sys

def wybierzPoziom ():
    lvl = int(input())
    while lvl < 1 or lvl > 4:
        print("Nie wybrałeś żadnego poziomu trudności! Spróbuj ponownie poziomy 1-4.")
        lvl = int(input())
    return lvl

def wczytywanieHasel (lvl):
    nazwapliku = "hasla" + str(poziom) + ".txt"
    hasla = []
    with codecs.open(nazwapliku, 'r', 'utf-8') as plik_z_haslami:
        for line in plik_z_haslami:
            hasla.append(str(line))
    return hasla
def ukrywanieHasla(haslo =[]):
    for i in range(len(haslo)):
        if tablica[i] == " ":
            tablica[i] = " "
        else:
            tablica[i] = "_"
    return tablica


def gra(tablica, tablica1):
    zycia = 0
    while zycia < 9:
       print(nick + " pozostało Ci :"+ str(9-zycia) + " zyc.")
       print(" ".join(tablica))

       print("Podaj JEDNA litere " + str(nick) + " :")
       litera = input()
       litera = litera.lower()
       if len(litera) > 1:
           print("Popelniłeś błąd! Podaj WYŁĄCZNIE JEDNĄ litere! Następny błąd będzie skutkował utratą życia!")
           litera = input()
           litera = litera.lower()

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






### Podanie imienia ###
print("Podaj imię: ")
nick = input()

### Wybór poziomu trudności ###
print("Wybierz poziom trudności : ")
print("1 - Łatwy (wyrazy do 5 liter) ")
print("2 - Średni (wyrazy do 10 liter) ")
print("3 - Trudny (wyrazy do 15 liter) ")
print("4 - Niemożliwy (15 i więcej liter) ")
poziom = wybierzPoziom()

### Wczytywanie haseł z pliku ###
hasla = wczytywanieHasel(poziom)

### Losowanie hasła ###
nr_wylosowanego_hasla = randint(1, len(hasla))

### Wczytywanie wylosownaego hasła ###
haslo = hasla[nr_wylosowanego_hasla-1]

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
tablica = ukrywanieHasla(tablica)
gra(tablica, tablica1)