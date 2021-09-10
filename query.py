import sqlite3

conn = sqlite3.connect('favmovies.db')

#creating a cursor
c = conn.cursor()

#Query the database
c.execute("SELECT * FROM movie")
movie=c.fetchall()
print("MOVIE_ID"+"\t\tTITLE"+"\t\tACTOR"+"\t\tACTRESS"+"\t\tDIRECTOR"+"\t\tYEAR")
print("--------------------------------------------------------------------------------------------")
for movies in movie:
	print(movies[0]+"\t"+movies[1]+"\t"+movies[2]+"\t"+movies[3]+"\t"+movies[4]+"\t"+str(movies[5]))





#commit the command
conn.commit()

#close our cinnection
conn.close()
