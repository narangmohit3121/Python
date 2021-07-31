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

                while (position > gap) and (input_arr[position - gap] > current_val):
                    input_arr[position] = input_arr[position - gap]
                    position -= gap
                input_arr[position] = current_val

        number_of_sublist = len(arr)//2
        while number_of_sublist > 0:
            for start_point in range(number_of_sublist):
                gap_insertion_sort(arr, start_point, number_of_sublist)
            number_of_sublist = number_of_sublist//2


a1 = [7, 4, 1, 5, 2, 6, 0, -1, 10, 3, 1]
SortingMethods.shell_sort(a1)

print(a1)
