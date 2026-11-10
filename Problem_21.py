def sum_proper_divisors(num):
    proper_divisors = [1]
    for i in range(2,int((num**0.5))+1):
        if num % i == 0:
            proper_divisors.append(i)
            proper_divisors.append(num//i)
    return sum(proper_divisors)

def Solution():
    amicable_numbers = []
    for i in range(2,10000):
        sumi = sum_proper_divisors(i)
        if sum_proper_divisors(sumi) == i and sumi != i:
            amicable_numbers.append(i)
    return sum(amicable_numbers)

print(Solution())