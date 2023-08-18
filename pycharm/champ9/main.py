notes = open("" + r"C:\Users\drewg\OneDrive\Desktop\mbox.txt", "r")
Emails = []

count = 0
for line in notes:
    # print(line)
    if line.startswith("From "):
        count = count + 1
        wtf = line.split()
        email = wtf[1]
        email = email.rstrip()
        Emails.append(email)
# print(Emails)
for email in Emails:
    email = email.rstrip()
    print(email)
print("There were " + str(count) + " lines in the file with From as the first word")

count = 0
counts = dict()


for swag in Emails:
    counts[swag] = counts.get(swag, 0) + 1
print("hi")
print(counts)

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)
