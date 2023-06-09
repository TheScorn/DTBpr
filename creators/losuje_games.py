import mysql.connector
import csv 
import random
from datetime import datetime, timedelta
import math

with open('C:\\Users\\User\\Documents\\GitHub\\DTBpr\\generators\\games\\bgg_dataset', 'r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';')
    gry = list(reader)
    del gry[0]
    kolumny_do_usuniecia = [0, 7, 9, 11]
    for row in gry:
        for index in sorted(kolumny_do_usuniecia, reverse=True):
            del row[index]
    kolumny = [6, 7]
    for row in gry:
        for index in sorted(kolumny, reverse=True):
              row[index] = row[index].replace(",", ".")
              row[index] = float(row[index])
    kolumny_do_naprawy = [1, 2, 3, 4, 5]
    for row in gry:
        for index in kolumny_do_naprawy:
            try:
                row[index] = int(row[index])
            except ValueError:
                pass 

def losuj_games(n):
    numerki = random.sample(range(1, len(gry)), n)
    lista = []
    for element in numerki:
        lista.append(gry[element])
    return(lista)