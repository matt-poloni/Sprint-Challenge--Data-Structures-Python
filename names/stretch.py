import time

start_time = time.time()

def merge_in_place(arr, start, mid, end):
    arrA, arrB = arr[start:mid], arr[mid:end]
    i_A, i_B = 0, 0
    while (i := start + i_A + i_B) < end:
        try:
            a = arrA[i_A]
        except:
            arr[i:end] = arrB[i_B:]
            break
        try:
            b = arrB[i_B]
        except:
            arr[i:end] = arrA[i_A:]
            break
        if a <= b:
            arr[i] = a
            i_A += 1
            i += 1
        if b <= a:
            arr[i] = b
            i_B += 1
    return arr

def merge_sort_in_place(arr, l=0, r=None):
    if r is None:
        r = len(arr) - 1
    if r - l > 0:
        m = ((l + r) // 2) + 1
        merge_sort_in_place(arr, l, m - 1)
        merge_sort_in_place(arr, m, r)
        merge_in_place(arr, l, m, r + 1)
    return arr

with open('names_1.txt', 'r') as f:
    names_1 = f.read().split("\n")  # List containing 10000 names
    merge_sort_in_place(names_1)

with open('names_2.txt', 'r') as f:
    names_2 = f.read().split("\n")  # List containing 10000 names
    merge_sort_in_place(names_2)

duplicates = []
for name_1 in names_1:
    if name_1 in names_2:
        duplicates.append(name_1)
    # ^ ran in 1.8 seconds

    # if name_1[0] < 'N':
    #     for name_2 in names_2:
    #         if name_1 < name_2:
    #             break
    #         elif name_1 == name_2:
    #             duplicates.append(name_1)
    # else:
    #     for name_2 in reversed(names_2):
    #         if name_1 > name_2:
    #             break
    #         elif name_1 == name_2:
    #             duplicates.append(name_1)
    # ^ ran in 5.1 seconds

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
