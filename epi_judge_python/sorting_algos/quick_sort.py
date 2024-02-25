def partition(arr, l, h):
    pivot = arr[h]

    i = l
    for j in range(l, h):
        if arr[j] <= pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1

    arr[i], arr[h] = arr[h], arr[i]
    return i


def quick_sort(arr, l, h):
    if l >= h:
        return
    
    new_pivot_idx = partition(arr, l, h)
    quick_sort(arr, l, new_pivot_idx-1)
    quick_sort(arr, new_pivot_idx+1, h)


if __name__ == "__main__":
    arr = [-4, 400, 20, 4,3,2,9,0, -1, 45]
    quick_sort(arr, 0, len(arr)-1)
    print(arr)