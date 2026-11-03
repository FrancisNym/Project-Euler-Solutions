def is_prime(num):
    if num < 2:
        return False
    else:
        for i in range(2,int(num**0.5 +1)):
            if num % i ==0:
                return False
        return True

def solution():
    total = 2 + 3
    n = 0
    while 6*n + 1 < 2000000 and 6*n - 1 < 2000000:
        if is_prime(6*n+1):
            total += 6*n+1
        if is_prime(6*n-1):
            total += 6*n-1
        n += 1
    return total

print(solution())