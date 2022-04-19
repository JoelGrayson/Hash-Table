from ListNode import ListNode

class LinkedList:
    def __init__(self, data=None):
        self.head=None
        self.length=0
        if data!=None: #optional data parameter becomes LinkedList
            for item in data:
                self.add_first(item)

    def add_first(self, val):
        new_head=ListNode(val)
        new_head.set_next(self.head)
        self.head=new_head
        self.length+=1
    
    def pop_first(self) -> any: #:node val
        old_head=self.get_head()
        self.head=old_head.get_next() #assign second node as first
        self.length-=1
        return old_head
    
    def get_head(self):
        return self.head
    
    def get_length(self):
        return self.length
    
    def get_node(self, index=None) -> ListNode:
        if index is None:
            # get node at position of iterator
            if self.current_node is None:
                raise Exception('Uninitialied iterator')
            return self.current_node
       
        if index<0: #if negative index, go from back of list
            index+=self.length

        node=self.head
        for i in range(index):
            node=node.get_next()
        return node
    
    def get(self, index=None) -> any:
        return self.get_node(index).get_data()

    def set(self, index, val):
        self.get_node(index).set_data(val)
        return val
    
    def insert(self, index, val):
        # Error check index
        if index>self.length-1 or index<0:
            raise IndexError('Index out of bounds')
        if type(index).__name__=='float':
            raise TypeError('Index must be an integer')
        if index==0:
            return self.add_first(val)

        # Adds node after `before` and connects to `after`
        before: ListNode=self.get_node(index-1)
        ''; #acts as indentation that doesn't trigger IndentationError
        ''; after: ListNode=before.get_next()
        '  '; inserting=ListNode(val)
        ''; inserting.set_next(after)
        before.set_next(inserting)

        self.length+=1
        
    def pop(self, index) -> any: #:ListNode val
        #Error checking
        if index>self.length-1 or index<0:
            raise IndexError('Index out of bounds')
        if type(index).__name__=='float':
            raise TypeError('Index must be an integer')
        if index==0: #prevent circular loop
            return self.pop_first()

        self.length-=1
        # Remove pop from chain, and link before to after
        before=self.get_node(index-1) #before pop
        to_pop=before.get_next()
        after=to_pop.get_next()
        before.set_next(after)
        return to_pop.get_data()
    
    def extend(self, lst): #adds LinkedList to end
        last=self.get_node(self.length-1)
        self.length+=lst.get_length() #add lst's length to own length
        last.set_next(lst.get_head()) #sets last's next item to head of second list
    
    def merge(self, lst): #sorted list
        item=None
        while lst.get_length():
            val=lst.pop_first()

    def to_list(self):
        lst=[]
        i=0
        l=self.get_length()
        node=self.get_head()
        while True:
            if i>=l-1:
                break
            lst.append(node)
            node=node.get_next()
            i+=1
        return lst
                    
    # Dunder methods
    def __str__(self): # | c | -> | b | -> | a |
        s=''
        node=self.get_head()
        i=0
        l=self.get_length()
        while True:
            if i>=l-1:
                break
            s+=f'| {node} | -> '
            node=node.get_next()
            i+=1
        
        s+=f'| {node} |'
        return s
        
    def __getitem__(self, index):
        return self.get(index)

    def __setitem__(self, index, value):
        return self.set(index, value)

    def __len__(self):
        return self.get_length()
    
    # def __iter__(self): #shortcut
    #     return iter(self.to_list())

    def __iter__(self):
        self.current_node=self.get_head()
        return self

    def __next__(self):
        if self.current_node is None:
            raise StopIteration() #exception to stop iterating
        buff=self.current_node.get_data()
        self.current_node=self.current_node.get_next()
        return buff