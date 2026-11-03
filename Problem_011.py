with open("Problem_011Data.txt") as file:
    lines = []
    for line in file:
        lines.append(line.strip())

for i in range(len(lines)):
    lines[i] = lines[i].split()
for i in range(len(lines)):
    for j in range(len(lines[i])):
        lines[i][j] = int(lines[i][j])

def solution(lst):
    max = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])-3):
            current = lines[i][j]*lines[i][j+1]*lines[i][j+2]*lines[i][j+3]
            if current > max:
                max = current
    for i in range(len(lines)-3):
        for j in range(len(lines[i])):
            current = lines[i][j]*lines[i-1][j]*lines[i-2][j]*lines[i-3][j]
            if current > max:
                max = current
    for i in range(len(lines)-3):
        for j in range(len(lines)-3):
            current = lines[i][j]*lines[i-1][j+1]*lines[i-2][j+2]*lines[i-3][j+3]
            if current > max:
                max = current
    for i in range(len(lines)-3):
        for j in range(len(lines)-3):
            current = lines[i][j+3]*lines[i-1][j+2]*lines[i-2][j+1]*lines[i-3][j+0]
            if current > max:
                max = current
    return max

print(solution(lines))