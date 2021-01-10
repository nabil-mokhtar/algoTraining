# Press the green button in the gutter to run the script.
def insertion(arr):
    sorted=1

    for i in range(len(arr)):
        #compare with sorted elements
        if i==0:continue
        tmp=i
        for x in range(sorted):
            if arr[tmp]<arr[i-x-1]:
                arr[tmp],arr[i-x-1]=arr[i-x-1],arr[tmp]
                tmp-=1
            else:

                break

        sorted+=1


    return arr

