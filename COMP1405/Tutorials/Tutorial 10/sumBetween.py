def sumBetween(start, end):
    if start == end:
        return start
    return start + sumBetween(start-1, end)

print(sumBetween(10, 1))