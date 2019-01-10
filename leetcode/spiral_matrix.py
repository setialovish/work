class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        if len(matrix) == 0:
            return []
        list_output = []
        list_temp = []
        int_m = len(matrix)
        int_n = len(matrix[0])
        
        
        while True:
            
            for element in matrix[0]:
                list_output.append(element)
                
            del matrix[0]
            
            if len(matrix) == 0:
                return list_output
                break
            
            for i in range(len(matrix[0])-1,-1,-1):
                list_temp.append(list(item[i] for item in matrix))
            matrix=list_temp
            list_temp = []
        
