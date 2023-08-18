


words = []
test = []
file_input = input('file name : ')
notes = open('' + r'C:\Users\drewg\OneDrive\Desktop\plists.txt', 'r')
'''
for line in notes:
    tits = line.split()
    if tits in words:
        print('placeholder has found this line already to be in the array words')
        break
    elif tits is not words:
        words.append(tits)
print(tits)
print(words)
'''
#linelength = len(tits)
#print(linelength)
#for linelength:
#hold1 = tits[0]
#print(hold1)


#print('starting for loop')
for wee in notes:
    tits = wee.split()
    #print('this should happen 4 times')
    i = -1
    for t in tits:
        i = i + 1
        if t in test:
            #print('Already in list')
            continue
        elif t not in test:
            test.append(tits[i])
            #print('added word' + tits[i])
        else:
            continue
test = sorted(test)
print(test)