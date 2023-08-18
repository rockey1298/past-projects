fhand = open('' + r'C:\Users\drewg\OneDrive\Desktop\mbox.txt', 'r')
counts = dict()
ass = dict()
# for line i
for line in fhand:
    words = line.split()
    # this is the part adding each element of split to dictionary for each occurrence
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        #print('counting!')
    # i think my problem lies here for now
    if line.startswith('From '):
        hours = line.split()
        #prints whole line starting with from
        print(hours)
        # extracts the days:hours:minutes string from the split
        test = hours[5]
        print(test[:2])
        # setting it to variable so i can try to create histogram
        working = test[:2]
        print('hello')
        # think im fucking up here now,
        ass[working] = ass.get(working, 0) + 1

# making list to manipulate dictionary objects
lst = list()
mylst = list()
# adding dictionary elements to list !
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
# now we have value,key and instead of key,value in a list instead of dictionary, so if we reverse it we now have the largest 10 values instead of keys
lst = sorted(lst, reverse=True)
for val, key in lst[:10]:
    print(key, val)

# here is my go at it, ass dictionary should only contain messages that start with from

for k, v in ass.items():
    mytup = (k, v)
    mylst.append(mytup)
    print('my tupile!')
    print(mytup)
# now we have value,key and instead of key,value in a list instead of dictionary, so if we reverse it we now have the largest 10 values instead of keys
mylst = sorted(mylst)
for k, v in mylst:
    print(k, v)
