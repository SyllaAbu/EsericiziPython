import sqlite3
import requests

id = input('Inserisci un id: ')

json = requests.get(f'https://api.rawg.io/api/games/{id}').json()
print(json)

conn = sqlite3.connect('database.db')
cur = conn.cursor()

try:
    cur.execute('INSERT INTO GamesDetails VALUES(?,?,?,?,?,?,?)', (json['id'], json['slug'], json['name'], json['name_original'], json['description'], json['metacritic'], json['released'],))
    conn.commit()
except:
    print('Già presente')
