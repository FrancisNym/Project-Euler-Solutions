'''
Question:
Find sum of all odd squares below 870 thousand
'''
def solution():
    sum:int = 0
    for i in range(1, 870000, 2):
        sum += i**2
    return sum

print(solution())