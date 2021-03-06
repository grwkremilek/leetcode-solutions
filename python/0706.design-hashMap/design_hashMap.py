#https://leetcode.com/problems/design-hashmap/

class MyHashMap(object):

    def __init__(self):
        self.items = [0] * 1000000
        
    def put(self, key, value):
        self.items[key] = value+key+1
        
    def get(self, key):
        if self.items[key]:
            return self.items[key]-key-1
        else:
            return -1
        
    def remove(self, key):
        self.items[key] = 0


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
