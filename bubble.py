def bubblesort(e):
    for n in range(len(e)-1,0,-1):
        for i in range(n):
            if e[i] > e[i+1]:
                e[i], e[i+1] = e[i+1], e[i]
e=[8,4,9,3,0,2,2] 
print(e)
bubblesort(e)
print(e) 

    