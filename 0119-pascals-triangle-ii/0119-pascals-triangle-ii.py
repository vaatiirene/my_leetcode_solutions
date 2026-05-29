class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res =[[1]]
        for i in range(rowIndex):
            temp_row = [0] + res[-1] + [0]
            row=[]
            for j in range (len(res[-1]) + 1):
                row.append(temp_row[j] + temp_row[j+1])
            res.append(row)
        return res[rowIndex]
        