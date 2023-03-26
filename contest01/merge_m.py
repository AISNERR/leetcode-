class Solution:
     def mergeArrays(self, nums1, nums2):
        ans = [] # array 
        i = j = 0 
        while i < len(nums1) or j < len(nums2): 
            if j == len(nums2) or i < len(nums1) and nums1[i][0] <= nums2[j][0]: 
                ans.append(nums1[i])
                i += 1
            else: 
                if ans and ans[-1][0] == nums2[j][0]: 
                    ans[-1][1] += nums2[j][1]
                else: 
                    ans.append(nums2[j])
                j += 1
        return ans 
    

nums1 = [[1,2],[2,3],[4,5]]
nums2 = [[1,4],[3,2],[4,1]]
nums3 = [[2,4],[3,6],[5,5]]
nums4 = [[1,3],[4,3]]
res = Solution()
print(res.mergeArrays(nums3, nums4))