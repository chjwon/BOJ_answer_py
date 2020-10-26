def fib(n):
    if(n<3):
        return 1
    else:
        return (fib(n-1)+fib(n-2))%1000000

num=int(input())
print(fib(num))