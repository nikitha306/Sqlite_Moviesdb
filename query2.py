import sqlite3

conn = sqlite3.connect('favmovies.db')

#creating a cursor
c = conn.cursor()
#Query to find movies released in 2009
c.execute("SELECT * FROM movie WHERE Year='2009'")

movies = c.fetchall()

for movie in movies:
	print(movie)

#Query to find movies released after 2011
c.execute("SELECT * FROM movie WHERE Year >'2011'")
movies = c.fetchall()

for movie in movies:
	print(movie)


#commit the command
conn.commit()

#close our cinnection
conn.close()
