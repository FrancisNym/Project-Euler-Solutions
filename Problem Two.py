'''
Question:
Sum of the even fibonacci numbers under 4 Million, starting with 1,2...
'''

Fibonacci = [1,2]

def GenerateFib():
    NextTerm = 0
    i = 2
    while NextTerm < 4000000:
        NextTerm = Fibonacci[i-1] + Fibonacci[i-2]
        Fibonacci.append(NextTerm)
        i += 1

def Solution():
    global Fibonacci
    GenerateFib()
    sum = 0
    for i in range(1, len(Fibonacci)-1, 3):
        sum += Fibonacci[i]
    return sum

print(Solution())