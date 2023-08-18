def group_list(group, users):
    mygroup = group
    myusers = users
    mynewusers = ", ".join(myusers)
    mystring = f"{mygroup}: {mynewusers}"
    return mystring


print(
    group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])
)  # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(
    group_list("Engineering", ["Kim", "Jay", "Tom"])
)  # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", ""))  # Should be "Users:"
