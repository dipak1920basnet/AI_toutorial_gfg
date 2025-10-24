def main():
    arr = [2,3,4,10,40]
    x = 10
    result = binary_search(arr, x)
    recusrive_result = recurvieBinarySearch(arr,x,0,len(arr)-1)


    if result == -1:
        print("The element is not present in array")
    else:
        print(f"The element is prenset in index {result}")


    print(recusrive_result)

def binary_search(arr,x):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = start + (end - start)//2
        check = arr[mid]
        if  check == x:
            return mid
        elif x < check:
            end = mid
        else:
            start = mid
    return -1

def recurvieBinarySearch(arr,x, low, high):
    if low <= high:
        mid = low + (high - low)//2
        check = arr[mid]
        if check == x:
            return mid
        elif x < check: 
            return recurvieBinarySearch(arr,x,low,mid-1)
        else:
            return recurvieBinarySearch(arr,x,mid+1,high)
    return -1

if __name__ == "__main__":
    main()