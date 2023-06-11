#!/usr/bin/env python3

import mysql.connector
from creators.create_customers import create_customers
from creators.create_inventory import create_inventory
from creators.create_tournaments import create_tournaments
from creators.create_games import create_games
from creators.create_staff import create_staff
from creators.create_rental import create_rental
from creators.create_payment import create_payment
from creators.create_players import create_players
from creators.create_tournament_player import create_tournament_player
from creators.alter_table import alter_table

def bob_the_builder():
    """
    uruchamia wszystkie funkcje tworzące tabele;
    potem uruchamia funkcje dodającą zależności
    (której jeszcze nie ma)
    """

    
    con = mysql.connector.connect(
            host = "giniewicz.it",
            user = "team04",
            password = "te@m0a",
            database = "team04",
            )
    if not con:
        raise Exception("connection error")
    
    cs = con.cursor()
    cs.execute("SET FOREIGN_KEY_CHECKS=0")
    cs.fetchall()
    
    cs.execute("DROP TABLE IF EXISTS customers,inventory,tournaments,games,staff,rental,payment,players,tournament_player")

    create_customers(con)
    create_inventory(con)
    create_tournaments(con)
    create_games(con)
    create_staff(con)
    create_rental(con)
    create_payment(con)
    create_players(con)
    create_tournament_player(con)
    alter_table(con)
    
    cs.execute("SET FOREIGN_KEY_CHECKS=1")
    con.close()

if __name__ == "__main__":
    bob_the_builder()
