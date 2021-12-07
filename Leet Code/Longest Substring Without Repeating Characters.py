class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maximum1 = 0
        maximum2 = set()
        letters = {}
        j=0
        for (k,i) in enumerate(s) :
            if i in letters :
                maximum2.add(maximum1)
                maximum1 = k-letters[i]-1
                letters.pop(i)
            maximum1+=1
            letters[i] = k
        maximum2.add(maximum1)
        if len(maximum2) == 0:
            return len(s)
        return(max(maximum2))
