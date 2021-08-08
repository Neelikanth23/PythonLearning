def insertion_sort(arr):
    for i in range(1, len(arr)):
        anchor = arr[i]
        j = i - 1
        while j >= 0 and anchor < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = anchor


a = [4, 2, 67, 32, 1, 0]
insertion_sort(a)
print(a)
