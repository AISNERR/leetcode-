import collections


class Solution(object):
    def mergeArrays(self, nums1, nums2):
        items = collections.defaultdict(int)
        for k, v in nums1:
            items[k] += v
        for k, v in nums2:
            items[k] += v
        return sorted(zip(items.keys(), items.values()))
        #return zip(items.keys(), items.values())
    

nums1 = [[1,2],[2,3],[4,5]]
nums2 = [[1,4],[3,2],[4,1]]
nums3 = [[2,4],[3,6],[5,5]]
nums4 = [[1,3],[4,3]]
res = Solution()
print(res.mergeArrays(nums3, nums4))