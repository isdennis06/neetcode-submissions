class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        # Step 1: count occurrences
        for n in nums:
            count[n] = count.get(n, 0) + 1

        # Step 2: bucket numbers by their frequency
        for n, c in count.items():
            freq[c].append(n)

        # Step 3: gather the k most frequent, from highest frequency down
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                    
        