import sqlite3
conn=sqlite3.connect('music.txt')
cur=conn.cursor()
cur.execute('DROP TABLE IF EXISTS track')
cur.execute('CREATE TABLE track(title TEXT,play INTEGER)')
cur.execute('INSERT INTO track(title,play)VALUES(?,?)',('Darshan Mehnge',25))
cur.execute('INSERT INTO track(title,play)VALUES(?,?)',('Tareyaan De Des',23))
conn.commit()
cur.execute('SELECT * FROM track')
print('TRACKS:-')
for row in cur:
    print(row)

cur.execute('DELETE FROM track WHERE play < 24')
conn.commit()
cur.execute('SELECT title,play FROM track ') # Everytime before printing the result you need to write select command
print(cur)
print('TRACKS AFTER DELETION:-')
for r in cur:
    print(r)

cur.execute('UPDATE track SET play=45 WHERE title=?',('Darshan Mehnge',)) # Always use string outside the expression and use that as tuple with a comma at the last
conn.commit()
print('TRACK AFTER UPDATION:-')
cur.execute('SELECT * FROM track')
for row in cur:
    print(row)

cur.close()
print(cur)