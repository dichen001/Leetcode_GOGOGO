'''
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Notes:
You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
Update (2015-06-11):
The class name of the Java function had been updated to MyStack instead of Stack.
'''

class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = collections.deque()


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        q = self.queue
        q.append(x)
        for i in range( len(q) - 1 ):
            q.append(q.popleft())


    def pop(self):
        """
        :rtype: nothing
        """
        return self.queue.popleft()


    def top(self):
        """
        :rtype: int
        """
        return self.queue[0]


    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0
