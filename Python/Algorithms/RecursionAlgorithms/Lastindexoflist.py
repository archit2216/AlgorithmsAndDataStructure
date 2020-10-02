def lastIndex(arr,x,li):
    if li==0 and arr[li]!=x:
        return -1
    
    if arr[li]==x:
        return li
    
    z=lastIndex(arr,x,li-1)
    return z
    
    pass


n=int(input())
arr=[int(x) for x in input().split()]
x=int(input())
li=n-1
print(lastIndex(arr,x,li))