"""
Seed your database with test values 
"""

import sqlite3
import pudb

db = 'rpg.db'

connection = sqlite3.connect(db)
c = connection.cursor()

monsters = [
    ["red", "scary","2","7","5","4"],
    ["blue", "not scary","4","74","9","0"]
]

print("Destroying old data")
c.execute("DELETE FROM monster")

# pu.db
for monster in monsters:
    c.execute("""
        INSERT INTO monster ("color", "kind", "id_num", "life", "scare", "limbs") VALUES (?, ?, ?, ?, ?, ?)""",(monster[0], monster[1], monster[2], monster[3], monster[4], monster[5]))


characters = [
	["Jack", "21", "M", "Killer", "5", "janteby1", "password", "7/5/13"]
]

c.execute("DELETE FROM character")

for character in characters:
    c.execute("""
        INSERT INTO character ("player_name", "age", "gender", "char_name", "life", "username", "password", "lastSaveDate") VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",(character[0], character[1], character[2], character[3], character[4], character[5], character[6], character[7]))


connection.commit()
c.close()

print ("Added all new data")
print("Looks like we're all good")

