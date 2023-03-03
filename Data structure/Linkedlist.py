class Node:
    def __init__(self, data, address=None):
        self.data = data
        self.next = next

    # def addData(data):
    #     node = head
    #     while node.address:
    #         node = node.address
    #     node.address = Node(data)

class LinkedList:
    def __init__(self):
        self.head = Node('head')
    def find(self, item):
        cur_node = self.head
        while cur_node.data != item:
             cur_node = cur_node.next
        return cur_node
    def insert(self, current, new):
        new_node = Node(new)
        cur_node = self.find(current)
        new_node.next = cur_node.next
        cur_node.next = new_node
    def show(self):
         cur_node = self.head
         while cur_node.next is not None:
              print(cur_node.data, end='->')
              cur_node=cur_node.next
         print(cur_node.data)
# secNode = Node('second')
# head = secNode
# Node.add('third')

# # 출력
# node = head
# while node.address:
# 	print(node.data)
#     node = node.next
# print(node.data)	# second \n third
boo = LinkedList()
boo.insert('head','1')
boo.insert('1','2')
boo.insert('2','3')
boo.insert('3','4')
boo.show()