# Control Flow statements

# n= 11

# if n % 2 == 0 :
#     print(n , " is an even number")
# else:
#     print(n, " is an odd number")

# i =10
# if i < 15: print('True') 
# else: print("False")

# a=12
# b=10
# c=15
# if a>b:
#     if a>c:
#         print(a,' is big')
#     else:
#         print(c,' in bigger')
# elif b > c :
#     print(b," is big")
# else:
#     print(c,' is big')


# list =[1,2,3,4,5]

# for i in list:
# # for i in 1,2,3,4,5
#     print(list[i], end=' ')

# m=5
# i=0
# print('While Started')
# while ( i < m ):
#     print(i, end=" ")
#     i+=1
# print('\n While Terminated')



# for i in range (10):
#     print(i)
#     break
# print('Out of loop')





# for var in "Python World":
#     if( var == 'o'):
#         print('Continue executed')
#         continue
#     else:
#         print('Continue not executed')
#     print(var, end=" ")

# String1="Hello Python"

# print(len(String1))

# pi = 3.142
# text = ' The value of pi is'+ str(pi)

# print(text)


# name=['alpha','beta','gama','delta']
# roll_no = [1,6,2,3]
# mapped = zip(name, roll_no)
# print(dict(mapped))

# l1 = ['alpha','beta','gama','delta']
# s1 ='Python'
# ob1 = enumerate(l1)
# ob2 = enumerate(s1)

# print(type(ob1))
# print(dict(ob1))


# print(list(enumerate(l1,2)))



def add(num1: int, num2: int) -> int:
    """Add two numbers"""
    num3 = num1 + num2
 
    return num3
 
# Driver code
num1, num2 = 5, 15
ans = add(num1, num2)
print("The addition of ",num1," and ",num2," results ",ans")