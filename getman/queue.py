class Queue:
	items = []

	def is_queue_empty(self):
		return not self.items

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		return self.items.pop()

	def size_queue(self):
		return len(self.items)

	def clear_queue(self):
		self.items.clear()

	def get_queues(self):
		return self.items
