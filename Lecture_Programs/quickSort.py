l1=[7,6,5,4,3,2,1]

def quickSort(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot=arr[0]
        left = [i for i in arr[1:] if i<pivot]
     # print(left)
        right = [i for i in arr[1:] if i>=pivot]
      #  print(right)
        return quickSort(left)+[pivot]+quickSort(right)



print(l1)
l2=quickSort(l1)
print(l2)