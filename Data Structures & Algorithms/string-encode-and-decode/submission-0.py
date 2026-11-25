class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            # find the delimiter that ends the length prefix
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            # the string starts right after '#' and spans `length` chars
            res.append(s[j + 1 : j + 1 + length])
            # move to the start of the next encoded string
            i = j + 1 + length

        return res
        