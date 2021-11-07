import Linear_Search

arr = [1, 3, 5, 7, 9, 11, 65, 24, 86, 13, 56, 78]
target = 99
search = Linear_Search.Linear_Search_Algo(arr, target)
print(search.LinearSearch_and_get_index())
print(search.LinearSearch_and_get_True_or_False())
print(search.LinearSearch_and_get_Max_number())
print(search.LinearSearch_and_get_Min_number())
array_2d = [[1, 3, 4], [13, 67], [76, 1, 874, 0, 24, 74, 11]]
print(search.LinearSearch_in_2D_Array(array_2d))