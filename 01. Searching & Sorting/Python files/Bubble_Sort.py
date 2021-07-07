def Bubble_sort(arr):  # argument: (arr) --> arr = array/list

    length = len(arr)  # find the length of array

    for i in range(length - 1):  # iterative for round 1

        for j in range(length - 1 - i):  # iteration for comparing adjacent element

            if arr[j] > arr[j + 1]:  # if [j]--> first element is greater then [j+1] --> element before it then swap

                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# also in j loop i have deduct i also because after round 1 we will get largest element at last which we dont want to
# compare with element before it

arr = [2, 4, 1, 2, 8, 3]  # after round 1 -- arr = [2,1,2,4,3,8]
Bubble_sort(arr)  # after round 2 -- arr = [1,2,2,3,4,8]
print(arr)
