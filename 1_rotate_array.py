def rotate_array_python(nums, k):
    n = len(nums)
    k = k % n
    nums = nums[n - k :] + nums[: n - k]
    return nums


def rotate_array(nums, k):
    n = len(nums)
    k = k % n
    for i in range(k):
        temp = nums[n - 1]
        for j in range(n - 1, 0, -1):
            nums[j] = nums[j - 1]
        nums[0] = temp
    return nums


def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_array_reverse(nums, k):
    n = len(nums)
    k = k % n
    k %= n

    if k > 0:
        nums.reverse()
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)


if __name__ == "__main__":

    num_elements = int(input("Enter the number of elements: "))
    arr = []
    for _ in range(num_elements):
        element = input("Enter an element: ")
        arr.append(element)  # or int(element) for integers

    k = int(input("Enter the number of rotations: "))
    rotated_arr = rotate_array_python(arr, k)
    print("Rotated array:", rotated_arr)
