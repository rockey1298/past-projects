def skip_elements(elements):
    y = enumerate(elements)
    z = list(y)
    mylist = []
    for element in z:
        # print(element[0])
        if element[0] % 2 == 0:
            # print(element)
            mylist.append(element[1])
        # print(mylist)
        # return mylist
    print(mylist)


print(
    skip_elements(["a", "b", "c", "d", "e", "f", "g"])
)  # Should be ['a', 'c', 'e', 'g']
print(
    skip_elements(["Orange", "Pineapple", "Strawberry", "Kiwi", "Peach"])
)  # Should be ['Orange', 'Strawberry', 'Peach']
