class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr=[]
        if len(nums) != 0:
            for i in range(len(nums)):
                arr.append(nums[i])
        return arr*2
            
