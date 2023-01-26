def isHappy(n):
    repeated = set()
    while n != 1:
        res = 0
        for num in str(n):
            res += int(num) ** 2
        n = res
        if n in repeated:
            return False
        repeated.add(n)
    return True

print(isHappy(19))