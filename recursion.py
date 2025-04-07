# Finding factorial of a program using ITERATIVE and RECURSIVE approach
# using ITERATION
'''def fact(num):
    res=1
    if num > 0:
        for i in range(1, num+1):
            res *= i
        return res'''
# using RECURSION
def fact(num):
    if num < 1:
        return 1
    else:
        return num*fact(num-1)
print(fact(5))