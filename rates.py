import re, schedule, time, sqlite3
import pandas as pd
from sqlite3 import Error
from urllib.request import urlopen
from datetime import date

today = date.today().strftime("%m%d%y")

toyota_url = "https://www.incomedrivernotes.com/en.html#faqs"
toyota_page = urlopen(toyota_url)
toyota_html = toyota_page.read().decode('utf-8')
toyota_rate = re.search(r"\d\.\d\d%", toyota_html).group().split("%")
trate = float(toyota_rate[0])

ford_url = "https://www.ford.com/finance/investor-center/ford-interest-advantage/"
ford_page = urlopen(ford_url)
ford_html = str(ford_page.read().decode('utf-8'))
ford_lst_rate = re.search(r"\$50,000</p>\n</td>\n                    <td><p>\d\.3\d%", ford_html).group().split("<p>")
ford_rate = ford_lst_rate[1].split("%")
frate = float(ford_rate[0])

print("Today's date: ", today)
print("Toyota rate is", trate)
print("Ford rate is", frate)

sql_array = [today, frate, trate]

def save_in_db(database_name):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(database_name)
        print("SQLite Version: ",sqlite3.version)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS interest_rates
            ([day], [ford_rate], [toyota_rate])
            ''')
        
        print("OK 1")
        
        c.execute('''
            INSERT INTO interest_rates VALUES (?, ?, ?)''', sql_array)
        
        print("OK 2")
        
        sql_query = pd.read_sql_query ('''SELECT * FROM interest_rates''', conn)

        df = pd.DataFrame(sql_query, columns = ['Day', 'Ford Rate', 'Toyota Rate'])
        print (df)  
        
#        df = pd.DataFrame(c.fetchall(), columns=['Day','Ford Rate','Toyota Rate'])
        
#        print(df)
        
        conn.commit()        
        
    except Error as e:
        print("Error: ",e)
    finally:
        if conn:
            conn.close()
    
save_in_db("rates.db")
