
class Solution:

    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:

        potions.sort()
        succ_pairs = []

        for spell in spells:

            left = 0
            right = len(potions)

            while left < right:

                mid = (left + right) // 2

                if spell * potions[mid] >= success:

                    right = mid

                else:
                    
                    left = mid + 1

            count = len(potions) - left
            succ_pairs.append(count)

        return succ_pairs
