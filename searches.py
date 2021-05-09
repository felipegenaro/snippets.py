# Searches can be linear or logarithmic

unsorted_array_1 = [10, 7, 8, 3, 4, 9, 5, 1, 2]
sorted_array_1 = [1, 2, 3, 4, 5, 7, 8, 9, 10]
sorted_array_2 = [1, 2, 3]

# Linear Search - O(n)
# Works better with non sorted lists
def Linear_Search(arr, value):
        for element in arr:
                if(element == value):
                        return "Value Found at position ", element
        
        return "Not Found"


# Binary Search - O(log n)
# Works better with sorted lists
def Binary_Search(arr, value):
        start_index = 0
        end_index = len(arr) - 1

        while (start_index <= end_index):
                middle_index = int((start_index + end_index) / 2)

                if (arr[middle_index] == value):
                        return "Value Found at position", middle_index

                if(arr[middle_index] < value):
                        start_index = middle_index + 1
                else:
                        end_index =  middle_index - 1
        
        return "Not Found"



print Linear_Search(unsorted_array_1, 4)
print Binary_Search(sorted_array_1, 4)
