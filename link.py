class node:
    def __init__(self,data):
        self.data = data
        self.next = next
class linkedlist:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next!=None:
            total+=1
            cur = cur.next
        return total
    
    def display(self):
        elems = []
        cur = self.head
        while cur.next!=None:
            cur= cur.next
            elems.append(cur.data)
        print(elems)

    def erase(self,index):
        if index>=self.length() or index<0:
            print("Error: 'Erase' Index out of range")
            return
        cur_idx = 0
        cur = self.head
        while True:
            lastnode = cur
            cur = cur.next
            if cur_idx == index:
                lastnode.next = cur.next
                return
            cur_idx+=1

    
    def get(self,index):
        if index>=self.length() or index<0:
            print("Error: 'Get' Index out of range")
            return
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx+=1
    

    def insert(self,index,data):
        if index>=self.length() or index<0:
            return self.append(data)
        cur_node = self.head
        priornode = self.head
        cur_idx = 0
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                new_node = node(data)
                priornode.next = new_node
                new_node.next = cur_node
                return
            priornode = cur_node
            cur_idx+=1
    

    def insert_node(self,index,node):
        if index<0:
            print("Error: 'Insert_node' Index out of range")
            return
        if index>=self.length():
            curnode = self.head
            while curnode.next!=None:
                curnode = curnode.next
            curnode.next =node 
            return
        cur_node = self.head
        priornode = self.head
        cur_idx = 0
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                priornode.next = node
                return
            priornode = cur_node
            cur_idx+=1

    def set(self,index):
        if index>=self.length() or index<0:
            print("Error: 'Get' Index out of range")
            return
        cur_node = self.head
        cur_idx = 0
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                cur_node.data = data
                return
            cur_idx+=1