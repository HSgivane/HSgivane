import sqlite3

con = sqlite3.connect("users.db")
cur = con.cursor()


cur.execute("CREATE TABLE IF NOT EXISTS User ( id serial PRIMARY KEY, username varchar (55) NOT NULL, password varchar (120) NOT NULL );")


cur.execute("SELECT * FROM User WHERE username in('ya')")

records = str(cur.fetchall())

print(records)

con.commit()