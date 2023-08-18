def guest_list(guests):
    for g in guests:
        # print(g)
        print(f"{g[0]} is {g[1]} years old and works as a {g[2]}")


guest_list([("Ken", 30, "Chef"), ("Pat", 35, "Lawyer"), ("Amanda", 25, "Engineer")])
