#https://leetcode.com/problems/duplicate-zeros/submissions/


def duplicateZeros(arr):
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            arr.insert(i, 0)
            arr.pop()
            i+=2
            continue
        i+=1


def duplicateZeros(arr):
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            arr.insert(i,0)
            arr.pop()
            i+=1
        i+=1
