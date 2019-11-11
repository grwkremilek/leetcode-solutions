#https://leetcode.com/problems/robot-return-to-origin/

def judgeCircle(moves):
    d = {'U' : 0, 'D' : 0, 'L' : 0, 'R' : 0}
    for move in moves:
        d[move] += 1
    if d['U'] == d['D'] and d['L'] == d['R']:
        return True
    return False


def judgeCircle(moves):
    return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')
    

def judgeCircle(self, moves: str) -> bool:
    move1 = 0
    move2 = 0
    for m in moves:
        if m == 'U': 
            move1 += 1
        elif m == 'D':
            move1 -=1
        elif m == 'L':
            move2 += 1
        elif m == 'R':
            move2 -=1
    return move1 == 0 and move2 == 0


def judgeCircle(self, moves: str) -> bool:
    return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")
