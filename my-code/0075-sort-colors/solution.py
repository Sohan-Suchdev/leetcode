class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        high = len(nums)-1
        i=0

        while i <= high:
            if nums[i]==0:
                temp = nums[i]
                nums[i] = nums[low]
                nums[low] = temp
                low+=1
                i+=1
            elif nums[i]==2:
                temp = nums[i]
                nums[i] = nums[high]
                nums[high] = temp
                high-=1
            else:
                i+=1


            
