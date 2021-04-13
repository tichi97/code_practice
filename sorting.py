def merge(arr,start,mid,end):
  left=arr[start:mid+1]
  right=arr[mid+1:end+1]

  l=0
  r=0
  f=start

  while l<len(left) and r<len(right):
   if left[l]<=right[r]:
     arr[f]=left[l]
     f+=1
     l+=1
   else:
     arr[f]=right[r]
     f+=1
     r+=1

  while l<len(left):
    arr[f]=left[l]
    f+=1
    l+=1
  while r<len(right):
    arr[f]=right[r]
    f+=1
    r+=1
 
 
def mergeSort(arr,start,end):
  if start<end:
   mid=(end+start)//2
  
   mergeSort(arr,start,mid)
   mergeSort(arr,mid+1,end)
   merge(arr,start,mid,end)
 
 
 
arr = [1,7,3,5,6,3,8,2,7,99,23,64,36,23]
# print(bubbleSort(test))
# print(insertion(test))
# print(quickSort(test))
mergeSort(arr,0,len(arr)-1)
print(arr)
