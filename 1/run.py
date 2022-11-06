Out = []
with open("input.txt", "r") as file:
    for line in file.readlines():
        oversplit = line.split(",")
        for number in oversplit:
            Out.append(int(number))
    Out.sort()

with open("output.txt", "w") as file:
    l=len(Out)
    for i in Out:
        file.write(str(i))
        l = l - 1
        if l > 0:
            file.write(", ")

