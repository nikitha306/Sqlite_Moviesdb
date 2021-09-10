import sqlite3

conn = sqlite3.connect('favmovies.db')

#creating a cursor
c = conn.cursor()

many_movie = []
line=input("Enter your favourite movies:(ID,Name,Actor,Actress,Director,Year)")

while(line !=''):
  many_movie.append(tuple(map(str,line.split(","))))
  line=input()

print(many_movie)

movieids=[]
              
c.executemany("INSERT INTO movie VALUES(?,?,?,?,?,?)",many_movie)

print("Command Executed successfully.....")



#commit the command
conn.commit()

#close our cinnection
conn.close()