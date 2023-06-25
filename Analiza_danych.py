def staff_ranking(): 
        """
        Funkcja tworzy ranking pracowników dla każdego miesiąca w którym sklep prowadził działalność.
        """ 
        cs = con.cursor()
        cs.execute("SELECT distinct YEAR(payment_date) as 'Year', MONTH(payment_date) as 'Month' from payment ORDER BY YEAR DESC,MONTH DESC")
        dates=cs.fetchall()
        rank=[]
        for i in dates: 
                wzorzec_daty=f"{i[0]}-{i[1]:02}"
                cs.execute("SELECT staff.staff_id,staff.first_name,staff.last_name,sum(amount) as earn from payment inner join staff on payment.staff_id=staff.staff_id WHERE payment_date LIKE %s GROUP BY staff.staff_id ORDER BY earn DESC LIMIT 1",[wzorzec_daty+ '%'])
                wynik = cs.fetchall()
                rank.append([wzorzec_daty,wynik[0][0],wynik[0][1],wynik[0][2],int(wynik[0][3])])
        df = pd.DataFrame(rank,columns=["Date","Staff_id","First_name","Last_Name","Earn"])
        return df

def top_10_tournament_players(g_id):
        """
        g_id- id gry
        Funkcja tworzy ranking 10 najlepszych zawodników dla id danej gry.
        Ranking tworzony jest na podstawie liczby wygranych turniejów przez zawodnika.
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
                print("Brak turniej dla danej gry.")

def top5_selers_AND_rental():
        '''
        Funkcja zwraca 5 najlepszych gier pod względem sumy sprzedaży, 
        oraz 5 najlepszych gier pod względem sumy wynajmu.
        '''
        cs = con.cursor()
        cs.execute("SELECT games.title as 'Game title',sum(payment.amount) as 'Sum of rental' from payment inner join inventory on payment.rental_id_or_last_rental_id=inventory.inventory_id inner join games on inventory.game_id=games.game_id WHERE rental_id_or_last_rental_id LIKE '___' GROUP BY games.game_id ORDER by sum(payment.amount) DESC LIMIT 5")
        top_5_rental=cs.fetchall()
        df_rental = pd.DataFrame(top_5_rental,columns=["Game Title", "Sum of rental amount"])
        
        cs.execute("SELECT games.title as 'Game title',sum(payment.amount) as 'Sum of rental' from payment inner join inventory on substring(payment.rental_id_or_last_rental_id,16)=inventory.inventory_id inner join games on inventory.game_id=games.game_id WHERE rental_id_or_last_rental_id LIKE 'l%' GROUP BY games.game_id ORDER by sum(payment.amount) DESC LIMIT 5")
        top_5_sold=cs.fetchall()
        df_sold = pd.DataFrame(top_5_sold,columns=["Game Title", "Sum of solds amount"])
        return  df_rental,df_sold

def days_rental():
        '''
        Funkcja tworzy wykres punktowy oraz pudełkowy czasów wynajmowania gier. [dni]
        '''
        
        cs = con.cursor()
        cs.execute("SELECT DATEDIFF(return_date,rental_date) as 'Liczba dni w wypożyczeniu' FROM rental ")
        X = cs.fetchall()
        plt.plot(X,'o')
        plt.title("Wykres punktowy czasu wynajmu gry.")
        plt.xlabel("ID_gry")
        plt.ylabel("Czas wynajmu [dni].")
        plt.show()
        X_lista = list(itertools.chain(*X))
        plt.boxplot(X_lista,vert=False)
        plt.xlabel("Czas wynajmu [dni]")
        plt.title("Wykres pudełkowy wynajmu gier.")
        plt.show()

def longest_tournament(tabela_top10=True,Wykres_sr=True):
        '''
        Funkcja tworzy tabelę 10 najdluższych turniejów,
        oraz średni czas trwania turnieju danej gry.
        '''
        cs = con.cursor()
        if tabela_top10==True:
                cs.execute("SELECT games.game_id,games.title,TIMESTAMPDIFF(MINUTE,tournaments.start_date,tournaments.end_date) as 'Czas_trwania_turnieju[min]' from tournaments inner join games on tournaments.game_id=games.game_id ORDER BY TIMESTAMPDIFF(MINUTE,tournaments.start_date,tournaments.end_date) DESC LIMIT 10")
                top_10=cs.fetchall()
                print(pd.DataFrame(top_10,columns=["id_gry","Tytuł","czas trwania turnieju[min]"]),"\n")
        
        if Wykres_sr==True:        
                cs.execute("SELECT games.game_id,games.title,sum(TIMESTAMPDIFF(MINUTE,tournaments.start_date,tournaments.end_date)) as 'Czas_trwania_turnieju[min]',count(*) from tournaments inner join games on tournaments.game_id=games.game_id GROUP BY games.title ORDER BY SUM(TIMESTAMPDIFF(MINUTE,tournaments.start_date,tournaments.end_date)) DESC")
                X= cs.fetchall()
                sr=[]
                for i in range(len(X)):
                        sr.append((X[i][0],round(X[i][2]/X[i][3],2)))
                kategorie = [sr[i][0] for i in range(len(sr))]
                wartosci = [sr[i][1] for i in range(len(sr))]
                plt.bar(kategorie,wartosci)
                plt.title("Wykres słupkowy średniego czasu turniejów")
                plt.xlabel('Id gry')
                plt.ylabel('Minuty')
                plt.show()

def top_10_clients(tab=True,wykres=True):
        cs = con.cursor()
        cs.execute("select payment.customer_id,customers.first_name,customers.last_name,sum(amount),count(*) from payment inner join customers on payment.customer_id=customers.customer_id GROUP by payment.customer_id ORDER by sum(amount) DESC")
        X = cs.fetchall()

        if tab==True:
                top10=X[:10]
                tabela=pd.DataFrame(top10,columns=["Id_klienta","Imię","Nazwisko","Suma","Ilość płatności"])
                print(tabela)

        if wykres == True:
                sr=[]
                for i in range(len(X)):
                        sr.append((X[i][0],round(X[i][3]/X[i][4],2)))
                kategorie = [sr[i][0] for i in range(len(sr))]
                wartosci = [sr[i][1] for i in range(len(sr))]
                plt.bar(kategorie,wartosci)
                plt.title("Średnia wartość transakcji klienta")
                plt.xlabel("Id klietna")
                plt.ylabel("Kwota")
                plt.show()
                

if __name__ == "__main__":
        import itertools
        import mysql.connector
        import pandas as pd
        import matplotlib.pyplot as plt

        con = mysql.connector.connect(
                host = "giniewicz.it",
                user = "team04",
                password = "te@m0a",
                database = "team04",
                )
        if not con:
                raise Exception("connection error")
        
        print("\n                 Employee of the month ")
        print(staff_ranking(),"\n")

        print("\n                 Top10 players")
        print(top_10_tournament_players(g_id=1),"\n")
        
        print("\n                  Top5 games earning by rental")
        print(top5_selers_AND_rental()[0],"\n")

        print("\n                 Top 5 best-selling games")
        print(top5_selers_AND_rental()[1],"\n")

        #Najdluższy czas wynajmowania
        days_rental()
        #Najdłuższy oraz średni czas turnieju
        longest_tournament()
        #Top_10 najwięcej wydających klientów, oraz wykres średniej wszystkich transakcji.
        top_10_clients()
        
        con.close()