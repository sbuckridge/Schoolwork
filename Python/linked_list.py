## 
# @file linked_list.py
#
# Template for linked_list class.
#

#Samuel Buckridge
#Class time: 13:00 - 14:15

class node :
    def __init__(self, item, prev = None, next = None) : 
        self.item = item
        self.prev = prev
        self.next = next

    def __str__(self) :
        return str(self.item)

    def __repr__(self) :
        return repr(self.item)


## linked_list
# Implements a doubly-linked list ADT
# @invariant (len == 0 and head == None and tail == None)
#         or (len != 0 and head != None and tail != None and head.prev == None and tail.next == None)
# You do not have to call your data members head/tail, but should be descriptive names
class linked_list :

    ## constructor - iterable is an iterable object that initializes
    #  the linked_list in the order iterable is traversed
    def __init__(self, iterable = []) :
        self.iterable = iterable
        self.head = None
        self.tail = None

    ## constant time access to first/last node, respectively
    #  @returns the first/last node, respectively
    def front(self) : 
        return self.head #returns the head, or the front of the list

    def back(self) : 
        return self.tail #returns tail of the list

    ## constant time insertion of a data item (any element)
    #  as the first/last (respectively) element 
    def push_front(self, item) :
        new_node = node(item) #create new node
        if self.head == None : #if the head is empty, this node is now the head and tail
            self.head = new_node
            self.tail = new_node
        else :
            new_node.next = self.head #else, attach new node in front of head
            new_node.next.prev = new_node #set prev of old head to new node
            self.head = new_node #make new node the head

    def push_back(self, item) :
        new_node = node(item)
        if self.head == None : #if the head is empty, this is the head and tail
            self.head = new_node
            self.tail = new_node
        else :
            self.tail.next = new_node #put new node after the tail
            new_node.prev = self.tail #set prev of new node to the old tail
            self.tail = self.tail.next #set tail to the end of the list


    ## constant time removal of the first/last (respectively) node/item
    #  @returns the item (not the node)
    def pop_front(self) : 
        self.head.next = self.head #set new head to the node next to head
        self.head.prev = None #deleting old head node

    def pop_back(self) :
        self.tail.prev = self.tail #set tail to node next to the tail
        self.tail.next = None #delete old tail node

    ## Turns list into a string representation.
    #  Strings prints identical to how 
    #  it would if it were a Python list
    #  @returns the string representation 
    def __str__(self) : 
        temp = self.head
        listStr = '['

        while temp.next != None : #traverse list until last node
            listStr = listStr + temp.item + ', ' #build string
            temp = temp.next

        listStr = listStr + temp.item + ']' #finish off the string by adding the last value and bracket

        return listStr
        

    ## converts linked list to a bool
    #  @returns False if empty, True otherwise
    def __bool__(self) : 
        if self.head == None : #if list is empty, return false
            return False
        else : #else, true
            return True
            

    ## Computes length of linked list
    #  @returns the length of the linked list 
    def __len__(self) : 
        counter = 0 #set counter variable to 0
        temp = self.head #set temp to head of list

        while temp != None : #traverse list until it's exhausted and increment counter by 1
            counter += 1
            temp = temp.next

        return counter
        

    ## implements in operator
    #  @returns True if item is in linked-list, False otherwise
    def __contains__(self, item) : 
        temp = self.head

        while temp != None : #traverse until end of list
            if temp.item == item : #if the node contains item, return true
                return True
            else : #otherwise, go to next node
                temp = temp.next

        return False #if loop exits, that means it was not found
