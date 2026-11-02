# Question:
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
# Difference is 2 times all addition permutations

def Solution(Num):
    Start = 1
    Total = 0
    for i in range(101):
        for j in range(Start+1,Num+1):
            Total += (Start * j)
        Start += 1
    return 2*Total

print(Solution(100))