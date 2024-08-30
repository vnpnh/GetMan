from dataclasses import dataclass

from getman.manager.browser.firefox import Firefox


@dataclass
class BrowserManager:
    """
    BrowserManager class for managing browser instances.
    """
    firefox = Firefox()
