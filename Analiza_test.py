import mysql.connector
import pandas as pd

con = mysql.connector.connect(
            host = "giniewicz.it",
            user = "team04",
            password = "te@m0a",
            database = "team04",
            )
if not con:
        raise Exception("connection error")
def staff_ranking(): 
        """
        Funkcja tworzy ranking pracowników miesiąca.
        """ 
        cs = con.cursor()
        cs.execute("SELECT distinct YEAR(payment_date) as 'Year', MONTH(payment_date) as 'Month' from payment ORDER BY YEAR DESC,MONTH DESC")
        dates=cs.fetchall()
        rank=[]
        for i in dates: 
                wzorzec_daty=f"{i[0]}-{i[1]:02}"
                cs.execute("SELECT staff_id,sum(amount) as earn from payment WHERE payment_date LIKE %s GROUP BY staff_id ORDER BY zarobek DESC LIMIT 1",[wzorzec_daty+ '%'])
                wynik = cs.fetchall()
                rank.append([wzorzec_daty,wynik[0][0],int(wynik[0][1])])
        df = pd.DataFrame(rank,columns=["Date","Staff_id","Earn"])
        return df

def top_10(g_id):
        """
        Funkcja tworzy ranking 10 najlepszych zawodników dla danej id gry.
        """
        cs = con.cursor()
        cs.execute("SELECT distinct game_id from tournaments")
        g_ids =cs.fetchall()
        g_ids=list(element[0] for element in g_ids)
        if g_id in g_ids:
                cs.execute("SELECT games.title,first_name,last_name,COUNT(list_of_players.customer_id) from list_of_players inner join tournaments on list_of_players.tournament_id=tournaments.tournament_id inner join games on tournaments.game_id=games.game_id inner join customers on list_of_players.customer_id=customers.customer_id WHERE place=1 and games.game_id=%s GROUP BY list_of_players.customer_id",[g_id])
                top_10=cs.fetchall()
                df = pd.DataFrame(top_10,columns=["Game_title","First_name","Last_name","Num_of_wins"])
                return df
        else:
                print("No tournament for this game.")


con.close()