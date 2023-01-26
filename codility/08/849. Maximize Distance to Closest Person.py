def maxDistToClosest(seats):
    import math

    res = 0
    dist = seats.index(1)  # for edge case if seats start with 0s [0,0,0,0,1]

    for seat in seats:
        if seat == 1:
            # if empty seat between 1s, count total distance between 1s and // 2, round down
            res = max(res, math.ceil(dist / 2))
            dist = 0
        # if empty seat, increase distance
        else:
            dist += 1

    # max takes care of edge case such as [1, 0, 0, 0, 0, 0]
    return max(res, dist)

print(maxDistToClosest([1,0,0,0,1,0,1]))
print(maxDistToClosest([0,1]))
print(maxDistToClosest([1,0]))
print(maxDistToClosest([1,1,1,0,1,1,1]))
print(maxDistToClosest([1,0,0,0]))