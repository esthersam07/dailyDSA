class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        j = 0
        while j<len(chars):
            curr = chars[j]
            count = 0
            while j<len(chars) and chars[j]==curr:
                j += 1
                count += 1
            chars[i] = curr
            i+=1
            if count>1:
                for d in str(count):
                    chars[i] = d
                    i+=1
        return i
        