import sqlite3
# Settings
db = "Jeopardy/jeopardy.db"
connection = sqlite3.connect(db)
cursor = connection.cursor()

# Queries
query1 = "SELECT game FROM category ORDER BY RANDOM() LIMIT 1"
query2 = """SELECT name, round FROM category where game=%d ORDER BY round"""

cursor.execute(query1)
results = cursor.fetchall()
game_id = results[0][0]
print(game_id)

query2 = query2 % (game_id)
cursor.execute(query2)
results = cursor.fetchall()
for result in results:
    game_name, game_round = result
    print("Name: %s" % game_name)
    print("Round: %d" % game_round)

connection.close()
