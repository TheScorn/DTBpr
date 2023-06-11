#!/usr/bin/env python3

from generators.name_gen import generate_person
from generators.address_gen import address_gen
from generators.city_gen import generate_city
import random
import math
import numpy as np

def fill_customers(con,n) -> int:
    """
    funkcja napełnia tabelę customers rekordami
    n - liczba rekordów
    zwraca liczbę klientów którzy zostali wylosowani jako gracze
    """
    cs = con.cursor()
    insert = "INSERT INTO customers (first_name,last_name,  email, address, city) VALUES (%s,%s,%s,%s,%s)"

    for i in range(n):
        person = generate_person()
        first_name = person[0]
        last_name = person[1]
        email = person[2]
        address = address_gen()
        city = generate_city()
        val = (first_name, last_name,email, address, city)
        cs.execute(insert,val)
        con.commit()
        cs.fetchall()

def fill_staff(con,n:int)-> None:
    """
    funkcja wypełniająca tabelę staff
    """

    cs = con.cursor()
    sal = [3000,3100,3200,3250,3300,3400]
    insert = "INSERT INTO staff (first_name, last_name, email, address, city, salary) VALUES (%s,%s,%s,%s,%s,%s)"

    for i in  range(n):
        person = generate_person()
        first_name = person[0]
        last_name = person[1]
        email = person[2]
        address = address_gen()
        city = generate_city()
        numb = random.randrange(0,6)
        salary = sal[numb]
        val = (first_name, last_name, email, address, city, salary)
        cs.execute(insert,val)
        con.commit()
        cs.fetchall()

def fill_inventory(con,n:int)->int:
    """
    funkcja wypełnia tablelę inventory
    n działa nieco inaczej w tym wypadku
    za n podstawiamy ilość gier które będą się znajdować w tabeli games
    funkcja zwraca całkowitą sumę gier które znajdują się w inwentarzu
    """

    cs  = con.cursor()
    insert = "INSERT INTO inventory (game_id) VALUES (%s)"

    for i in range(n):
        number = abs(math.ceil(np.random.normal(3,6)))
        for j in range(number):
            val = [i]
            cs.execute(insert,val)
            con.commit()
            cs.fetchall()

