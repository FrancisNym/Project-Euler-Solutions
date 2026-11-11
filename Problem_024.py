num = [0,1,2,3,4,5,6,7,8,9]
def GenPerms(lst):
    all_lsts = []
    if len(lst) == 1:
        return [lst]
    
    for i in range(len(lst)):
        start_val = lst[i]
        rest = lst[:i] + lst[i+1:]
        perms_rest = GenPerms(rest)
        for j in perms_rest:
            all_lsts.append([start_val]+j)
    return all_lsts

def Solution():
    perms = GenPerms(num)
    for i in range(len(perms)):
        perms[i] = int("".join(map(str, perms[i])))
    perms.sort()
    return perms[999999]

print(Solution())