def sum_proper_divisors(num):
    proper_divisors = [1]
    for i in range(2,int((num**0.5))+1):
        if num % i == 0:
            proper_divisors.append(i)
            proper_divisors.append(num//i)
    return sum(set(proper_divisors))

def check_abundant(num):
    if sum_proper_divisors(num) > num:
        return True
    else:
        return False

def Solution():
    upper_limit = 28123
    all_abundants = []
    for i in range(1, 28123):
        if check_abundant(i):
            all_abundants.append(i)
    total_sum = (28123*28124)//2
    all_sum_2_abundants = []
    for i in range(len(all_abundants)):
        for j in range(i,len(all_abundants)):
            all_sum_2_abundants.append(all_abundants[i]+all_abundants[j])
    all_sum_2_abundants.sort()
    all_sum_2_abundants = list(set(all_sum_2_abundants))
    for i in range(len(all_sum_2_abundants)):
        if all_sum_2_abundants[i] > 28123:
            index = i
            break
    all_sum_2_abundants = all_sum_2_abundants[:index]
    return total_sum - sum(all_sum_2_abundants)

print(Solution())