def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(0, len(lst) - 1 - i):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j +1]
                lst[j + 1] = temp

    return lst

lst = [66, 2,3,66,7,22,456,435,98]
print(bubble_sort(lst))