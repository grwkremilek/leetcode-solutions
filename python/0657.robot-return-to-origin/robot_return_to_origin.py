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
