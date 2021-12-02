class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        if isBadVersion(n-1) is False :
            return n
        last_good = 0
        first_bad = 0
        idx = 0
        idx2 = n
        while last_good != first_bad-1 :
            if isBadVersion((idx2+idx)//2) :
                idx2 = (idx2+idx)//2
                first_bad = idx2
            else :
                idx = (idx2+idx)//2
                last_good = idx
        return first_bad
