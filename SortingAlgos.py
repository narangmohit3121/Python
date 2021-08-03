class SortingMethods(object):
    @staticmethod
    def bubble_sort(arr: list):
        for i in range(len(arr)-1, 0, -1):
            for j in range(i):
                if arr[j] > arr[j+1]:
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp

    @staticmethod
    def selection_sort(arr: list):
        for i in range(len(arr)-1, 0, -1):
            position_to_fill = i
            max_val_pos = 0
            for j in range(i):
                if arr[j] > arr[max_val_pos]:
                    max_val_pos = j
            temp = arr[position_to_fill]
            arr[position_to_fill] = arr[max_val_pos]
            arr[max_val_pos] = temp

    @staticmethod
    def insertion_sort(arr: list):
        for i in range(0, len(arr)):
            j = int(i)
            while j > 0:
                if arr[j-1] > arr[j]:
                    temp = arr[j]
                    arr[j] = arr[j-1]
                    arr[j-1] = temp
                    j -= 1
                else:
                    break

    @staticmethod
    #Static methods do not need a self parameter
    def shell_sort(arr: list) -> None:

        def gap_insertion_sort(input_arr, start, gap):
            for i in range(start, len(input_arr), gap):
                position = i
                current_val = input_arr[i]

                while (position >= gap) and (input_arr[position - gap] > current_val):
                    input_arr[position] = input_arr[position - gap]
                    position -= gap
                input_arr[position] = current_val

        number_of_sublist = len(arr)//2
        while number_of_sublist > 0:
            for start_point in range(number_of_sublist):
                gap_insertion_sort(arr, start_point, number_of_sublist)
            number_of_sublist = number_of_sublist//2

    def merge_sort(self, arr):
        if len(arr) > 1:
            split_point = len(arr)//2
            array_first_half = arr[:split_point]
            array_second_half = arr[split_point:]
            self.merge_sort(array_first_half)
            self.merge_sort(array_second_half)

            i, j, k = 0, 0, 0
            while i < len(array_first_half) and j < len(array_second_half):
                if array_first_half[i] < array_second_half[j]:
                    arr[k] = array_first_half[i]
                    i += 1
                    k += 1
                else:
                    arr[k] = array_second_half[j]
                    j += 1
                    k += 1

            while i < len(array_first_half):
                arr[k] = array_first_half[i]
                i += 1
                k += 1
            while j < len(array_second_half):
                arr[k] = array_second_half[j]
                j += 1
                k += 1

    @staticmethod
    def quick_sort(input_arr):
        def quick_sort_help(arr, start, end):
            if start < end:
                split_position = find_partition(arr, start, end)
                quick_sort_help(arr, start, split_position - 1)
                quick_sort_help(arr, split_position + 1, end)

        def find_partition(arr, start, end) -> int:
            split_point = start
            split_value = arr[start]
            left_mark = start + 1
            right_mark = end
            done = False
            while not done:
                i = 0
                while left_mark <= right_mark and arr[left_mark] <= split_value:
                    left_mark += 1
                while right_mark >= left_mark and arr[right_mark] >= split_value:
                    right_mark -= 1
                if right_mark < left_mark:
                    done = True
                else:
                    temp = arr[left_mark]
                    arr[left_mark] = arr[right_mark]
                    arr[right_mark] = temp
            temp = arr[split_point]
            arr[split_point] = arr[right_mark]
            arr[right_mark] = temp
            # split_point = right_mark
            return right_mark

        quick_sort_help(input_arr, 0, len(input_arr) - 1)


sorting_methods = SortingMethods()
a1 = [7, 4, 1, 5, 2, 6, 0, -1, 10, 3, 1, 4, 9]
# SortingMethods.shell_sort(a1)
sorting_methods.quick_sort(a1)

print(a1)
