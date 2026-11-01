def GetPrimeFactors(num):
    prime_factors = []
    div = 2
    while div <= num**0.5:
        if num % div != 0:
            div += 1
        else:
            num //= div
            prime_factors.append(div)
    if num>1:
        prime_factors.append(num)
    prime_factors.sort()
    return prime_factors

all_factors = [2,3,5,7,11,13,17,19]

def Solution():
    list_of_prime_factors =[]
    LowestMultiple = 1
    for i in range(2,21):
        list_of_prime_factors.append(GetPrimeFactors(i))
    for i in all_factors:
        maxtotal = 0
        for j in range(len(list_of_prime_factors)):
            total = 0
            for k in range(len(list_of_prime_factors[j])):
                if i == list_of_prime_factors[j][k]:
                    total += 1
            if total > maxtotal:
                maxtotal = total
        LowestMultiple *= (i**maxtotal)
    print(LowestMultiple)

Solution()