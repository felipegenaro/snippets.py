import time as t

# Searches can be linear or logarithmic

unsorted_array = [10, 7, 8, 3, 4, 9, 5, 1, 2]
sorted_array = [1, 2, 3, 4, 5, 7, 8, 9, 10]

# From this list, in classification of the better and most constant algorithm 
# 1 - Binary_Search on Sorted List
# 2 - Linear_Search on Unsorted List
# 3 - Linear_Search on Sorted List
# 4 - Binary_Search on Unsorted List

# Linear Search - O(n)
# Works better with non sorted lists
def Linear_Search(arr, value):
        start_time = t.time()

        for element in arr:
                if(element == value):
                        end_time = t.time() - start_time
                        return "Value Found at position ", element, end_time
        
        return "Not Found"


# Binary Search - O(log n)
# Works better with sorted lists
def Binary_Search(arr, value):
        start_time = t.time()

        start_index = 0
        end_index = len(arr) - 1

        while (start_index <= end_index):
                middle_index = int((start_index + end_index) / 2)

                if (arr[middle_index] == value):
                        end_time = t.time() - start_time
                        return "Value Found at position", middle_index, end_time

                if(arr[middle_index] < value):
                        start_index = middle_index + 1
                else:
                        end_index =  middle_index - 1
        
        return "Not Found"



print "Linear_Search on Unsorted List", Linear_Search(unsorted_array, 4)
print "Linear_Search on Sorted List", Linear_Search(sorted_array, 4)
print "Binary_Search on Unsorted List", Binary_Search(unsorted_array, 4)
print "Binary_Search on Sorted List", Binary_Search(sorted_array, 4)
