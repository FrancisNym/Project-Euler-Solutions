def Solution():
    total = 1
    i = 1
    gap = 2
    while i <1001**2:
        current_sum = (i+gap) + (i+(2*gap)) + (i+(3*gap)) + (i+(4*gap))
        total += current_sum
        i = i+(4*gap)
        gap += 2
    return total

print(Solution())