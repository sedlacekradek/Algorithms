def uniqueOccurrences(arr):
    count_dic = {}
    for number in arr:
        count_dic[number] = count_dic.get(number, 0) + 1

    x = count_dic.values()
    y = set(count_dic.values())
    return len(x) == len(y)


    # check_duplicates = set()
    # for key, val in count_dic.items():
    #     if val not in check_duplicates:
    #         check_duplicates.add(val)
    #     else:
    #         return False
    # return True

print(uniqueOccurrences([1,2,2,1,1,3]))
print(uniqueOccurrences([1,2]))