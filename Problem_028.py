def generate_grid():
    grid = []
    for i in range(1001):
        grid.append([0]*1001)
    x, y = 501,501
    right,left,up,down = 0
    order = [0,1,2,3] # right, left, up, down
    count = 1
    while x<=1001 and y<=1001:
        next_move = order[(count-1)%4]
        grid[x][y] = count 
        count += 1
        if next_move == 0:
