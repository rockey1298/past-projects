def groups_per_user(group_dictionary):
    user_groups = {}
    mylist = []
    for value, key in group_dictionary.items():
        for k in key:
            if k not in mylist:
                mylist.append(k)
                user_groups[value] = mylist
        mylist = []

    return user_groups


print(
    groups_per_user(
        {
            "local": ["admin", "userA"],
            "public": ["admin", "userB"],
            "administrator": ["admin"],
        }
    )
)
