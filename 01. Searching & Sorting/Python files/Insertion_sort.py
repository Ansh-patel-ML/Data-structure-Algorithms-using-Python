def insertionSort(arr):  # argument: (arr) --> arr = array / list

    length = len(arr)  # find the length of array
    for i in range(1, length):  # starting from 1st index till end
        temp = arr[i]  # store the value of ith index in temp so it can be access later
        j = i - 1  # as we are starting from 1st index this j will have index of value before ith index
        while (j >= 0 and arr[
            j] > temp):  # this will loop will run till j has index 0 and j element must be larger then temp
            arr[j + 1] = arr[j]  # move j element right side
            j = j - 1  # take next j element from left side
        arr[j + 1] = temp  # add temp element to j + 1 index


arr = [2, 4, 1, 2, 8, 3]
insertionSort(arr)
print(arr)