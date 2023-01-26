class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        dist_left = [[] for _ in range(len(seats))]
        dist_right = [[] for _ in range(len(seats))]

        sit_index = -1
        for i in range(len(seats)):
            if seats[i] == 1:
                sit_index = i
                dist_left[i] = 0
            else:
                if sit_index == -1:
                    dist_left[i] = len(seats)
                else:
                    dist_left[i] = i - sit_index

        sit_index = -1
        for i in range(len(seats) - 1, -1, -1):
            if seats[i] == 1:
                sit_index = i
                dist_right[i] = 0
            else:
                if sit_index == -1:
                    dist_right[i] = len(seats)
                else:
                    dist_right[i] = sit_index - i

        max_dist = -1
        for l, r in zip(dist_left, dist_right):
            max_dist = max(max_dist, min(l, r))

        return max_dist
