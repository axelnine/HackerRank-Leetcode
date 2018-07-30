#Manipulate power of two while counting ones in binary
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        list = []
        candidates = sorted(candidates)
        self.getResult(list, [], candidates, target,0)
        return list

    def getResult(self, list, templist, candidates,target,start):
        if target <0:
            return
        elif target == 0:
            list.append(templist[:])
        else:
            for i in range(start,len(candidates)):
                templist.append(candidates[i])
                self.getResult(list, templist, candidates,target-candidates[i],i)
                templist.pop(len(templist)-1)

        
