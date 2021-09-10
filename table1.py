import sqlite3

conn = sqlite3.connect('favmovies.db')

#creating a cursor
c = conn.cursor()

many_movie = [
                    ('1','The intern','Robert','Anne Hathway','Nancy','2013'),
                    ('2','The blind side','Quinton','Sandra','John Lee','2009'),
                    ('3','Wake up Sid','Ranbir','Konkana','Ayan','2009'),
                    ('4','Gippi','Taash','Riya','Sonam','2013'),
           
                ]
c.executemany("INSERT INTO movie VALUES(?,?,?,?,?,?)",many_movie)

print("Command Executed successfully.....")



#commit the command
conn.commit()

#close our cinnection
conn.close()