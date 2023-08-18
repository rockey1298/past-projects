
"""
cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = 'mbox.txt'


cur.execute('DROP TABLE IF EXISTS works')

#cur.execute('CREATE TABLE Works (org TEXT, c INTEGER)')

newfh = open('mbox.txt')

for line in newfh:
    if not line.startswith('From: '): continue
    newpieces = line.split()
    #print(newpieces[1])
    wow = newpieces[1].split('@',)
    print(wow[1])
    wow = wow[1]
    cur.execute('SELECT count FROM Counts where org = ? ', (wow,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?,1)', (wow,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (wow,))
    conn.commit()
"""
import sqlite3
conn = sqlite3.connect('projectdatabasedb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Xml')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

