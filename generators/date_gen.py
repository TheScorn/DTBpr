#!/usr/bin/env python3

import random
import datetime
import pandas as pd

#Założenia
#uznajemy że sklep działa od 201? do 2022
#żeby nie było problemu z datami których nie było
#Zakładamy że sklep pracuje w weekendy

def date_gen() -> str:
    """
    sklep działa od 201? stąd daty zaczynają się od 
    201? (2016)

    załóżmy że ostatnia data działania to 2022-12-31 
    """
    start_date = datetime.datetime.strptime("2016-01-01","%Y-%m-%d")
    #w kalkulatorze dat tyle dni jest między startem a końcem
    #pandas generuje listę możliwych dat
    date_generated=pd.date_range(start_date, periods = 2557)
    random_date = random.randrange(0,2558,1)
    return(date_generated[random_date].strftime("%Y-%m-%d"))
    


if __name__ == "__main__":
    
    print(date_gen())
