def find_cycle_length(num):
    remainders = []
    remainder = 1
    while True:
        remainder = (10*remainder)%num
        if remainder in remainders:
            return len(remainders)
        else:
            remainders.append(remainder)

def Solution():
    max = 0
    maxnum = 0
    for i in range(1,1000):
        current = find_cycle_length(i)
        if current > max:
            max = current
            maxnum = i
    return maxnum

print(Solution())