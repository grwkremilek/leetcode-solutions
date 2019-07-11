#https://leetcode.com/problems/fizz-buzz/


def fizzBuzz(n):
    ans = []
    for i in range(1,n+1):
        if i % 3 == 0 and not i % 5 == 0:
            ans.append("Fizz")
        elif i % 5 == 0 and not i % 3 == 0:
            ans.append("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            ans.append("FizzBuzz")
        else:
            ans.append(str(i))
    return ans


def fizzBuzz(n):
    ans = []
    for num in range(1,n+1):
        divisible_by_3 = (num % 3 == 0)
        divisible_by_5 = (num % 5 == 0)
        num_ans_str = ""
        if divisible_by_3:
            num_ans_str += "Fizz"
        if divisible_by_5:
            num_ans_str += "Buzz"
        if not num_ans_str:
            num_ans_str = str(num)
        ans.append(num_ans_str)


def fizzBuzz(n):
    ans = []
    d = { 3 : "Fizz", 5 : "Buzz" }
    for num in range(1,n+1):
        current = ""
        for key in d.keys():
            if num % key == 0:
                current += d[key]
        if not current:
            current = str(num)
        ans.append(current)  
    return ans
        

def fizzBuzz(n):
    return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]
