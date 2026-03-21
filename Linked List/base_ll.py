class node :
    def __init__(self,value) :
        self.value = value
        self.next = None
        

class linklist:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_at_head(self, data):
        if self.head is None:
            self.head = node(data)
            self.size += 1
        else: 
            self.node = node(data)
            self.node.next = self.head
            self.head = self.node
            self.size += 1

    def add_at_tail(self, data):
        if self.head is None:
            self.head = node(data)
            self.size += 1
        else:
            temp = self.head
            while temp.next != None :
                temp = temp.next
            temp.next = node(data)
            self.size += 1
    
    def add_at_index(self, index, data):
        if index < 0  or index > self.size:
            print("index out of bound")
            return
        if index == 0:
            self.add_at_head(data)
        elif index == self.size:
            self.add_at_tail(data)
        else:
            temp1 = self.head
            temp2 = self.head.next
            for _ in range (index - 1):
                temp1 = temp1.next
                temp2 = temp2.next
            new_node = node(data)
            temp1.next = new_node
            new_node.next = temp2
            self.size += 1
            

    
    def __str__(self):
        temp = self.head
        res = ""
        while temp is not None:
            res += str(temp.value) + "-> "
            temp = temp.next
        res += "None"
        return res

    def __len__(self):
        return self.size
if __name__ == "__main__":    
    li = linklist()
    li.add_at_head(1)
    li.add_at_head(2)
    li.add_at_tail(0)
    print(li)
    # print(len(li))
