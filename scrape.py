from bs4 import BeautifulSoup
from urllib2 import urlopen
from flask import Flask , render_template
from flask import abort
app = Flask(__name__)

import sqlite3

#exception error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/users/<username>')
def users(username):
	if username == "dhruv":
		return "<h1> Hello " + username  + "</h1>"
	abort(404)


@app.route('/seen')
def seen():
	with sqlite3.connect('imdb.db') as connection:
		c = connection.cursor()
		cur = c.execute(' SELECT * from movies ')
		all_movies = [dict(title = row[0] , rating = row[1]) for row in cur.fetchall()]
		return render_template('seen.html' , all_movies = all_movies)

@app.route('/series')
def series():
	url = urlopen("http://www.imdb.com/chart/toptv/?ref_=nv_tvv_250_3")
	soup = BeautifulSoup(url)

	name = []
	for link in soup.find_all('td' , class_ = 'titleColumn'):
		name.append(link.a.string)

	rating = []
	for link in soup.find_all('td' , class_ = 'ratingColumn imdbRating'):
		rating.append(link.strong.string)

	with sqlite3.connect("imdb.db") as connection:
		c = connection.cursor()
		cur = c.execute("""SELECT * from series """ )
		all_names = [dict(title=row[0], rating=row[1]) for row in cur.fetchall()]

		# print "currently in database"
		# for i in range(len(all_names)):
		# 	print all_names[i]['title']

		for i in range(len(name)):
			show_name = name[i]

			found = False
			for j in range(len(all_names)):
				if show_name == all_names[j]['title']:
					found = True
					break
			if not found:
				print "New series in top 250"
				print name[i],
				print rating[i]
				c.execute("INSERT INTO series VALUES(? , ?)", (name[i] , rating[i]) )
	return "series"

@app.route('/movies')
def movies():
	url = urlopen("http://www.imdb.com/chart/top?ref_=nv_mv_250_6")
	soup = BeautifulSoup(url)

	name = []
	for link in soup.find_all('td' , class_ = 'titleColumn'):
		name.append(link.a.string)

	rating = []
	for link in soup.find_all('td' , class_ = 'ratingColumn imdbRating'):
		rating.append(link.strong.string)

	with sqlite3.connect("imdb.db") as connection:
		c = connection.cursor()
		cur = c.execute("""SELECT * from movies """ )
		all_names = [dict(title=row[0], rating=row[1]) for row in cur.fetchall()]

		# print "currently in database"
		# for i in range(len(all_names)):
		# 	print all_names[i]['title']

		for i in range(len(name)):
			show_name = name[i]

			found = False
			for j in range(len(all_names)):
				if show_name == all_names[j]['title']:
					found = True
					break
			if not found:
				print "New movie in top 250"
				print name[i],
				print rating[i]
				c.execute("INSERT INTO movies VALUES(? , ?)", (name[i] , rating[i]) )
	return "movies"

@app.route('/')
def welcome():
    return render_template('welcome.html')  # render a template


if __name__ == '__main__':
	app.run(debug = True)
	# series()
	# movies()
# database = connect_db()
# c = database.cursor()
# for i in range(10):
# 	print "executing"
# 	c.execute('INSERT INTO imdb VALUES(1 , 1)')