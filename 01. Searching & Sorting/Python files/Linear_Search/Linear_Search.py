class Linear_Search_Algo:

    def __init__(self, array, target):
        self.array = array
        self.target = target

    def LinearSearch_and_get_index(self):  # time_complexity = O(n), space_complexity = O(1)

        for i in range(len(self.array)):

            if self.target == self.array[i]:
                return i
        return -1

    def LinearSearch_and_get_True_or_False(self):  # time_complexity = O(n), space_complexity = O(1)

        for i in range(len(self.array)):
            if self.target == self.array[i]:
                return True
        return False

    def LinearSearch_and_get_Max_number(self):  # time_complexity = O(n), space_complexity = O(1)

        max_number = self.array[0]
        for i in self.array:
            if i > max_number:
                max_number = i
        return max_number

    def LinearSearch_and_get_Min_number(self):  # time_complexity = O(n), space_complexity = O(1)

        min_number = self.array[0]

        for i in self.array:

            if i < min_number:
                min_number = i

        return min_number

    def LinearSearch_in_2D_Array(self, array_2d):
        increment = 0
        for row in range(len(array_2d[increment])):
            for column in range(len(array_2d[increment])):
                if array_2d[row][column] == self.target:
                    return row, column
            increment += 1
        return -1, -1

