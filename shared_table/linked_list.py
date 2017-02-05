# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals


class LinkedList(object):
    def __init__(self):
        self.first = None
        self.last = None

    def delete_first(self):
        if self.first and self.first.next:
            self.first = self.first.next
            self.first.prev = None
        else:
            self.first = None

    def delete_last(self):
        if self.last and self.last.prev:
            self.last = self.last.prev
            self.last.next = None
        else:
            self.last = None

    def delete(self, node):
        if node is not self.first and node is not self.last:
            node.prev.next = node.next
            node.next.prev = node.prev
        elif node is self.first:
            self.delete_first()
        else:
            self.delete_last()

    def add_first(self, value):
        first = Node(value)
        if self.first:
            self.first.prev = first
            first.next = self.first
            self.first = first
        else:
            self.first = first
            self.last = first

    def add_last(self, value):
        last = Node(value)
        if self.last:
            self.last.next = last
            last.prev = self.last
            self.last = last
        else:
            self.last = last
            self.first = last


class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None
