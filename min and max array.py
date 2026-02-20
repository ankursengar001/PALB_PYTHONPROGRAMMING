class Solution:
    def getMinMax(self, arr):
        # Edge case: if array is empty
        if not arr:
            return []
        
        minimum = arr[0]
        maximum = arr[0]
        
        # Traverse array
        for num in arr[1:]:
            if num < minimum:
                minimum = num
            if num > maximum:
                maximum = num
        
        return [minimum, maximum]
