from dataclasses import dataclass, field
from typing import Any, List, Optional, Tuple


@dataclass
class DictManager:
    """
    A simple dictionary management class that provides basic dictionary operations.

    Attributes:
        data (dict): The dictionary that stores the data.
    """
    data: dict[Any, Any] = field(default_factory=dict)

    def __repr__(self) -> str:
        """Return the dictionary representation of the DictManager object."""
        return repr(self.data)

    def __getitem__(self, key: str) -> Any:
        """Get the value associated with the key from the dictionary."""
        try:
            return self.data[key]
        except KeyError as exc:
            raise KeyError(f"Key '{key}' not found.") from exc

    def __setitem__(self, key: str, value: Any) -> None:
        """Set the value associated with the key in the dictionary."""
        self.data[key] = value

    def __delitem__(self, key: str) -> None:
        """Delete the value associated with the key from the dictionary."""
        try:
            del self.data[key]
        except KeyError as exc:
            raise KeyError(f"Key '{key}' not found.") from exc

    def __contains__(self, key: Any) -> bool:
        """Check if a key exists in the dictionary."""
        return key in self.data

    def __len__(self) -> int:
        """Get the number of items in the dictionary."""
        return len(self.data)

    def __hash__(self):
        """Generate a hash for the DictManager instance."""
        return hash(tuple(sorted(self.data.items())))

    def __iter__(self):
        """Make the DictManager instance iterable over its data."""
        return iter(self.data.items())

    def add(self, key: str, value: Any) -> None:
        """Add an item to the dictionary."""
        self.data[key] = value

    def remove(self, key: Any) -> None:
        """Remove an item from the dictionary."""
        self.data.pop(key, None)

    def get(self, key: Optional[str] = None) -> Any:
        """
        Get the value of an item by key or return the entire dictionary.

        Args:
            key (Optional[str]): The key to look up in the dictionary.

        Returns:
            Any: The value associated with the key, or the entire dictionary if no key is provided.
        """
        if key is not None:
            try:
                return self.data[key]
            except KeyError as exc:
                raise KeyError(f"Key '{key}' not found.") from exc
        return self.data

    def keys(self) -> List[Any]:
        """Get a list of all keys in the dictionary."""
        return list(self.data.keys())

    def values(self) -> List[Any]:
        """Get a list of all values in the dictionary."""
        return list(self.data.values())

    def items(self) -> List[Tuple[Any, Any]]:
        """Get a list of all key-value pairs in the dictionary."""
        return list(self.data.items())

    def clear(self) -> None:
        """Clear the dictionary."""
        self.data.clear()


@dataclass
class HeaderManager(DictManager):
    """
    A specialized dictionary manager for handling HTTP headers.
    """

    def __init__(self):
        super().__init__()


@dataclass
class ParamManager(DictManager):
    """
    A specialized dictionary manager for handling URL parameters.
    """

    def __init__(self):
        super().__init__()
