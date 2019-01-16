#Better Solution required

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    

               
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None or head.next is None:
            return head
        
        
        def checkHead():
            
            nonlocal head
            bool_head = False
        
            #check for the head for duplicates
            while True:
            
                #if one element left
                if head.next is None:
                    if bool_head == True:
                        head = None
                        return
                    else:
                        return
            
            
                '''debug
                debug_node = head
                while debug_node.next is not None:
                    print(debug_node.val,end='->')
                    debug_node = debug_node.next
                print(debug_node.val)
                print('\n')'''
            
            
                if head.val != head.next.val:
                
                    #if the current head position was duplicate 
                    if bool_head == True:
                        head = head.next
                        checkHead()
                
                
                    #simply continue to check for other values
                    break
                else:
                    #just move the head to the next position
                    head = head.next
                    bool_head = True

                    
        checkHead() 
        #check if there is only one or two elements are left in the list
        if head is None or head.next is None or head.next.next is None:
            return head
    
        
        first = head
        second = head.next
        third = second.next
        bool_dup = False
        
        
        while True :
            #check if there is only one or two elements are left in the list
            if head.next is None or head.next.next is None:
                return head
                
        
            #debug
            debug_node = head
            print('printed from here')
            while debug_node.next is not None:
                print(debug_node.val,end='->')
                debug_node = debug_node.next
            print(debug_node.val)
            print('\n')
        
        
            if second.val != third.val:
                if bool_dup == True:
                    #similar to the main else condition
                    first.next = second.next
                    second = second.next
                    third = second.next
                    bool_dup = True
                
                else:
                    #simply move every node to next position
                    '''1(f)->2(s)->3(t)->3->4
                    1->2(f)->3(s)->3(t)->4'''
                    if third.next is None:
                        return head
                    first = second
                    second = third
                    third = second.next
            else:
                '''1->2(f)->3(s)->3(t)->4
                1->2(f)->3(s)->4(t)'''
                #first will remain at place
                #second will be removed and the forwaded
                #third will move forward
                
                if third.next == None:
                    first.next = None
                    return head
                first.next = second.next
                second = second.next
                third = second.next
                bool_dup = True
            
            
        return head
