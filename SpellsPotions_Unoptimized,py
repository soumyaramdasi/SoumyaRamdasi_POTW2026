class Solution:

    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:

        succ_pairs = []
        count = 0

        for i in range(len(spells)):

            for j in range(len(potions)):

                if spells[i] * potions[j] >= success:

                    count += 1
            
            succ_pairs.append(count)
            count = 0
        
        return succ_pairs
