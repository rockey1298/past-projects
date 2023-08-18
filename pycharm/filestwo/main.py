#trying some way to import file
open(r'C:\Users\drewg\OneDrive\Desktop\cemails.txt')

total = float(0)
count = 0
import filecmp
#this first line is bullshit but needs to work for assignment maybe, now we are going to focus on readline shit
file_input = input('File name : ')
f = open(''+r'C:\Users\drewg\OneDrive\Desktop\cemails.txt', 'r')
#print(f.read())
for line in f:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    count = count + 1
    #print(line)
    line = line[21:]
    #print(line)
    liner=float(line)
    total = total + liner
#print(total)
#print(count)
final = total / count
final = str(final)
print('Average spam confidence: ' + final)
