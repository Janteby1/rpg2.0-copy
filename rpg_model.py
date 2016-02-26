# this file should have everyhting the game interacts with DB  or API

import sqlite3
db = 'rpg.db'

connection = sqlite3.connect(db)
c = connection.cursor()

class CharacterModel:
	# no init function, all the attributes are given using input statments   
	def insert(life, name, gender, fighter, age, username, password):
		c.execute("""
	        INSERT INTO character ("life", "player_name","gender", "char_name", "age", "username", "password") 
	        VALUES (?, ?, ?, ?, ?, ?, ?)"""
	        ,(life, name, gender, fighter, age, username, password))
		connection.commit()

	def print_info():
		cursor = connection.execute("SELECT player_name, age, gender, char_name, life, username, password FROM character")
		i =0
		while i < 1:
			for row in cursor:
				print(" ")
				print (" --- DATABASE ---")
				print ("Character Info")
				print ("PLAYER NAME = ", row[0])
				print ("PALYER AGE = ", row[1])
				print ("GENDER = ", row[2])
				print ("CHARACTER NAME = ", row[3])
				print ("LIVES = ", row[4])
				print ("USERNAME = ", row[5])
				print ("PASSWORD = ", row[6])
				print (" --- --- --- ")
			i +=1

	def update_life (life):
		c.execute("""
			UPDATE Character
			SET life=life;
			"""
		)
		connection.commit()

	def print_keys():
		cursor = connection.execute("SELECT mid, wid FROM character")
		i =0
		while i < 1:
			for row in cursor:
				print (" ")
				print (" --- DATABASE ---")
				print ("Keys")
				print ("Monster FK = ", row[0])
				print ("Weapon FK = ", row[1], "\n")
			i +=1


class MonsterModel:
	# no init function, all the attributes are given using input statments   
	def insert(color, life, scare, kind, id_num):
		c.execute("""
	        INSERT INTO monster ("color", "life","scare", "kind", "id_num") 
	        VALUES (?, ?, ?, ?, ?)"""
	        ,(color, life, scare, kind, id_num))
		connection.commit()

	def print_info():
		cursor = connection.execute("SELECT color, life, scare, kind, id_num FROM monster")
		i =0
		while i < 1:
			for row in cursor:
				print (" ")
				print (" --- DATABASE ---")
				print ("Monster Stats")
				print ("COLOR = ", row[0])
				print ("LIFE = ", row[1])
				print ("SCARE = ", row[2])
				print ("KIND = ", row[3])
				print ("ID_Num = ", row[4])
				print (" --- --- --- ")
			i +=1

	def update_monster(mid):
		c.execute("""
			UPDATE Character
			SET mid=mid;
			"""
		)
		connection.commit()

	def update_life(life):
		c.execute("""
			UPDATE monster
			SET life = life;
			"""
		)
		connection.commit()


class WeaponModel:
	# no init function, all the attributes are given using input statments   
	def insert(color, kind, harm, description, id_num):
		c.execute("""
	        INSERT INTO weapon ("color", "kind","harm", "description", "id_num") 
	        VALUES (?, ?, ?, ?, ?)"""
	        ,(color, kind, harm, description, id_num))
		connection.commit()

	def print_info():
		cursor = connection.execute("SELECT color, kind, harm, description, id_num FROM weapon")
		i =0
		while i < 1:
			for row in cursor:
				print (" ")
				print (" --- DATABASE ---")
				print ("Weapon Stats")
				print ("COLOR = ", row[0])
				print ("KIND = ", row[1])
				print ("HARM = ", row[2])
				print ("DESCRIPTION = ", row[3])
				print ("ID_Num =", row[4])
				print (" --- --- --- ")
			i +=1

	def update_weapon(wid):
		c.execute("""
			UPDATE Character
			SET wid= wid;
			"""
		)
		connection.commit()



