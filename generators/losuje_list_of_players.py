import mysql.connector
import csv 
import random
from datetime import datetime, timedelta
import math

#ta funkcja potrzebuje losuj_tournaments(dane)[1] (drugi element przy returnie)

def losuj_list_of_players(dane):
    wynik = []
    for i in range(len(dane)):
        lista = random.sample(range(1, 301), dane[i])
        for k in lista:
            if lista[0] == k:
                wynik.append([k,i+1,1])
            else:
                wynik.append([k,i+1,0])
    random.shuffle(wynik)
    return wynik

if __name__ == "__main__":
    pass
