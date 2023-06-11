class Node:
    def __init__(self, data):
      self.data = data
      self.next = None
      

class SingleLinkedList:
    def __init__(self):
      self.head = None
      
    def is_empty(self):
        return self.head is None
    
    
    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def insert_at_tail(self, data):
        new_node = Node(data)
        
        if self.is_empty():
            print("Linked list is empty and new is now the head")
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
         
            
    def insert_after(self, target_value, new_data):
        new_node = Node(new_data)
        
        current = self.head
        while current:
            if current.data == target_value:
                new_node.next = current.next
                current.next = new_node
                break
            current = current.next
        return True
    
    
    def delete_Node(self, target_value):
        if self.is_empty():
            print("Cannot delete, linked list is empty.")
            return False
        
        if(self.head.data == target_value):
            self.head = self.head.next
            return True
        current =  self.head
        while current.next:
            if(current.next.data == target_value):
                current.next = current.next.next
                break
            current = current.next
        return True
    
    
    def display(self):
        if(self.is_empty()):
            print("Linked list is empty!")
            return 
        current_node = self.head
        while  current_node:
            print('[{}]'.format(current_node.data))
            current_node = current_node.next
            
            
            
singleLLst = SingleLinkedList()
print("is_empty ", singleLLst.is_empty())
singleLLst.insert_at_tail(1)
singleLLst.insert_at_tail(2)
singleLLst.insert_at_tail(3)
singleLLst.insert_at_tail(4)
singleLLst.insert_at_head(55)
singleLLst.insert_after(3,21)
print("display ", singleLLst.display())
singleLLst.delete_Node(21)
singleLLst.delete_Node(2)
singleLLst.delete_Node(1)
print("display ", singleLLst.display())
