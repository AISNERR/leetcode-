# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    hourllass.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aisner <aisner@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/27 23:18:54 by aisner            #+#    #+#              #
#    Updated: 2023/03/27 23:18:55 by aisner           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Maximum Sum of an Hourglass
# You are given an m x n integer matrix grid.

# We define an hourglass as a part of the matrix with the following form:
# Return the maximum sum of the elements of an hourglass.

# Note that an hourglass cannot be rotated and must be entirely contained within the matrix.


from typing import List


class Solution:
    """
    Time:   O(n*m)
    Memory: O(n*m)
    """

    def maxSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        return max(
            self.get_hourglass(grid, i, j)
            for i in range(1, n - 1)
            for j in range(1, m - 1)
        )

    @staticmethod
    def get_hourglass(grid: List[List[int]], i: int, j: int) -> int:
        return grid[i - 1][j - 1] + grid[i - 1][j] + grid[i - 1][j + 1] + \
                                    grid[i][j] + \
               grid[i + 1][j - 1] + grid[i + 1][j] + grid[i + 1][j + 1]

