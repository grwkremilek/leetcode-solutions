#https://leetcode.com/problems/asteroid-collision/

def asteroidCollision(asteroids):
    stack = []
    for aster in asteroids:
        if aster > 0:
            stack.append(aster)
        else:
            while stack and stack[-1] > 0 and stack[-1] < abs(aster):
            #while stack and 0 < stack[-1] < abs(aster):                #slower
                stack.pop()
            if not stack or stack[-1] < 0:
                stack.append(aster)
            elif stack[-1] == -aster:
                stack.pop()
    return stack
