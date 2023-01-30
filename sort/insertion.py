def insertionsort(array):
    for step in range(1,len(array)):
        key = array[step]  #compare key elemnt with others left until elemnt small
        j = step-1
        while j>=0 and key<array[j]:
           array[j+1]=array[j]
           j = j-1
        array[j+1]=key
a=[8,4,9,2,6,1]
print(a)
insertionsort(a)
print(a)


