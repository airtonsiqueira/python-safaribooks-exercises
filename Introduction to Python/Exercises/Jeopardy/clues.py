import sqlite3
db = 'Jeopardy/jeopardy.db'


connection = sqlite3.connect(db)

# Necessita de um cursor pra executar as queries
cursor = connection.cursor()
cursor.execute('SELECT text, answer, value FROM clue LIMIT 10')
results = cursor.fetchall()


for clue in results:
    text = clue[0]
    answer = clue[1]
    value = clue[2]

    print("[%s]" % (value))
    print("Question: %s" % (text))
    print("Answer: %s" % (answer))
    print("")

connection.close()
