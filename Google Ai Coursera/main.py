import re


def multiplication_table(start, stop):
    for x in range(start, stop + 1):

        for y in range(start, stop + 1):
            print("printing x: " + str(x))
            print("printing y: " + str(y))
            print("~~~~~")


nl = []


def even_numbers(maximum):
    mystring = ""
    for r in range(2, maximum + 1, 2):
        nl.append(" " + str(r))
        mystring = "".join(nl)
    # print("range of numbers : ")
    # print(nl)
    return mystring


# using regular expression to select the last time 'old' is in the string
# and replacing it with 'new'
def replace_ending(sentence, old, new):
    if old in sentence:
        sentence = re.sub(old + "$", new, sentence)
        return sentence
    else:
        return sentence


def get_word(s, n):
    if n > 0:
        words = s.split()
        # print(words)
        if n <= len(words):
            return words[n - 1]
        else:
            return
    else:
        return


def skip_elements():
    pass


print(
    skip_elements(["a", "b", "c", "d", "e", "f", "g"])
)  # Should be ['a', 'c', 'e', 'g']
print(
    skip_elements(["Orange", "Pineapple", "Strawberry", "Kiwi", "Peach"])
)  # Should be ['Orange', 'Strawberry', 'Peach']

# print(get_word("This is a lesson about lists", 4))  # Should print: lesson
# print(get_word("This is a lesson about lists", -4))  # Nothing
# print(get_word("Now we are cooking!", 1))  # Should print: Now
# print(get_word("Now we are cooking!", 5))  # Nothing

# print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# # Should display "It's raining cats and dogs"
# print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# # Should display "She sells seashells by the seashore"
# print(replace_ending("The weather is nice in May", "may", "april"))
# # Should display "The weather is nice in May"
# print(replace_ending("The weather is nice in May", "May", "April"))
# # Should display "The weather is nice in April"

# multiplication_table(1, 3)

# print(even_numbers(6))  # Should be 2 4 6
# print(even_numbers(10))  # Should be 2 4 6 8 10
# print(even_numbers(1))  # No numbers displayed
# print(even_numbers(3))  # Should be 2
# print(even_numbers(0))  # No numbers displayed
