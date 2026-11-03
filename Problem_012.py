# Find the first triangle number with over 500 factors

def find_num_factors(num):
    num_factors = 0
    for i in range(1,int(num**0.5 +1)):
        if num % i == 0:
            num_factors += 2
    return num_factors

def solution():
    current_triangle = 0
    current_num = 1
    while True:
        current_triangle += current_num
        if find_num_factors(current_triangle) > 500:
            return current_triangle
        current_num += 1

print(solution())


# This solution is very brute force, there is definitely a more efficient way to solve with some maths