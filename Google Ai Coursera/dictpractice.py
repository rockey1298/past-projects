def email_list(domains):
    email = []
    # print(domains.keys())
    # print(domains.values())
    # for value, key in domains.items():
    #     email.append(f"{key}{value}")

    # for v in domains.values():
    #     print(f"{v}")
    # for f in domains.keys():
    #     print(f"{f}")

    # for k in domains.keys():
    #     email.append(k)
    #     for v in domains.values():
    #         email.append(v)

    for value, keys in domains.items():
        for key in keys:
            email.append(key + "@" + value)

    return email


print(
    email_list(
        {
            "gmail.com": ["clark.kent", "diana.prince", "peter.parker"],
            "yahoo.com": ["barbara.gordon", "jean.grey"],
            "hotmail.com": ["bruce.wayne"],
        }
    )
)
