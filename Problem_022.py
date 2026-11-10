def FindAlphabeticalValue(word):
    total_value = 0
    for i in word:
        letter_value = ord(i) - 64
        total_value += letter_value
    return total_value

def Solution():
    with open("Problem_022Data.txt") as file:
        for line in file:
            line = line.strip()
    line = line.split(",")
    for i in range(len(line)):
        line[i] = line[i][1:-1]
    line.sort()
    total = 0
    for i in range(len(line)):
        total += FindAlphabeticalValue(line[i]) * (i+1)
    return total
print(Solution())