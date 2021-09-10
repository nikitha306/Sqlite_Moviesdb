import sqlite3

conn = sqlite3.connect('favmovies.db')

#creating a cursor
c = conn.cursor()

#creating a table
c.execute("""CREATE TABLE movie(
                ID VARCHAR PRIMARY KEY,
		 		Title TEXT NOT NULL UNIQUE, 
		 		Actor TEXT,
		 		Actress TEXT,
		 		Director TEXT,
		 		Year INT
		) """)


#commit the command
conn.commit()

#close our cinnection
conn.close()
