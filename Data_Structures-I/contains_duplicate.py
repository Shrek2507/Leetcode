from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsDict = dict()
        boolContainsDuplicate = False
        for n in nums:
            if n in numsDict.keys():
                numsDict[n] += 1    # Increment by one...
            else:
                numsDict[n] = 1

        for n, c in numsDict.items():
            if c >= 2:   # Check if the count is atleast 2....
                boolContainsDuplicate = True

        return boolContainsDuplicate


# Create a solution object...
obj_Sol = Solution()
arr = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

result = obj_Sol.containsDuplicate(arr)
print(result)
