'''
Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
 Convert the extracted value to a floating point number and print it out.

'''
#starting text
text = "X-DSPAM-Confidence:    0.8475"
#find statement
found = text.find('0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' or '10')
# print found index of start of number
print(found)
# slice object
x = slice(found, ' ')
#x = str(x)
str1 = ""
str1=text[x]

print(type(x))
# lets try to convert to float
x = int(x)
# trying to print out the slice , from start of found to a white space
print(str1)

foundset = text.find(' ', found)

print(foundset)


