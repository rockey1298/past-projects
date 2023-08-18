file_counts = {"jpg": 10, "txt": 14, "csv": 2, "py": 23}
for extension in file_counts:
    print(extension)
for ext, amount in file_counts.items():
    print(f"there are {amount} files with the .{ext} extension")
print(file_counts.keys())
print(file_counts.values())


def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result


print(count_letters("andrew"))
