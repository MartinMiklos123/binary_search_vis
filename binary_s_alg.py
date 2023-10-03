lst_mid = []


def binary_s(num, arr):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left)//2
        lst_mid.append([left,mid,right])

        if arr[mid] == num:
            return mid

        if arr[mid] > num:
            right = mid - 1

        else:
            left = mid + 1


