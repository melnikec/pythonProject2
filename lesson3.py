# import math
# a=3984573984573498
# print(math.sqrt(a))

# print(2 != 3)

# x=5
# print(0<=x<=10)

# print (1 and 110)

# a=2
# b=2
# print (a is b)

# Home Work

n1 = 867

n2 = 0

while n1 > 0:
    digit = n1 % 10
    n1 = n1 // 10

    n2 = n2 * 10
    n2 = n2 + digit

print(n2)