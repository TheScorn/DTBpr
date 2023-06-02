#!/usr/bin/env python3

import mysql.connector
from date_gen import date_gen


def main():
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

    cursor = con.cursor()
    cursor.execute("CREATE TEMPORARY TABLE IF NOT EXISTS test(id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,data DATE NOT NULL);")
    cursor.execute("SHOW COLUMNS FROM test;")
    random_date = date_gen()
    print(cursor)

    con.close()

if __name__ == "__main__":
    main()
