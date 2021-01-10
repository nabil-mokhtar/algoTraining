import math


def mergesort(arr,start,end):

    if end>start:
        mid = int((end + start )/ 2)
        mergesort(arr,start,mid)
        mergesort(arr,mid+1,end)
        merge(arr,start,end,mid)


##########################################################




def merge(arr,start,end,mid):

    l1=arr[start:mid+1]
    l2=arr[mid+1:end+1]

    ptr1=0
    ptr2=0
    for i in range(len(l1)+len(l2)):
        a=l1[ptr1] if ptr1<len(l1) else math.inf
        b=l2[ptr2] if ptr2<len(l2) else math.inf

        arr[start+i]=min(a,b)

        if a<b:
            ptr1+=1
        else:
            ptr2+=1
