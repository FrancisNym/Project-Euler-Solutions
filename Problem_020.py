def Solution():
    total = 1
    for i in range(1,100):
        total *= i
    strtotal = str(total)
    sum = 0
    for i in strtotal:
        sum += int(i)
    return sum

print(Solution())