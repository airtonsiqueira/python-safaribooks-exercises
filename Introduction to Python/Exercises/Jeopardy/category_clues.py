import sqlite3
# Settings
db = "Jeopardy/jeopardy.db"
connection = sqlite3.connect(db)
cursor = connection.cursor()

# Queries
query1 = "SELECT id, name FROM category ORDER BY RANDOM() LIMIT 1"
query2 = """SELECT text, answer, value FROM clue where category=%d ORDER BY value"""

cursor.execute(query1)
results = cursor.fetchall()
category_id, name = results[0]

print(name)

query2 = query2 % (category_id)

cursor.execute(query2)
results = cursor.fetchall()

for clue in results:
    text, answer, value = clue
    print("$[%s]" % value)
    print("Question: %s" % text)
    print("Answer: What is '%s'?" % answer)
    print("")

connection.close()
