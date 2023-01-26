def plusOne(digits):
    # point is to convert list of digits to int number:
    # 1. convert to list of strings
    # 2. join the list into one string
    # 3. convert string to int and add +1
    # 4. convert back to string so that we can iterate through it
    # 5. create a list of digits by iterating and converting to int
    a = [str(i) for i in digits]  # 1
    a = ''.join(a)
    a = str(int(a)+1)
    return [int(i) for i in a]

print(plusOne([9]))
print(plusOne([4,3,2,1]))