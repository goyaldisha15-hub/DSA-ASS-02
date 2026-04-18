# ldst_toolkit.py
# Name:Disha Goyal  Roll No: 2501730433
# Data Structures - Unit 2 Assignment

# =============================================
# TASK 1 - Dynamic Array
# =============================================

class DynamicArray:
    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.data = [None, None]   # start with 2 slots

    def append(self, x):
        # if full, double the size
        if self.size == self.capacity:
            self.capacity = self.capacity * 2
            new_data = [None] * self.capacity
            for i in range(self.size):
                new_data[i] = self.data[i]
            self.data = new_data
            print("  >> Array was full! Resized to capacity:", self.capacity)

        self.data[self.size] = x
        self.size = self.size + 1

    def pop(self):
        if self.size == 0:
            print("  >> Array is empty, cannot pop!")
            return None
        val = self.data[self.size - 1]
        self.data[self.size - 1] = None
        self.size = self.size - 1
        return val

    def print_array(self):
        elements = []
        for i in range(self.size):
            elements.append(str(self.data[i]))
        print("  Array =", "[" + ", ".join(elements) + "]",
              " | size =", self.size, "| capacity =", self.capacity)


# =============================================
# TASK 2A - Singly Linked List
# =============================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node

    def delete_by_value(self, x):
        if self.head is None:
            print("  >> List is empty!")
            return
        # if head itself is the value
        if self.head.data == x:
            self.head = self.head.next
            return
        curr = self.head
        while curr.next is not None:
            if curr.next.data == x:
                curr.next = curr.next.next
                return
            curr = curr.next
        print("  >> Value", x, "not found in list!")

    def traverse(self):
        items = []
        curr = self.head
        while curr is not None:
            items.append(str(curr.data))
            curr = curr.next
        print("  SLL:", " -> ".join(items), "-> None")


# =============================================
# TASK 2B - Doubly Linked List
# =============================================

class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, x):
        new_node = DNode(x)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def insert_after_node(self, target, x):
        curr = self.head
        while curr is not None:
            if curr.data == target:
                new_node = DNode(x)
                new_node.next = curr.next
                new_node.prev = curr
                if curr.next is not None:
                    curr.next.prev = new_node
                else:
                    self.tail = new_node
                curr.next = new_node
                return
            curr = curr.next
        print("  >> Target", target, "not found!")

    def delete_at_position(self, pos):
        # 0-based
        if self.head is None:
            print("  >> List is empty!")
            return
        curr = self.head
        index = 0
        while curr is not None:
            if index == pos:
                if curr.prev is not None:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next
                if curr.next is not None:
                    curr.next.prev = curr.prev
                else:
                    self.tail = curr.prev
                return
            curr = curr.next
            index = index + 1
        print("  >> Position", pos, "does not exist!")

    def traverse(self):
        items = []
        curr = self.head
        while curr is not None:
            items.append(str(curr.data))
            curr = curr.next
        print("  DLL:", " <-> ".join(items), "<-> None")


# =============================================
# TASK 3A - Stack using Singly Linked List
# =============================================

class Stack:
    def __init__(self):
        self.top = None   # just use Node directly

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("  >> Stack is empty! Underflow.")
            return None
        val = self.top.data
        self.top = self.top.next
        return val

    def peek(self):
        if self.top is None:
            print("  >> Stack is empty!")
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None


# =============================================
# TASK 3B - Queue using Singly Linked List
# =============================================

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, x):
        new_node = Node(x)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            print("  >> Queue is empty! Underflow.")
            return None
        val = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return val

    def front(self):
        if self.head is None:
            print("  >> Queue is empty!")
            return None
        return self.head.data

    def is_empty(self):
        return self.head is None


# =============================================
# TASK 4 - Balanced Parentheses Checker
# =============================================

def is_balanced(expr):
    s = Stack()
    for ch in expr:
        if ch == '(' or ch == '{' or ch == '[':
            s.push(ch)
        elif ch == ')' or ch == '}' or ch == ']':
            if s.is_empty():
                return False
            top = s.pop()
            if ch == ')' and top != '(':
                return False
            if ch == '}' and top != '{':
                return False
            if ch == ']' and top != '[':
                return False
    return s.is_empty()


# =============================================
# MAIN - Run all test cases
# =============================================

print("=" * 50)
print("  LDST - Linear Data Structures Toolkit")
print("=" * 50)

# --- Task 1 ---
print("\n--- TASK 1: Dynamic Array ---")
da = DynamicArray()
print("Appending 1 to 10 (capacity starts at 2):")
for i in range(1, 11):
    da.append(i)
da.print_array()

print("Popping 3 elements:")
print("  Popped:", da.pop())
print("  Popped:", da.pop())
print("  Popped:", da.pop())
da.print_array()

# --- Task 2A ---
print("\n--- TASK 2A: Singly Linked List ---")
sll = SinglyLinkedList()
sll.insert_at_beginning(3)
print("Insert 3 at beginning:")
sll.traverse()

sll.insert_at_end(3)
print("Insert 3 at end:")
sll.traverse()

sll.insert_at_beginning(1)
sll.insert_at_end(7)
print("Insert 1 at beginning, 7 at end:")
sll.traverse()

sll.delete_by_value(3)
print("Delete value 3:")
sll.traverse()

sll.delete_by_value(99)  # not found

# --- Task 2B ---
print("\n--- TASK 2B: Doubly Linked List ---")
dll = DoublyLinkedList()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
print("Initial list (10, 20, 30):")
dll.traverse()

dll.insert_after_node(20, 25)
print("Insert 25 after node 20:")
dll.traverse()

dll.delete_at_position(1)
print("Delete at position 1 (0-based):")
dll.traverse()

dll.delete_at_position(10)  # out of range

# --- Task 3A ---
print("\n--- TASK 3A: Stack ---")
st = Stack()
st.push(10)
st.push(20)
st.push(30)
print("  Pushed 10, 20, 30")
print("  Peek:", st.peek())
print("  Pop:", st.pop())
print("  Pop:", st.pop())
print("  Peek:", st.peek())
st.pop()
st.pop()   # underflow

# --- Task 3B ---
print("\n--- TASK 3B: Queue ---")
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print("  Enqueued 1, 2, 3")
print("  Front:", q.front())
print("  Dequeue:", q.dequeue())
print("  Dequeue:", q.dequeue())
print("  Front:", q.front())
q.dequeue()
q.dequeue()   # underflow

# --- Task 4 ---
print("\n--- TASK 4: Balanced Parentheses Checker ---")
print('  "([{}])" ->', "Balanced" if is_balanced("([{}])") else "Not Balanced")
print('  "([)]"   ->', "Balanced" if is_balanced("([)]")   else "Not Balanced")
print('  "((("    ->', "Balanced" if is_balanced("(((")    else "Not Balanced")
print('  ""       ->', "Balanced" if is_balanced("")       else "Not Balanced")

print("\n" + "=" * 50)
print("  All test cases done!")
print("=" * 50)