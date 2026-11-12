def Solution():
    next_term = 0
    current_term = 1
    previous_term = 1
    index = 2
    while len(str(next_term)) < 1000:
        next_term = current_term + previous_term
        previous_term = current_term
        current_term = next_term
        index += 1
    return index

print(Solution())