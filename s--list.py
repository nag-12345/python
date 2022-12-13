class node:
    slots='element','next'
    def __init__(self,element,next):
        self.element=element
        self.next=next
class linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def __len__(self):
        return self.size
    def isempty(self):
        return self.size==0
    def addlast(self,e):
        new = node(e,None)
        if self.isempty():
            self.head = new
        else:
            self.tail.next = new
        self.tail=new
        self.size+=1
    def addfirst(self,e):
        new = node(e,None)
        if self.isempty():
            self.head = new
            self.tail=new
        else:
            new.next=self.head
            self.head=new
        self.size+=1
    def search(self,key):
        p=self.head
        index=1
        while p:
            if p.element==key:
               return index
            p=p.next
            index+=1
        return l
    def addany(self,e,position):
        new=node(e,None)
        p=self.head
        i=1
        while i < position-1:
            p=p.next
            i=i+1
        new.next=p.next
        p.next=new
        self.size+=1
    def delfirst(self):
        if self.isempty():
            print('list is empty')
            return
        e=self.head.element
        self.head=self.head.next
        self.size-=1
        if self.isempty():
            self.tail=None
        return e
    def dellast(self):
        if self.isempty():
            print('list is empty')
            return
        p=self.head
        i=1
        while i < len(self)-1:
            p=p.next
            i=i+1
        self.tail=p
        p=p.next
        e=p.element
        self.tail.next=None
        self.size-=1
        return e
    def delany(self,position):
        p=self.head
        i=1
        while i < position-1:
            p=p.next
            i = i+1
        e=p.next.element
        p.next = p.next.next
        self.size-=1
        return e
    def display(self):
        p=self.head
        while p:
            print(p.element,end='-->')
            p=p.next
        print()
l=linkedlist()
l.addlast(10)
l.addlast(20)
l.display()
k=l.search(20)
print(k)
l.addfirst(30)
l.addfirst(40)
l.display()
l.addany(50,3)
l.display()
l.delfirst()
l.display()
l.dellast()
l.display()
l.delany(2)
l.display()
print('size',len(l))

