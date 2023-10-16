
class Node:
    def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None
      
      
      
class DoubleLinkedList:
    def __init__(self):
      self.head = None
      self.tail = None
      
    def is_empty(self): # O(1) time, O(1) space
        return self.head is None
    
    
    def insert_at_tail(self, data): # O(1) time, O(1) space
        new_node =  Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail =  new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node  # set the current tail
            
    
    def insert_at_head(self, data): #O(1) time, O(1)
        new_Node = Node(data)
        if self.is_empty():
            self.head = new_Node
            self.tail = new_Node
        else:
            new_Node.next = self.head
            self.head.prev = new_Node
            self.head = new_Node
            
            
    def display_forward(self): # O(n) Time, O(1) space
        if self.is_empty():
            return False
        current = self.head
        while current:
            print(current.data,  end=" <=>  " )
            current = current.next            
            
            
    def display_backward(self):# O(n) Time, O(1) space
        if self.is_empty():
            return False
        current = self.tail
        while current:
            print(current.data,  end=" <=> ")
            current = current.prev
            
    
    def insert_at_position(self, position, data): # O(n) time, O(1) space
        if position < 0:
            print("Position must not be less than 0")
            return
        
        new_Node = Node(data)
        if (position ==  0):
            self.insert_at_head(data)
        else:
            current = self.head
            for i in range(position - 1):
                if current is None:
                    print("Position is not found")
                    return
                current = current.next
            new_Node.next = current.next
            current.next =  new_Node
            
    
    def search(self, value): # O(n) time, O(1) space
        if self.is_empty():
            return False
        current = self.head
        count = 0
        while current:
            if current.data == value:
                return count
            current = current.next
            count += 1
        return None
        
            
    def remove_from_head(self): # O(1) time, O(1) space
        if self.is_empty():
            return False
        data = self.head.data
        if self.head ==  self.tail:
            self.head = None
            self.tail =  None
            return data
        else:
            self.head = self.head.next
            self.head.prev = None
            return data
        
    def remove_from_tail(self):  # O(1) time, O(1) space
        if self.is_empty():
            return False
        data =  self.tail.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return data
        else:
            self.tail = self.tail.prev
            self.tail.next =  None
            return data
        
        
        

doubleLL =  DoubleLinkedList()
doubleLL.insert_at_tail(1)
doubleLL.insert_at_tail(4)
doubleLL.insert_at_tail(2)
doubleLL.insert_at_tail(3)
doubleLL.insert_at_head(44)
doubleLL.insert_at_head(48)
doubleLL.display_forward()
data = doubleLL.remove_from_tail()
print("Break  \n" , data)
doubleLL.display_forward()
# index = doubleLL.search(2)
# print("index ", index)
# doubleLL.insert_at_position(66, 6)
# doubleLL.display_backward()
            

 



        
            
        