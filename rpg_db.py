import sqlite3

connection = sqlite3.connect('rpg.db')

connection.execute(
    """
    DROP TABLE IF EXISTS monster;
    """
)
connection.execute(
    """
    DROP TABLE IF EXISTS weapon;
    """
)
connection.execute(
    """
    DROP TABLE IF EXISTS character;
    """
)

connection.execute(
    """
    CREATE TABLE monster (
        id INTEGER PRIMARY KEY, 
        color TEXT,
        kind TEXT,
        id_num INTEGER,
        life INTEGER,
        scare INTEGER,
        limbs INTEGER
    )
    """
)

connection.execute(
    """
    CREATE TABLE weapon (
        id INTEGER PRIMARY KEY, 
        color TEXT,
        kind TEXT,
        harm INTEGER,
        description TEXT,
        id_num INTEGER
    )
    """
)

connection.execute(
    """
    CREATE TABLE character (
        char_ID INTEGER PRIMARY KEY, 
        mid INTEGER,
        wid INTEGER, 
		player_name TEXT,
		age INTEGER,
		gender TEXT,
		char_name TEXT,
		life INTEGER,
		username TEXT,
		password TEXT,
		lastSaveDate DATE,
		FOREIGN KEY(wid) REFERENCES weapons(id),
		FOREIGN KEY (mid) REFERENCES monster(id) 
	)
    """
)

connection.commit()
connection.close()

print("Your database was created")
