def main():
    global fh
    fh = open("C:\\Users\drewg\Downloads\mbox.txt", "r")
    # print(fh.read())
    # This is going to count all the words in a file
    counting_characters()
    print(counting_words())
    print(counting_thirds())

    fh.close()


# Counters all the characters ina file
def counting_characters():
    counter = 0
    for line in fh:
        for word in line:
            for character in word:
                counter += 1
    print(counter)


def counting_words():
    wordCOUNT = 0
    fh.seek(0)
    for line in fh:
        for word in line.split():
            wordCOUNT += 1
    return wordCOUNT


def counting_thirds():
    list_of_words = ""
    fh.seek(0)
    for line in fh:
        counter = 0
        for word in line:
            counter += 1
            if counter == 3:
                list_of_words += word
    return list_of_words


if __name__ == "__main__":
    main()
