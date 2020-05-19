# Searches can be linear or logarithmic

# Linear Search - O(n)
# Works better with non sorted lists
def Linear_Search(arr, value):
        for element in arr:
                if(element == value):
                        print("Value Found at position ", element)
        
        print("Not Found")


# Binary Search - O(log n)
# Works better with sorted lists
def Binary_Search(arr, value):
        start_index = 0
        end_index = len(arr - 1)

        while (start_index < end_index):
                middle_index = int((start_index + end_index) / 2)

                if (arr[middle_index] == value):
                        print("Value Found at position", middle_index)

                if(arr[middle_index] < value):
                        start_index = middle_index + 1
                else:
                        end_index =  middle_index - 1
        
        print("Not Found")
