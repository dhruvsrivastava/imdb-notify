import sqlite3

with sqlite3.connect("shows.db") as connection:
#creates database if it does not exist
	c = connection.cursor()
	c.execute('CREATE TABLE show(title TEXT , description TEXT) ')
	# c.execute('INSERT INTO posts VALUES("Good" , "I\'m good")')
	# c.execute('INSERT INTO posts VALUES("Well" , "I\'m well")')

	# c.execute('CREATE TABLE IF NOT EXISTS codes(id INTEGER , code TEXT) ')
	# codeString = 'print "Hello world" '
	# c.execute("INSERT INTO codes VALUES (1, ?)", (codeString,))
	# codeString = 'print "Second code" '
	# c.execute("INSERT INTO codes VALUES (2, ?)", (codeString,))
