import sqlite3

connect = sqlite3.connect('rpg.db')
print ("Opened database successfully")

cursor = connect.execute("SELECT id, color, kind, id_num, life, scare, limbs FROM monster")

for row in cursor:
	print ("Monster")
	print ("ID = ", row[0])
	print ("COLOR = ", row[1])
	print ("KIND = ", row[2])
	print ("ID_num = ", row[3])
	print ("LIFE = ", row[4])
	print ("SCARE = ", row[5])
	print ("LIMBS = ", row[6], "\n")

cursor = connect.execute("SELECT id, color, kind, harm, description FROM weapon")

for row in cursor:
	print ("Weapon")
	print ("ID = ", row[0])
	print ("COLOR = ", row[1])
	print ("KIND = ", row[2])
	print ("HARM = ", row[3])
	print ("Description = ", row[4], "\n")


cursor = connect.execute("SELECT char_ID, mid, wid, player_name, age, gender, char_name, life, username, password, lastSaveDate FROM character")

for row in cursor:
	print ("Character Info")
	print ("CHARACTER ID = ", row[0])
	print ("MONSTER ID = ", row[1])
	print ("WEAPON ID = ", row[2])
	print ("PLAYER NAME = ", row[3])
	print ("PALYER AGE = ", row[4])
	print ("GENDER = ", row[5])
	print ("CHARACTER NAME = ", row[6])
	print ("LIVES = ", row[7])
	print ("USER NAME = ", row[8])
	print ("PASSWORD = ", row[9])
	print ("LAST SAVED DATE = ", row[10], "\n")

cursor = connect.execute("SELECT id, name, age FROM test")

for row in cursor:
	print ("Test Info")
	print ("CHARACTER ID = ", row[0])
	print ("NAME = ", row[1])
	print ("AGE = ", row[2])

print ("Operation done successfully")
connect.close()







