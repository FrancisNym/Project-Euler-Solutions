'''
Find the maximum total from the top of the triangle to the bottom
'''

triangle = []
with open("Problem_018Data.txt") as file:
    for line in file:
        triangle.append(line.strip().split())


def Solution():
    # Start from bottom and work way up
    last_line = len(triangle)-1
    for i in range(last_line,0,-1):
        for j in range(len(triangle[i])-1):
            if int(triangle[i][j])>int(triangle[i][j+1]):
                triangle[i-1][j] = int(triangle[i-1][j])+int(triangle[i][j])
            else:
                triangle[i-1][j] = int(triangle[i-1][j])+int(triangle[i][j+1])
    return triangle[0][0]

print(Solution())