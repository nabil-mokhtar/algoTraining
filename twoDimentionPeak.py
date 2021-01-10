from oneDimentionPeak import findPeak
def tdpeak(arr):
    col=len(arr[0])
    midcol=col//2
    maxv, row = findmax(arr[:,midcol])
    if col>1:
        if arr[row][midcol+1]>arr[row][midcol]:
            return tdpeak(arr[:,midcol+1:col])
        elif arr[row][midcol-1]>arr[row][midcol]:
            return tdpeak(arr[:,0:midcol])
        else:
            return arr[row][midcol]
    else:
        return arr[row][midcol]


git
def findmax(arr):
    maxv=0
    row=-1
    for i in arr:
        row+=1
        if i>maxv :
            maxv=i
            rows=row

    return maxv, rows
