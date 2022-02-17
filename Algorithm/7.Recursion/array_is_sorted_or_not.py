def is_sorted(arr):
    if len(arr)==1:
        return True
    if arr[0]>arr[1]:
        return False

    is_sorted(arr[1:])


    
