from typing import List

def list_avg(var_a:List)->float:
    return sum(var_a)/len(var_a)

# list_avg((123))


def divide(a,b):
    return a/b

def calculate(*values, operator):
    return operator(*values)


result=calculate(20,4,operator=divide)
print(result)


add=lambda x,y: x+y

print(add(2,4))

l=[1,5,7,9,2,4,5]
print([x*2 for x in l])

