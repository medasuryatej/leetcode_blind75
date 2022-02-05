class Solution:
    def countBits(self, n: int) -> List[int]:
        counter = [0]
        for i in range(1, n+1):
        	# ex: 3 >> 1 = 3 // 2 = 1
        	#     and 3 % 2 = 1
        	#     therefor 3 >> 1 + 3 % 2 = 1 + 1 = 2
            counter.append(counter[i>>1] + i%2)
        return counter