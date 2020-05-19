# Sorts can use insertion or comparison

# Comparison Sorts

# Bubble Sort - O(n^2)
def Bubble_Sort(arr):
        for i in arr:
                for j in range(len(arr) - 1):
                        if (arr[j] > arr[j + 1]):
                                lesser = arr[j + 1]
                                arr[j + 1] = arr[j]
                                arr[j] = lesser

        print(arr)

# Selection Sort - O(n^2)
def Selection_Sort(arr):
        for i in range(len(arr)):
                min_index = i
                
                for j in range(i + 1, len(arr)):
                        if (arr[j] < arr[min_index]):
                                min_index = j

                if (i != min_index):
                        lesser = arr[min_index]
                        arr[min_index] = arr[i]
                        arr[i] = lesser

        print(arr)


# Insertion Sort

# Insertion Sort - O(n^2)
def Insertion_Sort(arr):
        for i in range(len(arr)):
                key = arr[i]
                j = i - 1

                while (j >= 0 and arr[j] > key):
                        arr[j + 1] = arr[j]
                        j -= 1

                arr[j + 1] = key

        print(arr)
