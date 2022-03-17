# https://leetcode.com/problems/design-hashset/submissions/
class MyHashSet:

    def __init__(self):
        self.arr = [ [] ,[],[] ,[],[] ,[],[] ,[],[] ,[] ]
        

    def add(self, key: int) -> None:
        h = key%10
        if key in self.arr[h]:
            return 
        self.arr[h].append(key)
        
        

    def remove(self, key: int) -> None:
        h = key%10
        if key in self.arr[h]:
            self.arr[h].remove(key)
        
        

    def contains(self, key: int) -> bool:
        h = key%10
        if key in self.arr[h]:
            return True
            
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)