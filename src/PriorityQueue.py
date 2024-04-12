class Node:
  def __init__(self, value, priority):
    self.value = value
    self.priority = priority
    self.next = None
    self.prev = None

class PriorityQueue:
  def __init__(self):
    self.head = None
    self.tail = None

  def is_empty(self):
    return self.head is None

  def enqueue(self, value, priority):
    new_node = Node(value, priority)

    if self.is_empty():
      self.head = new_node
      self.tail = new_node
    else:
      if priority > self.head.priority:
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
      else:
        current_node = self.head
        while current_node.next is not None and priority <= current_node.next.priority:
          current_node = current_node.next

        if current_node.next is None:
          self.tail.next = new_node
          new_node.prev = self.tail
          self.tail = new_node
        else:
          new_node.next = current_node.next
          current_node.next.prev = new_node
          new_node.prev = current_node
          current_node.next = new_node

  def dequeue(self):
    if self.is_empty():
      return None

    dequeued_node = self.head
    self.head = self.head.next

    if self.head is not None:
      self.head.prev = None
    else:
      self.tail = None

    return dequeued_node.value

