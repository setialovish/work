class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        #Global variables
        list_output = []
        str_change_var = 'j'
        str_inc_dec = 'inc'
        int_i = 0
        int_j = 0
        int_change_counter = 0

        
        if len(matrix) == 0 or len(matrix[0]) == 0 :
            return []
        elif len(matrix) == 1:
            return matrix[0]
        int_m = len(matrix)
        int_n = len(matrix[0])

        
        
        def change_direction():
            nonlocal int_change_counter, str_change_var,str_inc_dec
            
            int_change_counter += 1
            
            '''increment and decrement shall take place like
            inc, inc, dec, dec, inc, inc, dec, dec'''    
            if (int_change_counter % 2) == 0 and int_change_counter != 0:
                
                if str_inc_dec == 'inc':
                    str_inc_dec = 'dec'
                else:
                    str_inc_dec = 'inc'
                                        
            
            if str_change_var == 'j':
                str_change_var = 'i'
            elif str_change_var == 'i':
                str_change_var = 'j'
            
            
        def increment_decrement():
        
            nonlocal  int_i, int_j
            

            
            if str_inc_dec == 'inc':
                if str_change_var =='j':
                    int_j += 1
                else:
                    int_i += 1
            elif str_inc_dec == 'dec':
                if str_change_var == 'j':
                    int_j -= 1
                else:
                    int_i -= 1
            
                
        def revert():
            nonlocal int_i, int_j
            if str_inc_dec == 'dec':
                if str_change_var == 'i':
                    int_i += 1
                else:
                    int_j += 1
            else:
                if str_change_var == 'i':
                    int_i -= 1
                else:
                    int_j -= 1
            
            
        #for i in range(len(matrix)**2+3):
        while True:    
            ''' 4 conditions to be checked
            1) i==0 and j==len(matrix) - 1
            2) i==len(matrix)-1 and j==len(matrix)-1
            3) i==len(matrix)-1 and j==0
            4) matrix[i][j] already in the o/p matrix'''

            
            if int_i==0 and int_j== int_n-1:
                list_output.append(matrix[int_i][int_j])
                change_direction()
            elif int_i == int_m-1 and int_j==int_n-1:
                list_output.append(matrix[int_i][int_j])
                change_direction()                
            elif int_i==int_m-1 and int_j==0:
                list_output.append(matrix[int_i][int_j])
                change_direction()
            elif matrix[int_i][int_j] in list_output:
                
                #come to the previous location somehow 
                revert()
                change_direction()
                
            else:
                list_output.append(matrix[int_i][int_j])
                
                #increment_decrement()
            increment_decrement()
            if len(list_output) == int_m*int_n:
                break
        
        
        return list_output
