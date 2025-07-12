class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity should be a non-negative int")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return f"🍪" * self.size

    def deposit(self, n):
        self._size += n
        if self.size > self.capacity:
            raise ValueError("Deposited too many cookies")

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Withdrew too many cookies")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
