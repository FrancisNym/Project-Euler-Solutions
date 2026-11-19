def generate_factorial(num):
    total = 1
    for i in range(1,num+1):
        total *= i
    return total


def Solution():
    factorials = []
    sum = 0
    for i in range(0,10):
        factorials.append(generate_factorial(i))
    for i in range(3, generate_factorial(9)*7):
        factotal = 0
        strnum = str(i)
        for j in str(i):
            factotal += factorials[int(j)]
        if factotal == i:
            sum += i
            print(i)
    print(sum)

Solution()