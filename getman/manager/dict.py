from dataclasses import dataclass, field
from functools import lru_cache
from typing import Any, Optional, List, Tuple


@dataclass
class DictManager:
	data: dict[Any, Any] = field(default_factory=dict)

	def __repr__(self) -> str:
		"""Return the dictionary representation of the DictManager object."""
		return repr(self.data)

	@lru_cache(maxsize=None)
	def __getitem__(self, key: str) -> dict:
		"""Get the value associated with the key from the cache."""
		try:
			return dict(self.data[key])
		except KeyError:
			raise KeyError(f"Key '{key}' not found.")

	def __setitem__(self, key: str, value: Any) -> None:
		"""Set the value associated with the key in the cache."""
		self.data[key] = value

	def __delitem__(self, key: str) -> None:
		"""Delete the value associated with the key from the cache."""
		try:
			del self.data[key]
		except KeyError:
			raise KeyError(f"Key '{key}' not found.")

	def __contains__(self, key: Any) -> bool:
		"""Check if a key exists in the cache."""
		return key in self.data

	def __len__(self) -> int:
		"""Get the number of items in the cache."""
		return len(self.data)

	def __hash__(self):
		return hash(tuple(sorted(self.data.items())))

	def __iter__(self):
		"""Make the DictManager instance iterable over its data."""
		return iter(self.data.items())

	def add(self, key: str, value: Any) -> None:
		"""Add an item to the cache."""
		self.data[key] = value

	def remove(self, key: Any) -> None:
		"""Remove an item from the cache."""
		self.data.pop(key, None)

	@lru_cache(maxsize=None)
	def get(self, key: Optional[str] = None) -> Any:
		"""Get the value of an item by key or return the entire cache."""
		if key is not None:
			try:
				return self.data[key]
			except KeyError:
				raise KeyError(f"Key '{key}' not found.")
		return self.data

	def keys(self) -> List[Any]:
		"""Get a list of all keys in the cache."""
		return list(self.data.keys())

	def values(self) -> List[Any]:
		"""Get a list of all values in the cache."""
		return list(self.data.values())

	def items(self) -> List[Tuple[Any, Any]]:
		"""Get a list of all key-value pairs in the cache."""
		return list(self.data.items())

	def clear(self) -> None:
		"""Clear the cache."""
		self.data.clear()


class HeaderManager(DictManager):
	def __init__(self):
		# Invoke parent class's __init__ method
		super().__init__()


class ParamManager(DictManager):
	def __init__(self):
		# Invoke parent class's __init__ method
		super().__init__()
