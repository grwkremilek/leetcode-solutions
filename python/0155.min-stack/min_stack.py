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



class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []
        self._min = float('inf')

    def push(self, x: int) -> None:
        if x < self._min:
            self._min = x
        self._stack.append(x)

    def pop(self) -> None:
        if self._min == self._stack.pop():
            self._min = float('inf')
            for val in self._stack:
                if val < self._min:
                    self._min = val

    def top(self) -> int:
        return self._stack[-1]
        
    def getMin(self) -> int:
        return self._min
