class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i,j= 0,0
        Counter = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums) and nums[i] == nums[j]:
                nums[j] = 102
                Counter += 1
                j += 1
            
            print(Counter)

            i = j 
        nums.sort()
        return len(nums) - Counter
        
        