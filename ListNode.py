class ListNode:
    def __init__(self, data):
        self.data=data
        self.link: ListNode=None #stores the next node

    def __str__(self):
        return str(self.data)

    def get_data(self) -> any:
        return self.data
    
    def set_data(self, new) -> any:
        self.data=new
        return new
    
    def get_next(self):
        return self.link
    
    def set_next(self, node):
        self.link=node
        return node
