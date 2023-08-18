"""
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
print(line.rstrip())


going to go nuts 

words = []
#file_input = input('file name : ')
notes = open('' + r'C:\Users\drewg\OneDrive\Desktop\plists.txt', 'r')
for line in notes:
    line = line.split()
    if line in words:
        print('placeholder has found this line already to be in the array words')
        break
    elif line is not words:
        words.append(line)
print(line)
print(words)

"""
words = []
file_input = input("file name : ")
notes = open('' + r'C:\Users\drewg\OneDrive\Desktop\plists.txt', 'r')
for line in notes:
    line = line.split()
    if line in words:
        print('placeholder has found this line already to be in the array words')
        break
    elif line is not words:
        words.append(line)
print(line)
print(words)