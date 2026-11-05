# Longest collatz chain by a number under 1mill

def LengthCollatzChain(num):
    steps = 0
    while num != 1:
        if num % 2 ==0:
            num //= 2
        else:
            num = 3*num +1
        steps += 1
    return steps



def Solution():
    max = 0
    maxnum = 0
    for i in range(1,1000000):
        if max < LengthCollatzChain(i):
            max = LengthCollatzChain(i)
            maxnum = i
    return maxnum

print(Solution())