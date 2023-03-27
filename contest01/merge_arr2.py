# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    merge_arr2.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aisner <aisner@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/27 23:19:04 by aisner            #+#    #+#              #
#    Updated: 2023/03/27 23:19:05 by aisner           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import collections


class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        items = collections.defaultdict(int)
        res2 = []
        for k, v in nums1:
            items[k] += v
        for k, v in nums2:
            items[k] += v
        res3 = sorted(zip(items.keys(), items.values()))
        for i in res3:
            res2.append(list(i))
        return res2
    

nums1 = [[1,2],[2,3],[4,5]]
nums2 = [[1,4],[3,2],[4,1]]
nums3 = [[2,4],[3,6],[5,5]]
nums4 = [[1,3],[4,3]]
res = Solution()
 
print(res.mergeArrays(nums3, nums4))
   