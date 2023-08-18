# inp = input('Europe Floor?')
# usf = int(inp) + 1
# print('Us floor ' + str(usf))

# hrs = input("enter hours")
# payRate = input('enter payrate')
# grossPay = int(hrs) * float(payRate)
# print(float(grossPay))

# hrs = input("Enter Hours:")
# h = float(hrs)
# payr = input("Enter Payrate:")
# p = float(payr)
# int(h)
# if h > 40:
#    total = 40 * 10.50 + (h-40) * 15.75
#    print(total)
# else:
#    total = h * p
#    print(total)

# score = input("Enter Score: ")
# s = float(score)

# if  s >= .9 :
#    print('A')
# elif s > .8 :
#    print('B')
# elif s > .7:
#    print('C')
# elif s > .6:
#    print('D')
# else :
#    print('F')


# def computepay(x, y):
#    #print(x, y)
#    hour = int(x)
#    payr = float(y)
#    if hour > 40:
#       total = 40 * 10.50 + (hour - 40) * (payr * 1.5)
#       return total
#    else:
#        total = x * y
#        return total


# h = input('hours?')
# p = input('payrate?')
# total = computepay(h, p)
# print('Pay ' + str(total))
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
"""


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
        int(userinput)
        user_list.append(userinput)
    else :
        print('not quite what were looking for')

        # checking array here
for number in user_list:
    print(number)
max_number = None

# my attempt at finding max number here, need to find way to convert array to int
for number in user_list:
    if number > max_number:
        max_number = number
        print(number, max_number)

#find the largest value
largest_so_far = None
print('before')
for the_num in user_list :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('after', largest_so_far)







