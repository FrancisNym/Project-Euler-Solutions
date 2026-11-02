# What is the 10001st prime number

def Is_prime(num):
    if num <2:
        return False
    for i in range(2, int(num**0.5 + 1)):
        if num % i == 0:
            return False
    return True

# Every prime >3 is in the form 6n-1 or 6n+1 so only need to check these numbers

def Solution():
    primes = [2,3]
    n=0
    while len(primes) <= 10001:
        if Is_prime(6*n -1):
            primes.append(6*n -1)
        if Is_prime(6*n+1):
            primes.append(6*n+1)
        n += 1
    return primes[10000]

print(Solution())