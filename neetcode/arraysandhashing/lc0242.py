class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        for i in range(0, len(s)):
            index_s = ord(s[i]) - ord('a')
            index_t = ord(t[i]) - ord('a')
            count[index_s] += 1
            count[index_t] -= 1
        for num in count:
            if num != 0:
                return False
        return True

    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = {}
        count_t = {}
        for ch in s:
            count_s[ch] = count_s.get(ch, 0) + 1
        for ch in t:
            count_t[ch] = count_t.get(ch, 0) + 1
        return count_s == count_t


if __name__ == '__main__':
    sol = Solution()
    s = 'anagram'
    t = 'nagaram'
    print(sol.isAnagram(s, t))
