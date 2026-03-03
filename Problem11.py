class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        maximum_area = float("-inf")
        i, j = 0, len(height)-1

        while i < j:
             
            product = (j-i) * min(height[i],height[j])
            maximum_area = max(maximum_area, product)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return maximum_area