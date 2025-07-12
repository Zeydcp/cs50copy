def main():
    jar = Jar()
    jar.deposit(11)
    jar.withdraw(2)
    print(str(jar))


class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity is not a non-negative int")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Exceed capacity")
        self._size += n

    def withdraw(self, n):
        if self.size < n:
            raise ValueError(f"Not {n} cookies left")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


main()
