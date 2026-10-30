'''
Question:
Largest Prime Factor of 600851475143
'''

Number = 600851475143
RootNumber = int((600851475143)**0.5)

def IsPrime(Num):
    CheckUpTo = int(Num**0.5)
    for i in range(2,CheckUpTo):
        if Num % i == 0:
            return False
    return True

def GenFactors(Number):
    Factors = []
    for i in range(1,int((Number)**0.5)+1):
        if Number % i == 0:
            Factors.append(i)
            Factors.append(Number//i)
    Factors.sort()
    return Factors

def Solution(Number):
    Factors = GenFactors(Number)
    for i in range(len(Factors)-1,-1,-1):
        if IsPrime(Factors[i]):
            return Factors[i]

print(Solution(Number))