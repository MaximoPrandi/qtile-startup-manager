from config import APP_ROUTES, FONTS, PROMPT_ON_STARTUP, DEFAULT_ENVIRONMENT
from dataclasses import dataclass, field
from environment_object import Environment

@dataclass
class Manager:
    """
    The startup manager class.

    Attributes:
        environments (list[Environment]): The list of environments the manager has.
    """
    _environments: list[Environment] = field(default_factory=list)