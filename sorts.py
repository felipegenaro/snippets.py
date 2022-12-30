import time as t
import random as r

# Sorts can use insertion or comparison

# From this list, in classification of the better and most constant algorithm 
# 1 - Selection Sort
# 2 - Bubble Sort
# 3 - Merge Sort
# 4 - Insertion Sort

# Sample to be analysed
start_sample_time = t.time()
random_set = r.sample(range(20000), 10000)
end_sample_time = t.time() - start_sample_time

some_array_1 = random_set
some_array_2 = random_set
some_array_3 = random_set
some_array_4 = random_set

# ========================================================================

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


# There is also Quick Sort, an in-place sorting using a pivot to compare to - O(n^2)

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


# Printing according to the classification above
print ("Time to get the sample to be sorted", end_sample_time)
print ("-----------------------------------------------------")
print ("Selection_Sort_TimeSorting_", Selection_Sort(some_array_3)[1])
print ("Bubble_Sort_TimeSorting_", Bubble_Sort(some_array_2)[1])
print ("Merge_Sort_TimeSorting_", Merge_Sort(some_array_1)[1])
print ("Insertion_Sort_TimeSorting_", Insertion_Sort(some_array_4)[1])

# ========================================================================

# Understanding BIG O Notation

# Big O - Worst
# Big Ω - Best
# Big Θ - Average

# O(n Log n) = FOR inside a FOR
# int n = 100
# for(int i = 0; i < n; i++) // this loop is executed n times, so O(n)
# {
#     for(int j = n; j > 0; j/=2) // this loop is executed O(log n)
#     {
#
#     }
# }


# Both Merge and Heap Sort have the same worst case scenario - O(n Log n)
# Merge Sort is for a general purpose, more stable (divide and conquer)
# Heap Sort it is complex to implement


# In oder words

# O(1) = O(yeah)
# O(log n) = O(nice) 
# O(n) = O(ok)
# O(n^2) = O(my)
# O(2^n) = O(no)
# O(n!) = O(mg!)

