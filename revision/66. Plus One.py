def plusOne(digits):
    string = ""
    res = []
    for n in digits:
        string += str(n)

    number = int(string)
    number += 1

    for n in str(number):
        res.append(int(n))

    return res