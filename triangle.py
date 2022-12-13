def triangle(n):
    #no.of spaces
    k=n-1
    for i in range(0,n):  #rows
        for j in range(0,k):  #spaces
            print(end=" ")
        k=k-1   #decreasing each loop after k
        for j in range(0,i+1): #columns
            print("*",end=" ")
        print("\r")
n=5
triangle(n)