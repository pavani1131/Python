str1="Pavani"
for i in str1:
    print(i)
l1=[124,"abc"]
for j in l1:
    print(j)
for i in range(0,11):
    print("Hi")
dict1={1:"abc",2:"bcd"}
for k in dict1:
    print(k)
set1={1,2,4,4}
for g in set1:
    print(g)
#Assignment
l1=[1,2,3]
for t in l1:
    if t %2 == 0:
        print(t,"Even")
even_count=0
odd_count =0
for o in range(1,11):
    if o % 2 ==0:
        print("Even")
        even_count=even_count+1
    else:
        print("odd")
        odd_count=odd_count+1
print("even_count",even_count)
print("odd_count",odd_count)
        
num1=12322
num1_str=str(num1)
sum_of_digits=0
for i in num1_str:
    sum_of_digits+= int(i)
    print(sum_of_digits)
num2=123
num2_str=str(num2)
product=1
for j in num2_str:
    product *=int(j)
    print(product)
num3=9

   






