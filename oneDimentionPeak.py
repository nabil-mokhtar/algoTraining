def findPeak(arr):


    mid = (len(arr)-1) // 2
    if len(arr)>1:
        if arr[mid]<arr[mid+1]:
            print("go write -->")
            return findPeak(arr[mid+1:len(arr)])
        elif arr[mid]<arr[mid-1]:
            print("<-- go left")
            return findPeak(arr[0:mid])
        else:
            return arr[mid]
    else:
        return arr[mid]
