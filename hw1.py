def fib (x):
 a,b=0,1
 for i in range(1,x+1):
  if (i == x):
   return b
  c=a+b
  a,b=b,c
print(fib(2))
print(fib(5))
print(fib(12))
