class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """

        seen = set()
        m = len(image)
        n = len(image[0])
        oldColor = image[sr][sc]

        def fill(sr, sc):

            if ((sr, sc) not in seen) & (0 <= sr < m) & (0 <= sc < n):
                if image[sr][sc] == oldColor:
                    image[sr][sc] = newColor
                    seen.add((sr, sc))
                    fill(sr + 1, sc)
                    fill(sr, sc + 1)
                    fill(sr - 1, sc)
                    fill(sr, sc - 1)

        fill(sr, sc)
        return image
