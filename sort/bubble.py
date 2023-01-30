def bubblesort(e):
  for i in range(len(e)):
    for j in range(0, len(e) - i - 1):

      if e[j] > e[j + 1]:
        temp = e[j]
        e[j] = e[j+1]
        e[j+1] = temp

e=[8,4,9,3,0,2,2] 
print(e)
bubblesort(e)
print(e) 


    