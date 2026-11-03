class Solution:

    def heightChecker(self, heights: list[int]) -> int:
        
        expected = sorted(heights)
        nonmatching = 0

        for i in range(len(heights)):

            if heights[i] != expected[i]:

                nonmatching = nonmatching + 1
    
        return nonmatching
