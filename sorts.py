# Sorts can use insertion or comparison

some_array_1 = [10, 7, 8, 3, 4, 9, 5, 1, 2]
some_array_2 = [10, 7, 8, 3, 4, 9, 5, 1, 2]
some_array_3 = [10, 7, 8, 3, 4, 9, 5, 1, 2]
some_array_4 = [10, 7, 8, 3, 4, 9, 5, 1, 2]

# Comparison Sorts

# Merge Sort - O(n log n)
def Merge_Sort(arr):
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

        return arr


# Bubble Sort - O(n^2)
def Bubble_Sort(arr):
        if len(arr) <= 1:
                return

        for i in arr:
                for j in range(len(arr) - 1):
                        if (arr[j] > arr[j + 1]):
                                lesser = arr[j + 1]
                                arr[j + 1] = arr[j]
                                arr[j] = lesser

        return arr

# Selection Sort - O(n^2)
def Selection_Sort(arr):
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

        return arr



# Insertion Sorts

# Insertion Sort - O(n^2)
def Insertion_Sort(arr):
        if len(arr) <= 1:
                return

        for i in range(len(arr)):
                key = arr[i]
                j = i - 1

                while (j >= 0 and arr[j] > key):
                        arr[j + 1] = arr[j]
                        j -= 1

                arr[j + 1] = key

        return arr



print Merge_Sort(some_array_1)
print Bubble_Sort(some_array_2)
print Selection_Sort(some_array_3)
print Insertion_Sort(some_array_4)
