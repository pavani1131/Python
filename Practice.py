# a=int(input("Enter number"))
# print(int(str(a)[ ::-1]))
# b="999"
# print(int(str(b)[ ::-1]))
# str1="pavani"
# print(str1[ ::-1])

# num=int(input("Enter number"))
# fact=1
# if num>1:
#     for i in range(1,num+1):
#         fact *=i
#         print(fact)
# elif num==0:
#     print("factorial of 0 is 1")
# else:
#     print("factorial is not possible for negative numbers")
# str2="Wonder"
# print(str2[2:4])
    
# num2="1224"
# print(int(str(num2)[1:3]))
# str3="World"
# print(str3[2])
# str4="6969"
# # print(int(str(str4)[1:3]))

for i in range(1,101,1):
    print(i)

# a=int(input("enter number"))
# while a>=50:
#     for a in range (2,50,2):
#      print(a)
def simple_calc(num1,num2,op):
   if op=='+'or op=='add':
      print(num1+num2)
   elif op=='-' or op=='sub':
      print(num1-num2)
   elif op=='*' or op=='mul':
      print(num1*num2)
   elif op=='/' or op=='div':
      print(num1/num2) if num2!=0 else print('Division not possible')
   else:
      print('Invalid operator')

num1=float(input("Enter num1"))
num2=float(input("enter num2"))
op=input("enter op")

simple_calc(num1,num2,op)

def check_leap(year):
   # if year<0:
      return 'Leap year' if( year %400 ==0) or (year%100 !=0 and year % 4==0) else 'Not a Leap Year'
   # if year%400==0:
   #    return 'Leap Year'
   # elif (year%100 !=0 and year %4==0):
   #    return 'Leap Year'
   # else:
   #    return 'Non Leap Year'
year=int(input("Enter Year"))
print(check_leap(year))
# student=int(input("enter marks"))
# if student>=40:
#     print("Pass")
# else:
#     print("fail")
def check_student(marks):
    if(marks > 90):
        return 'Grade A'
    elif 80<=marks<=89:
        return 'Grade B'
    elif 70<=marks<=79:
        return 'Grade C'
    else:
        return 'fail'
marks=int(input("Enter marks"))
print(check_student(marks))

s1,s2,s3=3,4,5

if(s1+s2>s3) and (s1+s3>s2) and (s2+s3>s1):
    print('Valid triangle')
    if s1==s2==s3:
        print('Equilateral triangle')
    elif s1==s2 or s2==s3 or s1==s3:
        print('Isoceles Triangle')
    elif s1!=s2 and s2!=s3 and s1!=s3:
        print('Scalene Triangle')
    else:
        print('Invalid Triangle')
start=2
while start<=50:
    
    print(start)
    start+=2
n=100
for i in range(1,n+1):
    if i%2==0:
        print(i)
    
    


    
      
