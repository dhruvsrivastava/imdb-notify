import sqlite3

with sqlite3.connect("imdb.db") as connection:
#creates database if it does not exist
	c = connection.cursor()
	# c.execute('DROP TABLE show')
	# c.execute('DROP TABLE series')
	c.execute('CREATE TABLE IF NOT EXISTS movies(title TEXT , rating FLOAT(1) ) ')
	c.execute('CREATE TABLE IF NOT EXISTS series(title TEXT , rating FLOAT(1) ) ')
