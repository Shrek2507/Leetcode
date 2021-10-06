from typing import List
from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        boolContainsNearbyDuplicate = False
        numsDict = {}

        if len(nums) <= 1:  # No duplicates found...
            return boolContainsNearbyDuplicate
        elif len(set(nums)) == len(nums):   # If all are distinct...
            return boolContainsNearbyDuplicate
        else:
            for index, num in enumerate(nums):
                if num not in numsDict:
                    numsDict[num] = index
                else:
                    currentIndex = index
                    previousIndex = numsDict[num]

                    # Check the diff...
                    if abs(currentIndex - previousIndex) <= k:
                        boolContainsNearbyDuplicate = True
                    else:
                        numsDict[num] = currentIndex

        return boolContainsNearbyDuplicate


objSol = Solution()
nums = [1, 2, 3, 1, 2, 3]
k = 2

# get the result...
result = objSol.containsNearbyDuplicate(nums, k)
print(result)
