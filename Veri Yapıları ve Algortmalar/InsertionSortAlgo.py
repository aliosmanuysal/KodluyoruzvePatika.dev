def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        current_element = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current_element:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current_element

liste = [22, 27, 16, 2, 18, 6]

print("Sırasız dizi: ", liste)
insertion_sort(liste)
print("Sıralı dizi: ", liste)

