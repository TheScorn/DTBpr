#!/usr/bin/env python3

def create_payment(con):
    """
    funkcja tworząca tabelę customers,
    na ten moment temporary
    by nie usuwać danych na serwerze,
    w ten sposób od szablonu można tworzyć i testować
    wszystkie funkcje tworzące tabele,
    potem wystarczy zaimportować i odpalić wszystkie na raz.
    """
    cs = con.cursor()
    table = "CREATE OR REPLACE TEMPORARY TABLE payment(payment_id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,rental_id SMALLINT UNSIGNED DEFAULT NULL,customer_id SMALLINT UNSIGNED NOT NULL,staff_id SMALLINT UNSIGNED NOT NULL,payment_date DATE NOT NULL,amount FLOAT UNSIGNED NOT NULL)"
    cs.execute(table)
    cs.fetchall()

    alter1 = "ALTER TABLE payment ADD CONSTRAINT payment_date_in_bounds CHECK (payment_date <= '2022-12-01' AND payment_date >= '2014-01-01')"
    cs.execute(alter1)


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
    create_payment(con)
    ##########
    #test czy działa wstawiając wartość i odczytując
    cs = con.cursor()
    insert = "INSERT INTO payment (customer_id,staff_id,payment_date,amount) VALUES (%s, %s, %s, %s)"
    

    val = (1,1,"2015-03-02",20.70)
    cs.execute(insert,val)
    con.commit()
    cs.fetchall()

    cs.execute("SELECT * FROM payment")

    for i in cs:
        print(i)

    con.close()






