p = input('pay')
h = input('hours')

hour = int



def computepay(x, y):
    hour = int(x)
    payr = float(y)
    if hour > 40:
        total = 420 + (hour - 40) * (payr * 1.5)
        return total
    else:
        total = int(x) * int(y)
        return total


total = computepay(h, p)
print('Pay ' + str(total))
