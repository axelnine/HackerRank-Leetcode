import collections
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = collections.Counter(s).most_common()
        return ''.join([''.join(i[0]*i[1]) for i in count])
