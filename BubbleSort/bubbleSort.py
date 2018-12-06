
def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if(nums[j] > nums[j+1]):
                 arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [7, 4, 3, 67, 34, 1, 8]
bubble_sort(arr)
print(arr) 