add=lambda a,b : a+b
print(add(3,5))

say_hello=lambda: "Hello People"
print(say_hello())

square=lambda x : x*x
print(square(4))

fib= lambda n : n if n <=1 else fib(n-1)+fib(n-2)
for i in range(10):
    print(fib(i),end=" ")