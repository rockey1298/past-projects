'''
Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
 The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
 After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''

notes = open('' + r'C:\Users\drewg\OneDrive\Desktop\mbox.txt', 'r')
Emails = []
count = 0
for line in notes :
    #print(line)
    if line.startswith('From '):
        count = count + 1
        wtf = line.split()
        email = wtf[1]
        email = email.rstrip()
        emaillist = Emails.append(email)
#print(Emails)
for email in Emails:
    email = email.rstrip()
    print(email)
print('There were '+str(count)+' lines in the file with From as the first word')


counts = dict()
for line in notes :
    if line.startswith('From '):
        count = count + 1
        wtf = line.split()
        email = wtf[1]
        email = email.rstrip()
        emaillist = Emails.append(email)
        for word in wtf:
            counts[word] = counts.get(word, 0) + 1

bigcount = str
bigword = str

for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
