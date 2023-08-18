'''
Write a program that prompts for a file name, then opens that file and reads through the file,
 and print the contents of the file in upper case. Use the file words.txt to produce the output below.
'''
#trying some way to import file
open(r'C:\Users\drewg\OneDrive\Desktop\coursearaassignment.txt')


import filecmp
#this first line is bullshit but needs to work for assignment maybe, now we are going to focus on readline shit
file_input = input('File name : ')
f = open(''+r'C:\Users\drewg\OneDrive\Desktop\coursearaassignment.txt', 'r')
#print(f.read())
for line in f:
    line=line.strip()
    line=line.upper()
    print(line)

