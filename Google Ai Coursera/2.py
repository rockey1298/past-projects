filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
mysplits = []
oops = []
newfilenames = []
for f in filenames:
    mysplits.append(f.split("."))
for m in mysplits:
    # print(m[1])
    if m[1] == "hpp":
        m[1] = "h"
    # print(m[1])
    oops.append(m)
# print(oops)
for f in oops:
    f = ".".join(f)
    # print(f)
    newfilenames.append(f)
print(newfilenames)


# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
