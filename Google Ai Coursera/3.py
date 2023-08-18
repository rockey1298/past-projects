def pig_latin(text):
    newlist = []
    newstring = str
    say = text.split()
    # print(say)
    for s in say:
        # print(s)
        # print(s[0])
        start = s[0]
        end = start + "ay"
        # print(end)
        myw = s[1:]
        mys = s[-1]
        mys = end
        final = myw + mys
        newlist.append(final)
        herewego = " ".join(newlist)
    return herewego


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
print(
    pig_latin("programming in python is fun")
)  # Should be "rogrammingpay niay ythonpay siay unfay"
