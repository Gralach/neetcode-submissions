class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for temperature in range(len(temperatures)):
            check = temperature
            while check <= len(temperatures):
                if (check == len(temperatures)):
                    result.append(0)
                    break
                if temperatures[check] > temperatures[temperature]:
                    result.append(check - temperature)
                    break
                else:
                    check += 1
                
        return result