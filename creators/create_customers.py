#!/usr/bin/env python3

def create_customers():
    """
    funkcja tworząca tabelę customers
    ma dodane player_id gdy klient jest jednocześnie graczem
    na razie w trybie temporary
    """
    cs = con.cursor()
    table = "CREATE OR REPLACE TEMPORARY TABLE customers(customer_id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,first_name VARCHAR(45) NOT NULL,last_name VARCHAR(45) NOT NULL,email VARCHAR(50),address varchar(50) NOT NULL,city VARCHAR(50) NOT NULL,player_id SMALLINT UNSIGNED DEFAULT NULL)"
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
    create_customers()
    ##########
    #test czy działa wstawiając wartość i odczytując
    cs = con.cursor()
    insert = "INSERT INTO customers (first_name, last_name, email, address, city) VALUES (%s, %s, %s, %s, %s)"
    

    val = ("andrzej","ziomal","andrzej.ziomal@gmail.com","Wrocławska 10","Kraków")
    cs.execute(insert,val)
    con.commit()
    cs.fetchall()

    cs.execute("SELECT first_name FROM customers")

    for i in cs:
        print(i)

    con.close()






