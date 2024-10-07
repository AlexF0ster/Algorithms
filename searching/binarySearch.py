def binarySearch(data:list[int],term:int)->int:
    """Returns -1 if data not found
    Returns index of data if found
    data must be sorted"""

    start=0
    end=len(data)-1
    while start<=end:
        middle=(start+end)//2
        if term==data[middle]:
            return middle
        elif term<data[middle]:
            end=middle-1
        else:
            start=middle+1
    return -1
        
    