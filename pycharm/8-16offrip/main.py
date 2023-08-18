'''
Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered,
 print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with
  a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.


'''
#list to store user variables into
user_list = []
#asking for user input to store into array

#need a loop to get user information and then break when done, unless they say done number goes into array
i = 1
while i < 5:
    userinput = input('please enter a number or say done')
    if userinput == 'done':
        break
    elif userinput.isdigit():
        try:
            userinputtoint = int(userinput)
        except:
            print('Invalid output')
        user_list.append(userinputtoint)
    else :
        print('Invalid input')

'''     # checking array here
for number in user_list:
    print(number)
'''
max_number = 0
min_number = 0


# my attempt at finding max number here, need to find way to convert array to int
for number in user_list:
    if max_number == 0:
        max_number = number
    if number > max_number:
        max_number = number
print('Maximum is ' + str(max_number))

for zebra in user_list:
    if min_number == 0:
        min_number = zebra
    if zebra < min_number:
        min_number = zebra
print('Minimum is ' + str(min_number))




'''
def computepay(x, y):
    #print(x, y)
    hour = int(x)
    payr = float(y)
    if hour > 40:
        total = 40 * 10.50 + (hour - 40) * (payr * 1.5)
        return total
    else:
        total = x * y
        return total


h = input('Enter Hours:')
p = input('Enter Payrate:')
total = computepay(h, p)
print('Pay ' + str(total))
'''