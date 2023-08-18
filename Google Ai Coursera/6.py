def groups_per_user(group_dictionary):
    user_groups = {}
    for value, key in group_dictionary.items():
        for k in key:
            user_groups[k] = value
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
