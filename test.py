#!/usr/bin/env python3

import mysql.connector
from date_gen import date_gen
from name_gen import generate_person

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
    '''
    cursor = con.cursor()
    cursor.execute("CREATE TEMPORARY TABLE IF NOT EXISTS test(id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,data DATE NOT NULL)")
    cursor.fetchall()
    random_date = date_gen()
    #random_date = str(random_date)
    sql_command = ("INSERT INTO test (data) VALUES ({})".format(random_date))
    cursor.execute(sql_command)
    con.commit()
    cursor.fetchall()
    cursor.execute("SELECT data FROM test")
    '''
    cursor = con.cursor()
    cursor.execute("CREATE TEMPORARY TABLE IF NOT EXISTS test(id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,imie VARCHAR(20) NOT NULL,nazwisko VARCHAR(25) NOT NULL)")
    cursor.fetchall()
    
    person = generate_person()
    sql_command2 = "INSERT INTO test (imie, nazwisko) VALUES (%s,%s)"
    val = (person[0], person[1])
    cursor.execute(sql_command2,val)
    con.commit()
    cursor.fetchall()
    
    sql_command2 = "SELECT imie, nazwisko FROM test"
    cursor.execute(sql_command2)
    for i in cursor:
        print(i)
    con.close()
    
if __name__ == "__main__":
    main()
