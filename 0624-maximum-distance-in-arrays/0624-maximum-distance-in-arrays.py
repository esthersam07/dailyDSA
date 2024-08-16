class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # Initialize with the first array's min and max
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        result = 0
        
        # Iterate from the second array onwards
        for i in range(1, len(arrays)):
            # Calculate possible distances with the current array's elements
            result = max(result, abs(arrays[i][-1] - min_val), abs(max_val - arrays[i][0]))
            
            # Update min and max values
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][-1])
        
        return result
