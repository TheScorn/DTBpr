import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import os
from matplotlib.backends.backend_pdf import PdfPages
from Analiza_danych import *
current_path = os.path.dirname(os.path.abspath(__file__))

con = mysql.connector.connect(
                host = "giniewicz.it",
                user = "team04",
                password = "te@m0a",
                database = "team04",
                )
if not con:
                raise Exception("connection error")
cs = con.cursor()

output_path = os.path.join(current_path, 'Analiza.pdf')
pp = PdfPages(output_path)

df = pd.DataFrame(staff_ranking(cs),columns=["Date","Staff_id","First_name","Last_Name","Earn"])
fig, ax =plt.subplots(figsize=(12,12))
plt.title("Pracownicy miesiąca")
ax.axis('tight')
ax.axis('off')
the_table = ax.table(cellText=df.values,colLabels=df.columns,loc='center')
pp.savefig()


df = pd.DataFrame(top_10_tournament_players(cs,g_id=1),columns=["Game_title","First_name","Last_name","Num_of_wins"])
fig, ax =plt.subplots(figsize=(12,12))
ax.axis('tight')
ax.axis('off')
plt.title("Top 10 graczy turniejowych")
the_table = ax.table(cellText=df.values,colLabels=df.columns,loc='center')
pp.savefig()

df = pd.DataFrame(top5_selers_AND_rental(cs)[0],columns=["Game Title", "Sum of rental amount"])
fig, ax =plt.subplots(figsize=(12,4))
ax.axis('tight')
ax.axis('off')
plt.title("Top5 zarabiających gier na wynajmie")
the_table = ax.table(cellText=df.values,colLabels=df.columns,loc='center')
pp.savefig()

df = pd.DataFrame(top5_selers_AND_rental(cs)[1],columns=["Game Title", "Sum of rental amount"])
fig, ax =plt.subplots(figsize=(12,4))
ax.axis('tight')
ax.axis('off')
plt.title("Top5 zarabiających gier na sprzedaży")
the_table = ax.table(cellText=df.values,colLabels=df.columns,loc='center')
pp.savefig()

df=pd.DataFrame(longest_tournament(cs),columns=["id_gry","Tytuł","czas trwania turnieju[min]"])
fig, ax =plt.subplots(figsize=(12,4))
ax.axis('tight')
ax.axis('off')
plt.title("Najdłuższe turnieje")
the_table = ax.table(cellText=df.values,colLabels=df.columns,loc='center')
pp.savefig()

plt.figure()
plt.clf()
plt.bar(longest_tournament_plot(cs)[0],longest_tournament_plot(cs)[1])
plt.title("Wykres słupkowy średniego czasu turniejów")
plt.xlabel('Id gry')
plt.ylabel('Minuty')

pp.savefig()
pp.close()