# #perfect number
# num=9
# sum=0
# for i in range(1,num):
#  if num%i==0:
#   sum+=i
# if sum==num:
#    print('Perfect Number')
# else:
#     print('Not Perfect number')
 


# def check_perfectnumber(num1):
#  sum=0
# for i in range(1,num1):
#  if num1%i==0:
#   sum+=i
# if sum==num1:
#    return True
# else:
#     return False

# n=int(input("Enter number"))

# if n==[2,3,4,5,9]:
#   print('n')
# else:
#   print(' ')
# #check prime by using single digits

# for i in range(2,10):
#  if n%i==0:
#     print('Not prime')
#     break
#  else:
#     print('Prime')
# if we take 2459 as input it should print only prime numbers by using list not range

# list1=[2,3,5,6,7]
# if i>1:
#   for i in range(2,i):
#     if list%i==0:
#       break
#   else:
#     print(i)

# numbers = [2,3,5,6,7]

# for num in numbers:
#     if num > 1:   
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(num)
list2=[[1,2,3],[5,6,7]]
sum=0
for i in list2:
    for j in i:
        sum+=j
print(sum)

str1='Pavani'
rev_str=' '
for i in str1:
    rev_str=i+rev_str
print(rev_str)

list4=[1,2,3,4]
rev_list=[ ]
for l in list4:
    rev_list = [l] + rev_list
print(rev_list)