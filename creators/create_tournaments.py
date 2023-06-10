#!/usr/bin/env python3

def create_tournaments():
    """
    funkcja tworząca tabelę customers,
    na ten moment temporary
    by nie usuwać danych na serwerze,
    w ten sposób od szablonu można tworzyć i testować
    wszystkie funkcje tworzące tabele,
    potem wystarczy zaimportować i odpalić wszystkie na raz.
    """
    cs = con.cursor()
    table = "CREATE OR REPLACE TEMPORARY TABLE tournaments(tournament_id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,game_id SMALLINT NOT NULL,start_date DATE NOT NULL,end_date DATE NOT NULL,prize FLOAT UNSIGNED DEFAULT NULL)"
    cs.execute(table)
    cs.fetchall()
    
    alter1 = "ALTER TABLE tournaments ADD CONSTRAINT start_date_in_bounds CHECK (start_date <= '2022-12-01' AND start_date >= '2014-01-01')"
    alter2 = "ALTER TABLE tournaments ADD CONSTRAINT end_date_in_bounds CHECK (DATE(end_date) > DATE(start_date))"
    cs.execute(alter1)
    cs.execute(alter2)
    

if __name__ == "__main__":
    import time
    import datetime
    import mysql.connector
    con = mysql.connector.connect(
            host = "giniewicz.it",
            user = "team04",
            password = "te@m0a",
            database = "team04",
            )
    if con:
        print("connected")
    else:
        print("connection error")
    create_tournaments()
    ##########
    #test czy działa wstawiając wartość i odczytując
    cs = con.cursor()
    insert = "INSERT INTO tournaments (game_id, start_date, end_date, prize) VALUES (%s, %s, %s, %s)"

    
    date1 = datetime.datetime(2021,6,14)
    print(date1)
    date1_formatted = date1.strftime('%Y-%m-%d')
    print(date1)
    date2 = datetime.datetime(2021,6,23)
    date2_formatted = date2.strftime('%Y-%m-%d')

    val = (4,date1_formatted,date2_formatted, 350.50)
    cs.execute(insert,val)
    con.commit()
    cs.fetchall()

    cs.execute("SELECT * FROM tournaments")
    
    for i in cs:
        print(i)

    con.close()