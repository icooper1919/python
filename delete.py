import re, schedule, time, sqlite3
import pandas as pd
from sqlite3 import Error
from urllib.request import urlopen
from datetime import date

conn = sqlite3.connect("rates.db")
print("SQLite Version: ",sqlite3.version)
c = conn.cursor()

print("OK 1")
        
c.execute('''DELETE FROM interest_rates WHERE Day=063022;''')
        
print("OK 2")
        
      
        
#df = pd.DataFrame(c.fetchall(), columns=['Day','Ford Rate','Toyota Rate'])
        
#print(df)
        
conn.commit()