def is_prime(num):
    if num < 2:
        return False
    else:
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                return False
    return True

def primes_up_to_1000():
    primes = []
    for i in range(1001):
        if is_prime(i):
            primes.append(i)
    return primes

def Solution():
    primes = primes_up_to_1000()
    max_consec = 0
    ab = 0
    for a in range(-999, 1000):
        for b in primes:
            next_num = b
            streak = 0
            n = 0
            while is_prime(next_num):
                next_num = n**2 + a*n + b
                streak += 1
                n+=1
            if streak > max_consec:
                max_consec = streak
                ab = a*b
    return max_consec, ab

print(Solution())