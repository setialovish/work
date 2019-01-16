# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        '''1->4->3->2->5->2 and x = 3'''
        
        counter = 0
        iterator = head
        last_s = head 
        last_g = head # The leftmost number greater than x
        
        #check if the head is None
        if head  is None:
            return head
        
        #Find the leftmost largest and its left element
        while iterator.next is not None:
            
            #Check if the number is greater
            if iterator.val >= x:
                last_g = iterator
                break
                
            iterator = iterator.next
            
            if counter != 0:
                last_s = last_s.next
            counter = 1
        
        '''1->4->3->2->5->2
        last_g->4 and last_s->1'''
        
        #Check if there was no number greater than x(1->1 and x = 2)
        if last_g.val < x:
            print('returning from here')
            return head
        
        #move the smaller element before the leftmost largest number
        
        iterator = last_g
        while iterator.next is not None:
            
            #value is greater or equal to x then simply move fwd.  
            if iterator.next.val >= x:
                #just move forward
                iterator = iterator.next                
            else:
                #create a temporary new node
                temp_node = ListNode(iterator.next.val)#1
                
                #2-->1-->1 and x = 2
                if last_g == last_s:
                    temp_node.next = last_g
                    last_s = temp_node
                    if iterator.next.next is not None: #2-->1  
                        iterator.next = iterator.next.next
                        head = temp_node
                    else:#2-->1-->1
                        iterator.next = None
                        return temp_node
                    continue
                    
                #place the newly created node
                last_s.next = temp_node
                last_s = last_s.next
                last_s.next = last_g
                iterator.next = iterator.next.next
        
        return head
        
        

        
        print('the first largest node is:{} and previous element is:{}'.format(last_g.val, last_s.val))
        
        
