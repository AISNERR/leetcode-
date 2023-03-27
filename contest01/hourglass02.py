# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    hourglass02.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aisner <aisner@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/27 23:12:51 by aisner            #+#    #+#              #
#    Updated: 2023/03/27 23:18:47 by aisner           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from typing import List

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        def solve(grid, row, col):
            return (grid[row][col] + grid[row-1][col] + grid[row-1][col-1] + grid[row-1][col+1] + grid[row+1][col] + grid[row+1][col-1] + grid[row+1][col+1])
        currSum = float("-inf")
        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[0])-1):
                temp = solve(grid, i, j)
                if currSum < temp:
                    currSum = temp
        return currSum
    

grid = [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]
s = Solusion()
print(s.maxSum)