"""
Design a time-based key-value data structure that can store multiple values for the same key at different
time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:
TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously,
with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated
 with the largest timestamp_prev. If there are no values, it returns "".


Example 1:
Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"
"""


class TimeMap(object):

    def __init__(self):
        self.times_dict = {}
        self.min_val = float("inf")  # inf so that the first value is always lower

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.times_dict[key] = self.times_dict.get(key, []) + [(timestamp, value)]

        # update the lowest timestamp value - used for edge cases
        if timestamp < self.min_val:
            self.min_val = timestamp
        # helper for debug
        print(self.times_dict)


    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        # edge cases
        if key not in self.times_dict or timestamp < self.min_val:
            return ""

        # retrieve list from a hashmap
        key_list = self.times_dict[key]

        # binary search
        l = 0
        r = len(key_list) - 1

        while l <= r:
            mid = (l + r) // 2

            if key_list[mid][0] == timestamp:
                return key_list[mid][1]

            elif key_list[mid][0] > timestamp:
                r = mid - 1

            elif key_list[mid][0] < timestamp:
                l = mid + 1


        if l > 0:
            return key_list[l-1][1]
        else:
            return key_list[l][1]


timeMap = TimeMap()
timeMap.set("key", "item1", 1)
timeMap.set("key", "item2", 2)
timeMap.set("key", "item4", 4)
print(timeMap.get("key", 1))  # item1
print(timeMap.get("key", 3))  # item2
print(timeMap.get("key", 4))  # item4

timeMap.set("love","high",10)
timeMap.set("love","low",20)
print(timeMap.get("love", 5))  # item1