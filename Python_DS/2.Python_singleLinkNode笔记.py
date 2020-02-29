# coding:utf-8
# python单链表

class Node(object):
    """
    节点 （实际上可以用元组，为了通用性，链表元素也需要创建）
    """
    def __init__(self,elem):
        self.elem = elem
        self.next = None

# 定义链表
class SinglinkList(object):
    """   单链表节点    """
    # 默认值的设置错误导致！！！
    def __init__(self,node =None): # 对外不暴露 私有属性 可以引入node也可以是空列表
        self.__head = node


    def is_empty(self):
        """判断是否为空"""
        return self.__head == None


    def lenth(self): #链表长度不需要参数 指针/游标   假设起始位置为cur
        # cur 游标 用来移动遍历节点
        cur = self.__head
        # count 用来记录数量
        count = 0 # 能处理空链表时候的特殊情况
        while cur != None: # cur不用curnext 是因为 指针到最后，不进入循环体，输出正确数量
            count += 1
            cur = cur.next # 指针后移
        return count


    def travel(self):
        """遍历"""
        cur = self.__head
        while cur != None:
            print(cur.elem,end=" ")
            cur = cur.next
        print(" ")


    def add(self,item):
        """链表头部添加"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def addend(self,item): # 游标走到最后的位置后，在尾部追加
        """尾部追加"""

        node = Node(item)
        if self.is_empty():  # 判断空
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node


    def insert(self,pos,item):
        """
        插入某个元素
        :param pos 从0开始，
        """
        if pos <= 0:
            self.add(item)
        elif pos > (self.lenth()-1):
            self.addend(item)
        else:
            pre = self.__head
            count = 0
            while count < pos - 1 :
                count += 1
                pre =pre.next
            # 循环退出后，pre指向pos-1位置
            node = Node(item)   # pre/游标-1的约定做法
            node.next = pre.next
            pre.next = node

        # node.next = self.__head
        # self.__head = node



    def remove(self,item):
        """删除某个元素"""
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                # 判断此节点是否是头结点
                if cur == self.__head:
                    self.__head = cur.next
                # 如果是头结点
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next





    def search(self,item):
        """判断是否存在"""
        cur = self.__head
        while cur != None:
           if  cur.elem == item:
               return True
           else:
               cur = cur.next
        return False







if __name__ == "__main__":
    l1 = SinglinkList()
    print(l1.is_empty())
    print(l1.lenth())
    l1.addend(1)
    print(l1.is_empty())
    print(l1.lenth())

    l1.addend(2)
    l1.addend(3)
    l1.add(8)
    l1.addend(4)
    l1.addend(5)
    l1.addend(6)
    # 8 1 2 3 4 5 6
    l1.insert(-1,9)
    # 9 8 1 2 3 4 5 6
    l1.travel()
    l1.insert(2, 100)
    l1.travel()
    l1.insert(100,200)
    l1.travel()
    l1.remove(200)
    l1.travel()
    l1.remove(9)
    l1.travel()


