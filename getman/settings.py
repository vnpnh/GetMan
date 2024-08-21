from dataclasses import dataclass, field
from typing import Optional, Literal, Dict, Any


@dataclass
class Settings:
	"""
	Class representing settings for a certain operation.
	"""
	timeout: int = 20  # Timeout duration in seconds (default: 20)
	retries: int = 1  # Number of retries in case of failure (default: 1)
	delay: int = 1  # Delay duration in seconds between retries (default: 1)
	timeout_increment: int = 10  # Increase in timeout duration in case of timeout (default: 10)
	style: Optional[Dict[str, str]] = field(
		default_factory=lambda: {"success": "green", "failed": "bold red", "info": "yellow bold"})
	color_system: Optional[Literal["auto", "standard", "256", "truecolor", "windows"] | None] = "windows"
