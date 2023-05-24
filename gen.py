#!/usr/bin/env python3
import random


def generate_person():
    sex = random.randrange(0,2)
    print(f"sex:{sex}")
    if sex == 0:
        #generowanie dla male
        number_name = random.randrange(0,100)
        print(number_name)
        f = open("names/male_names.txt","r",encoding="utf8")
        for i in range(number_name-1):
            f.readline()
        name = f.readline()
        name = name[:-1]
        f.close()

        number_surname = random.randrange(0,42)
        print(number_surname)
        f = open("names/male_surnames.txt","r",encoding="utf8")
        for i in range(number_surname-1):
            f.readline()
        surname = f.readline()
        surname = surname[:-1]
        f.close()
        return(name,surname)

    else:
        #generowanie dla female
        number_name = random.randrange(0,100)
        print(number_name)
        f = open("names/female_names.txt","r",encoding="utf8")
        for i in range(number_name-1):
            f.readline()
        name = f.readline()
        name = name[:-1]
        f.close()
        
        number_surname = random.randrange(0,42)
        print(number_surname)
        f = open("names/female_surnames.txt","r",encoding="utf8")
        for i in range(number_surname-1):
            f.readline()
        surname = f.readline()
        surname = surname[:-1]
        f.close()
        return(name,surname)

osoba = generate_person()
print(osoba[0])
print(osoba[1])
