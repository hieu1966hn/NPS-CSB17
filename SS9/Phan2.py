def sort_asc(arr):
    for i in range(len(arr) - 1):
        min_pos = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_pos]:
                min_pos = j
                arr[i] = arr[min_pos]
                arr[min_pos] = arr[i]
    return arr



# 5 1 8 92 -1 30