#!/usr/bin/env python3

from creators.create_customers import create_customers
from creators.create_inventory import create_inventory
from creators.create_tournaments import create_tournaments
from creators.create_games import create_games
from creators.create_staff import create_staff

def bob_the_builder():
    """
    uruchamia wszystkie funkcje tworzące tabele;
    potem uruchamia funkcje dodającą zależności
    (której jeszcze nie ma)
    """

    import mysql.connector
    
    con = mysql.connector.connect(
            host = "giniewicz.it",
            user = "team04",
            password = "te@m0a",
            database = "team04",
            )
    if not con:
        raise Exception("connection error")
    
    create_customers()
    create_inventory()
    create_tournaments()
    create_games()
    create_staff()

    con.close()
