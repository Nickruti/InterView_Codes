#----------------------------------------------------------------
#Companies - Amazon, VMWare, Riverbed
#----------------------------------------------------------------

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        listElem = list(A)
        listElem.sort()
        lastElem = listElem[0]
        for i in range(1, len(A)):
            if lastElem == listElem[i]:
                return lastElem
            else:
                lastElem = listElem[i]
        return -1
