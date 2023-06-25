
class Queue:
    """
    Params
    ------
    queue_list: list
        The list to initialize the queue with
    max_size: int
        The maximum size of the queue

    References
    ----------
    https://en.wikipedia.org/wiki/Queue_(abstract_data_type)

    Notes
    -----
    A queue is a data structure that follows the First In First Out (FIFO) principle.
    This means that the first item added to the queue will be the first item removed from the queue.
    A queue can be implemented using a list or a linked list.

    Examples
    --------
    queue = Queue([1, 2, 3, 4, 5], 10)

    a = queue.dequeue()
    print(a)
    """


    def __init__(self, queue_list: list = None, max_size: int = None):
        """
        Params
        ------
        queue_list: list
            The list to initialize the queue with
        max_size: int
            The maximum size of the queue

        Returns
        -------
        None

        Notes
        -----
        If the queue_list is not None, then the queue will be initialized with the list
        If the max_size is not None, then the queue will be initialized with the max_size

        Examples
        --------
        queue = Queue([1, 2, 3, 4, 5], 10)

        a = queue.dequeue()
        print(a)
        """
        self.list = []
        self.max_size = max_size
        if queue_list is not None:
            for item in queue_list:
                self.enqueue(item)

    def enqueue(self, item):
        """
        Params
        ------
        item: any
            The item to add to the queue

        Returns
        -------
        None

        Notes
        -----
        Adds the item to the end of the queue

        Examples
        --------
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        print(queue)
        """
        self.list.append(item)
        if self.max_size is not None:
            if self.size() > self.max_size:
                self.dequeue()

    def dequeue(self):
        """
        Params
        ------
        None

        Returns
        -------
        item: any
            The item that was removed from the queue

        Notes
        -----
        Removes the first item from the queue

        Examples
        --------
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        a = queue.dequeue()
        print(a)
        """
        return self.list.pop(0)

    def size(self) -> int:
        """

        Params
        ------
        None

        Returns
        -------
        size: int
            The size of the queue

        Notes
        -----
        Returns the size of the queue

        Examples
        --------
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        print(queue.size())
        """
        return len(self.list)

    def is_empty(self) -> bool:
        """

        Params
        ------
        None

        Returns
        -------
        is_empty: bool
            True if the queue is empty, False otherwise

        Notes
        -----
        Returns True if the queue is empty, False otherwise

        Examples
        --------
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)

        print(queue.is_empty())
        """
        return self.size() == 0

    def peek(self):
        """
        Params
        ------
        None

        Returns
        -------
        item: any
            The first item in the queue

        Notes
        -----
        Returns the first item in the queue without removing it

        Examples
        --------
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        a = queue.peek()
        print(a)
        """
        return self.list[0]

    def get_list(self):
        """

        Params
        ------
        None

        Returns
        -------
        list: list
            The list of items in the queue

        Notes
        -----
        Returns the list of items in the queue

        Examples
        --------
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        a = queue.get_list()
        print(a)
        """
        return self.list

    def __len__(self):
        """
        Params
        ------
        None

        Returns
        -------
        size: int
            The size of the queue

        Notes
        -----
        Returns the size of the queue

        Examples
        --------
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)

        print(len(queue))
        """
        return self.size()

    def copy(self):
        """
        Params
        ------
        None

        Returns
        -------
        new_queue: Queue
            A copy of the queue

        Notes
        -----
        Returns a copy of the queue

        Examples
        --------
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        new_queue = queue.copy()
        print(new_queue)
        """

        new_queue = Queue()
        for item in self.list:
            new_queue.enqueue(item)
        return new_queue

    def __copy__(self):
        """
        Params
        ------
        None

        Returns
        -------
        new_queue: Queue
            A copy of the queue

        Notes
        -----
        Returns a copy of the queue

        Examples
        --------
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        new_queue = queue.copy()
        print(new_queue)
        """

        return self.copy()

    def __eq__(self, other):
        """
        Params
        ------
        other: Queue
            The other queue to compare to

        Returns
        -------
        is_equal: bool
            True if the queues are equal, False otherwise

        Notes
        -----
        Returns True if the queues are equal, False otherwise

        Examples
        --------
        queue = Queue([1, 2, 3, 4, 5], max_size=10)
        other = Queue([1, 2, 3, 4, 5], max_size=10)

        print(queue == other)
        """

        if self.size() != other.size():
            return False
        for i in range(self.size()):
            if self.list[i] != other.list[i]:
                return False
        return True

    def __ne__(self, other):
        """
        Params
        ------
        other: Queue
            The other queue to compare to

        Returns
        -------
        is_not_equal: bool
            True if the queues are not equal, False otherwise

        Notes
        -----
        Returns True if the queues are not equal, False otherwise

        Examples
        --------
        queue = Queue([1, 2, 3, 4, 5], max_size=10)
        other = Queue([1, 2, 3, 4, 5], max_size=10)

        print(queue != other)
        """
        return not self.__eq__(other)

    def __getitem__(self, index):
        """
        Params
        ------
        index: int
            The index of the item to get

        Returns
        -------
        item: any
            The item at the given index

        Notes
        -----
        Returns the item at the given index

        Examples
        --------
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        print(queue[2])
        """
        return self.list[index]

    def __setitem__(self, index, value):
        """
        Params
        ------
        index: int
            The index of the item to set
        value: any
            The value to set the item to

        Returns
        -------
        None

        Notes
        -----
        Sets the item at the given index to the given value

        Examples
        --------
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        queue[2] = 10
        print(queue)
        """
        self.list[index] = value

    def __delitem__(self, index):
        """
        Params
        ------
        index: int
            The index of the item to delete

        Returns
        -------
        None

        Notes
        -----
        Deletes the item at the given index

        Examples
        --------
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        del queue[2]
        print(queue)
        """
        del self.list[index]

    def __iter__(self):
        """
        Params
        ------
        None

        Returns
        -------
        iter: iter
            An iterator for the queue

        Notes
        -----
        Returns an iterator for the queue

        Examples
        --------
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        for item in queue:
            print(item)
        """
        return iter(self.list)

    def __reversed__(self):
        """
        Params
        ------
        None

        Returns
        -------
        reversed: iter
            An iterator for the queue in reverse order

        Notes
        -----
        Returns an iterator for the queue in reverse order

        Examples
        --------
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        for item in reversed(queue):
            print(item)
        """
        return reversed(self.list)

    def __contains__(self, item):
        """
        Params
        ------
        item: any
            The item to check for

        Returns
        -------
        is_in: bool
            True if the item is in the queue, False otherwise

        Notes
        -----
        Returns True if the item is in the queue, False otherwise

        Examples
        --------
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        print(1 in queue)
        """
        return item in self.list

    def __add__(self, other):
        """
        Params
        ------
        other: Queue
            The other queue to add to this queue

        Returns
        -------
        new_queue: Queue
            A new queue with the items from both queues

        Notes
        -----
        Returns a new queue with the items from both queues

        Examples
        --------
        queue = Queue([1, 2, 3, 4, 5], max_size=10)
        other = Queue([6, 7, 8, 9, 10], max_size=10)

        new_queue = queue + other
        print(new_queue)
        """
        new_queue = Queue()
        for item in self.list:
            new_queue.enqueue(item)
        for item in other.list:
            new_queue.enqueue(item)
        return new_queue

    def __iadd__(self, other):
        """
        Params
        ------
        other: Queue
            The other queue to add to this queue

        Returns
        -------
        self: Queue
            This queue with the items from both queues

        Notes
        -----
        Returns this queue with the items from both queues

        Examples
        --------
        queue = Queue([1, 2, 3, 4, 5], max_size=10)
        other = Queue([6, 7, 8, 9, 10], max_size=10)

        queue += other
        print(queue)
        """
        for item in other.list:
            self.enqueue(item)
        return self

    def __mul__(self, other):
        """
        Params
        ------
        other: int
            The number of times to repeat the queue

        Returns
        -------
        new_queue: Queue
            A new queue with the items from this queue repeated the given number of times

        Notes
        -----
        Returns a new queue with the items from this queue repeated the given number of times

        Examples
        --------
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        new_queue = queue * 3
        print(new_queue)
        """
        new_queue = Queue()
        for i in range(other):
            for item in self.list:
                new_queue.enqueue(item)
        return new_queue

    def __imul__(self, other):
        """
        Params
        ------
        other: int
            The number of times to repeat the queue

        Returns
        -------
        self: Queue
            This queue with the items from this queue repeated the given number of times

        Notes
        -----
        Returns this queue with the items from this queue repeated the given number of times

        Examples
        --------
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        queue *= 3
        print(queue)
        """

        for i in range(other):
            for item in self.list:
                self.enqueue(item)
        return self

    def __str__(self):
        """
        Params
        ------
        None

        Returns
        -------
        string: str
            A string representation of the queue

        Notes
        -----
        Returns a string representation of the queue

        Examples
        --------
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        print(queue)
        """
        string_result = ""
        for item in self.list:
            string_result += str(item) + "\n"
        return string_result