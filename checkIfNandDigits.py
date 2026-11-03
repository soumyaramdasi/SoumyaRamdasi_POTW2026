class Solution:

    def checkIfExist(self, arr: list[int]) -> bool:

        for i in range(len(arr)):

            for j in range(1, len(arr)):

                if arr[i] == arr[j] * 2 or arr[j] == arr[i] * 2:

                    if i != j:

                        return True
        
        return False
