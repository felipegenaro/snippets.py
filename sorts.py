import time as t

# Sorts can use insertion or comparison

some_array_1 = [10, 7, 8, 3, 4, 9, 5, 1, 2]
some_array_2 = [10, 7, 8, 3, 4, 9, 5, 1, 2]
some_array_3 = [10, 7, 8, 3, 4, 9, 5, 1, 2]
some_array_4 = [10, 7, 8, 3, 4, 9, 5, 1, 2]

# From this list, in classification of the better and most constant algorithm 
# 1 - Selection Sort
# 2 - Bubble Sort
# 3 - Merge Sort
# 4 - Insertion Sort

# Comparison Sorts

# Merge Sort - O(n log n)
def Merge_Sort(arr):
        start_time = t.time()

        if len(arr) <= 1:
                return

        # Divide and Conquer 
        mid_element = len(arr) // 2
        left_half = arr[:mid_element]
        right_half = arr[mid_element:]

        # Recursively Sorting the Halves
        Merge_Sort(left_half)
        Merge_Sort(right_half)

        # Initialize Counters
        i = j = k = 0

        # Comparison
        while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                        arr[k] = left_half[i]
                        i += 1
                else:
                        arr[k] = right_half[j]
                        j += 1
                k += 1
        
        # Check if any element was left behind
        while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1
        
        while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

        end_time = t.time() - start_time
        return arr, end_time


# Bubble Sort - O(n^2)
def Bubble_Sort(arr):
        start_time = t.time()

        if len(arr) <= 1:
                return

        for i in arr:
                for j in range(len(arr) - 1):
                        if (arr[j] > arr[j + 1]):
                                arr[j], arr[j+1] = arr[j+1], arr[j]

        end_time = t.time() - start_time
        return arr, end_time

# Selection Sort - O(n^2)
def Selection_Sort(arr):
        start_time = t.time()

        if len(arr) <= 1:
                return

        for i in range(len(arr)):
                min_index = i
                
                for j in range(i + 1, len(arr)):
                        if (arr[j] < arr[min_index]):
                                min_index = j

                if (i != min_index):
                        lesser = arr[min_index]
                        arr[min_index] = arr[i]
                        arr[i] = lesser

        end_time = t.time() - start_time
        return arr, end_time


# ========================================================================

# Insertion Sorts

# Insertion Sort - O(n^2)
def Insertion_Sort(arr):
        start_time = t.time()

        if len(arr) <= 1:
                return

        for i in range(len(arr)):
                key = arr[i]
                j = i - 1

                while (j >= 0 and arr[j] > key):
                        arr[j + 1] = arr[j]
                        j -= 1

                arr[j + 1] = key

        end_time = t.time() - start_time
        return arr, end_time



print "Merge_Sort", Merge_Sort(some_array_1)
print "Bubble_Sort", Bubble_Sort(some_array_2)
print "Selection_Sort", Selection_Sort(some_array_3)
print "Insertion_Sort", Insertion_Sort(some_array_4)
