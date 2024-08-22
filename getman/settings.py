from dataclasses import dataclass, field
from typing import Dict, Literal, Optional


@dataclass
class Settings:
    """
    A class to manage configuration settings for specific operations,
    providing detailed control over operation timing, retry logic, and output formatting.

    Attributes:
        timeout (int): Duration in seconds to wait for an operation before timing out. Default: 20.
        retries (int): Number of allowed retries if an operation fails. Default: 1.
        delay (int): Duration in seconds between retries. Default: 1.
        timeout_increment (int): Increment in timeout duration after each timeout event, useful for
            operations that may need progressively longer wait times. Default: 10.
        style (Dict[str, str]): Styling for different operation statuses,
            mapping status keys to style values.
            Default: {'success': 'green', 'failed': 'bold red', 'info': 'yellow bold'}.
        color_system (Optional[Literal['auto',
            'standard', '256', 'truecolor', 'windows']]): Color system
            used for output formatting. Supports a range
            of color modes or 'None' for no color. Default: 'windows'.
    """
    timeout: int = 20
    retries: int = 1
    delay: int = 1
    timeout_increment: int = 10
    style: Dict[str, str] = field(default_factory=lambda: {
        "success": "green",
        "failed": "bold red",
        "info": "yellow bold"
    })
    color_system: Optional[Literal['auto', 'standard', '256', 'truecolor', 'windows']] = 'windows'
