from typing import Any, List


class QueueManager:
    """
       A simple queue management class that provides basic queue operations.

       Attributes:
           items (List[Any]): The list that stores the queue items.
   """
    items = []

    def is_queue_empty(self) -> bool:
        """
        Check if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self.items) == 0

    def enqueue(self, item: Any) -> None:
        """
        Add an item to the end of the queue.

        Args:
            item (Any): The item to be added to the queue.
        """
        self.items.insert(0, item)

    def dequeue(self) -> Any:
        """
        Remove and return the item from the front of the queue.

        Returns:
            Any: The item removed from the front of the queue.

        Raises:
            IndexError: If the queue is empty when trying to dequeue.
        """
        if self.is_queue_empty():
            raise IndexError("Cannot dequeue from an empty queue.")
        return self.items.pop()

    def size_queue(self) -> int:
        """
        Get the number of items in the queue.

        Returns:
            int: The number of items in the queue.
        """
        return len(self.items)

    def clear_queue(self) -> None:
        """
        Remove all items from the queue.
        """
        self.items.clear()

    def get_queues(self) -> List[Any]:
        """
        Get a list of all items currently in the queue.

        Returns:
            List[Any]: The list of items in the queue.
        """
        return self.items.copy()
