with open("Problem_013Data.txt") as file:
    truncated_lines = []
    for line in file:
        truncated_lines.append(int((line.strip())[:13]))

def solution(lst):
    total = 0
    for i in lst:
        total += i
    total = str(total)
    return total[:10]

print(solution(truncated_lines))