def f(n,c):
    n=n+c
    if(n==155):
        return n
    else:
        print(n)
        return f(n,c+1)
n=int(input())
c=n+1
print(f(n,c))
    
