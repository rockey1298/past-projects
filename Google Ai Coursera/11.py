def format_address(address_string):
    # Declare variables
    mysplit = address_string.split()
    mynum = mysplit[0:1]
    myform = mysplit[1:]
    mynum = " ".join(mynum)
    myform = " ".join(myform)
    # print(mysplit)
    mystr = f"house number {mynum} on street named {myform}"
    return mystr


# Separate the address string into parts


print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"
