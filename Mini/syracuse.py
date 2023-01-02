def syracuse(n: int) -> int:
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count
def syracuse2(n: int) -> int:
    for i in range(n):
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        if n == 1:
            return i + 1

