def selection_sort(arr):  # argument: (arr) --> arr = array/list

    length = len(arr)  # find the length of array/list

    for i in range(length - 1):  # will run loop till the end of list

        minindex = i  # our min-element index = i

        for j in range(i + 1, length):  # will start after the ith element

            if arr[j] < arr[minindex]:  # if j element is less then ith element then we found min-element then i

                minindex = j  # so our next min-element is j (then we just found)

        arr[i], arr[minindex] = arr[minindex], arr[i]  # after the whole iteration finish we will have two things
        #  |                        # 1. our ith element and 2. element lesser then ith element so we will
        #  |--------------- swap them so at first position we will get min-element from the whole list


arr = [2, 4, 1, 2, 8, 3]
selection_sort(arr)
print(arr)
