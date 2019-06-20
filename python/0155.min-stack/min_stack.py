#https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []        

    def push(self, x):
        self.stack.append(x)      

    def pop(self):
        self.stack = self.stack[:-1]    

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return min(self.stack)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()






class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.st = [] 
        
    def push(self, x):
        cur_min = min(x, self.st[-1][1] if self.st else x)
        self.st.append((x, cur_min))                
    
    def pop(self):
        self.st.pop()        
    
    def top(self):
        return self.st[-1][0]        
    
    def getMin(self):
        return self.st[-1][1]
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
