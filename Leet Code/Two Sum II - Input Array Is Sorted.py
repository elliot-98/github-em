class Solution:
    def twoSum(self, numbers, target):
        begin, end = 0, len(numbers)-1
        if numbers[begin] + numbers[end] == target :
            return (begin+1, end+1)
        while begin<end:
            if numbers[begin] + numbers[end]<target:
                begin+=1
            elif numbers[begin] + numbers[end]>target:
                end-=1
            else:
                return(begin+1, end+1)
