class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        #GLOBAL variables
        matrix = []
        list_sec = []
        list_temp = []
        list_output = [[x for x in range(x,x+n)] for x in range(0,n**2,n)  ]
        list_output_1 = list_output.copy()
        
        #print(list_output)
        '''[1,2,3]
           [4,5,6],
           [7,8,9]'''
        
    
        
        for i in range(n):
            matrix.append([str(i)+','+str(x) for x in range(n)])
        
        #print(matrix)
        '''[['0,0', '0,1', '0,2'],
            ['1,0', '1,1', '1,2'],
            ['2,0', '2,1', '2,2']]'''

        #spiral matrix traversal using transpose method
        #Q54 for reference
        while True:
            list_sec.append([x for x in matrix[0]])
            
            del matrix[0]
            if len(matrix) == 0:
                break
            
            for j in range(len(matrix[0])-1,-1,-1):
                list_temp.append([item[j] for item in matrix])
            
            matrix = list_temp
            list_temp = []
            
        #print(list_sec)   
        '''[['0,0', '0,1', '0,2'], ['1,2', '2,2'], ['2,1', '2,0'], ['1,0'], ['1,1']]'''
        
        #consolidated list
        list_temp = [j  for x in list_sec for j in x ]
        
        #print(list_temp)
        #split each element by , and place the elements 
        for i in range(n**2):
            
            list_positions = list_temp[i].split(',')
            x = int(list_positions[0])
            y = int(list_positions[1])
            #print(list_positions)
            list_output_1[x][y] = i + 1

        return list_output_1
            
            
        
    
        
            
       
        
        
            
            
                
