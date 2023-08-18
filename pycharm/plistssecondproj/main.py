file_input = input('file name : ')
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


