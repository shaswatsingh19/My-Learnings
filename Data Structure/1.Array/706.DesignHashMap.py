# https://leetcode.com/problems/design-hashmap/
class MyHashMap:

    def __init__(self):
        self.arr = [None] * 1000001

    def put(self, key: int, value: int) -> None:
        self.arr[key] = value

    def get(self, key: int) -> int:
        if self.arr[key] == None:
            return -1
        else:
            return self.arr[key]

    def remove(self, key: int) -> None:
        self.arr[key] = None