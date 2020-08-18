# TO-DO: Complete the selection_sort() function below

def selection_sort(arr):
    # loop through each element in the array
    for i in range(len(arr)):
        # set the current minimum value's index
        current_min = i

        # start new loop from the next index
        for j in range(i+1, len(arr)):
            # compare the CM's value against the current iteration's value
            # if CM's value is greater than the current iteration's value,
            # set CM to the current iteration's index
            if arr[current_min] > arr[j]:
                current_min = j

            # if no other index's value is greater than the newly set CM, the loop will exit and swap values
        if current_min != i:
            arr[i], arr[current_min] = arr[current_min], arr[i]

    return arr

# done in class
def selection_sort1(arr):
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        # loop over the rest of the elements
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr


arr1 = [4,1,2,5,3]
selection_sort(arr1)
print(f'Selection Sort: {arr1}')

arr2 = [4,2,3,5,1]
selection_sort1(arr2)
print(f'Selection Sort1: {arr2}')

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    for i in range(0, len(arr) - 1):

        for j in range(0, len(arr) - i - 1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1], = arr[j+1], arr[j]

    return arr

# done in class
def bubble_sort1(arr):
    swapped = True

    while swapped:
        swapped = False
        for idx in range(len(arr) - 1):
            num1 = arr[idx]
            num2 = arr[idx + 1]

            if num1 > num2:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                swapped = True
    return arr

arr3 = [10,1,2,5,3,20,24,16,11,12,6,7,9]
arr4 = [10,1,2,5,3,20,24,16,11,12,6,7,9]
bubble_sort(arr3)
bubble_sort1(arr4)
print(f'Bubble Sort: {arr3}')
print(f'Bubble Sort: {arr4}')

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
