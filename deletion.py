class node:
  def__init_(self,data=none):
  self.data=data
  self.next=none
class slinked list:
  def__init_(self):
   self.head=none
  def at begining(self.data_in):
   newnode=node(data_in):
   newnode.next=self.head
   self.head=newnode
  def remove node(self,removekey):
   headval=self.head
   if(headval is not none):
     if(headval.data==removekey):
       self.head=headval.next
       headval=none
       return
  while(headval is not none)
   if headval.data==removekey:
     break
   prev=headvalheadval
   =headval.next
   if(head val==none):
     return
   prev.next=headval.next
   headval=none
def llistprint(self):
  printval=self.head
  while(printval):
    print(printval.data)
    printval=printval.next
llist=slinkedlist()
llist.atbegining("mon")
llist.atbegining("tue")
llist.atbegining("wed")
llist.atbegining("thu")
llist.llistprint()
