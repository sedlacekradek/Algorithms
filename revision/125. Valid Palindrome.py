def solution(s):

    lowercase = s.lower()
    my_string = ""

    import string
    letters = string.ascii_lowercase
    numbers = ("0123456789")


    for char in lowercase:
        if char in letters or char in numbers:
            my_string += char

    l = 0
    r = len(my_string) - 1
    while l < r:
        if my_string[l] != my_string[r]:
            return False
        l += 1
        r -= 1

    return True


print(solution("Aa12/"))
print(solution("A man, a plan, a canal: Panama"))
print(solution(" "))
print(solution("race a car"))