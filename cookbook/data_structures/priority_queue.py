import heapq


class PriorityQueue:
    """
    This thing really just calls the heapq function on a thing to get the thing
    with the highest priority.

    We are always getting the one with the highest priority, but we could do the
    second most, third most, etc.

    What we do here is save the priority, the index, and the item itself. When
    comparing tuples, python compares the first values first before the next
    values, and stops once it can determine it. This works the same with lists.
    """

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Item ({!r})".format(self.name)


q = PriorityQueue()
q.push(Item("foo"), 1)
q.push(Item("bar"), 5)
q.push(Item("sna"), 4)
q.push(Item("fu"), 1)
