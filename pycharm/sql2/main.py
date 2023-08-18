import sqlite3
conn = sqlite3.connect('projectdatabasedb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

fname = 'mbox.txt'

fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM counts WHERE email = ? ', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (email, count) VALUES (?, 1)', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
    conn.commit()

sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.execute('DROP TABLE IF EXISTS works')

cur.execute('CREATE TABLE Works (org TEXT, c INTEGER)')

newfh = open('mbox.txt')

for line in newfh:
    if not line.startswith('From: '): continue
    newpieces = line.split()
    #print(newpieces[1])
    wow = newpieces[1].split('@',)
    print(wow[1])
    wow = wow[1]
    cur.execute('SELECT c FROM works where org = ? ', (wow,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO works (org, c) VALUES (?,1)', (wow,))
    else:
        cur.execute('UPDATE works SET c = c + 1 WHERE org = ?', (wow,))
    conn.commit()









