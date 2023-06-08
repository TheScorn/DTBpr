#!/usr/bin/env python3

def create_inventory():
    """
    funkcja tworząca tabelę customers,
    na ten moment temporary
    by nie usuwać danych na serwerze,
    w ten sposób od szablonu można tworzyć i testować
    wszystkie funkcje tworzące tabele,
    potem wystarczy zaimportować i odpalić wszystkie na raz.
    """
    cs = con.cursor()
    table = "CREATE OR REPLACE TEMPORARY TABLE inventory(inventory_id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,game_id SMALLINT UNSIGNED NOT NULL) COMMENT 'magazynek'"
    cs.execute(table)
    cs.fetchall()


if __name__ == "__main__":
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

    create_inventory()
    
    ##########
    #test czy działa wstawiając wartość i odczytując
    cs = con.cursor()
    insert = "INSERT INTO inventory (game_id) VALUES (%s)"
    

    val = [2]
    cs.execute(insert,val)
    con.commit()
    cs.fetchall()

    cs.execute("SELECT * FROM inventory")

    for i in cs:
        print(i)

    con.close()
