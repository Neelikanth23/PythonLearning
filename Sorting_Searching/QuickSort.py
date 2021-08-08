def partion(a, start, end):
    pivot_idx = start
    pivot = a[start]
    while start < end:
        while start < len(a) and a[start] <= pivot:
            start += 1
        while a[end] > pivot:
            end -= 1

        if start < end:
            a[start], a[end] = a[end], a[start]

    a[pivot_idx], a[end] = a[end], a[pivot_idx]
    return end


def quicksort(a, start, end):
    if start < end:
        pi = partion(a, start, end)
        quicksort(a, pi+1, end)
        quicksort(a, start, pi-1)


print('Hello')
arr = [4, 2, 67, 32, 1, 0]
quicksort(arr, 0, len(arr)-1)
print(arr)
