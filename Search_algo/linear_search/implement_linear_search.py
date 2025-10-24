def search(arr,x):
    for i in range(0,len(arr)):
        if arr[i] == x:
            return i 
    else:
        return -1
    
if __name__ == "__main__":
    arr = [2,3,4,10,40]
    x = 10

    result = search(arr,x)

    if result == -1:
        print("The element isnt present in array")
    else:
        print(f"The element is present ar index {result}")