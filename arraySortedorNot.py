class Solution:
    def arraySortedOrNot(self, arr) -> bool:
        left = 0
        right = 1
        while right < len(arr):
            if arr[left] > arr[right]:
                return False
            else:
                left += 1
                right += 1
        return True
