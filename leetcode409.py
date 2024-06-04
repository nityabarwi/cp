def longestPalindrome(self, s: str) -> int:
        char = Counter(s)
        length = 0
        odd = False

        for count in char.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                odd = True
        if odd:
            length += 1

        return length
