import sqlite3

connection = sqlite3.connect('Jeopardy/jeopardy.db')

# Necessita de um cursor pra executar as queries
cursor = connection.cursor()
cursor.execute('SELECT name FROM category LIMIT 10')
results = cursor.fetchall()


for result in results:
    print(result[0])
connection.close()
