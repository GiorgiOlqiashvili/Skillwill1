class FIFOQueue:
    def __init__(self):
        self.queue = []
        self.max_size = 15

    def inqueue(self, num):
        if 1 <= num <= 10:
            return "Number must be outside the range 1 to 10"
        if len(self.queue) >= self.max_size:
            return "Queue is full"
        self.queue.append(num)
        return f"inqueued: {num}"

    def dequeue(self):
        if not self.queue:
            return "Queue is empty"
        return self.queue.pop(0)

    def __str__(self):
        return f"Queue: {self.queue}"


# Example usage
fifo = FIFOQueue()
print(fifo.inqueue(7))
print(fifo.inqueue(20))
print(fifo.inqueue(23))
print(fifo.dequeue())
print(fifo)
