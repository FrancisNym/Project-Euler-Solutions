'''
Question:
Find sum of all the multiples of 3 or 5 below 1000
'''
def solution():
    sum = 0
    for i in range(3, 1000, 3):
        sum += i
    for i in range(5, 1000, 5):
        if i % 3 !=0:
            sum += i
    return sum

print(solution())