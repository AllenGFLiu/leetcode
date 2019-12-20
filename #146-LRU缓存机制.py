'''
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。

获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。

进阶:

你是否可以在 O(1) 时间复杂度内完成这两种操作？

示例:

LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回  1
cache.put(3, 3);    // 该操作会使得密钥 2 作废
cache.get(2);       // 返回 -1 (未找到)
cache.put(4, 4);    // 该操作会使得密钥 1 作废
cache.get(1);       // 返回 -1 (未找到)
cache.get(3);       // 返回  3
cache.get(4);       // 返回  4
'''

from typing import Optional

# 方法1：使用Python内置的OrderedDict有序字典
from collections import OrderedDict

class LRUCache(OrderedDict):
    def __init__(self, capacity):
        self.capacity = capacity

    def get(self, key):
        if key not in self:
            return -1

        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value

        if len(self) > self.capacity:
            self.popitem(last=False)


# 方法2：方法1中OrderedDict实际上就是使用双向链表加哈希表这种底层数据结构实现的
# 所以，直接使用这两个数据结构实现LRU

class DLinkedList:
    # 定义双向链表的节点结构
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None

class LRUCache:
    # 定义几种private类型的方法
    def _add_node(self, node):
        # always add the new node right after self.head
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

    def _pop_tail(self):
        tail = self.tail.prev
        self._remove_node(tail)
        return tail

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)
    # 定义完成


    def __init__(self, capacity):
        self.size = 0
        self.cache = {}
        self.capacity = capacity
        self.head = DLinkedList()
        self.tail = DLinkedList()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        node = self.cache[key]
        if not node:
            return -1
        self._move_to_head(node)
        return node.value

    def put(self, key, value):
        node = self.cache[key]
        if not node:
            new_node = DLinkedList()
            new_node.key = key
            new_node.value = value
            self._add_node(new_node)
            self.size += 1

            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            self._move_to_head(node)
            node.value = value