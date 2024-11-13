from enum import Enum

class Operations(Enum):
    """
    A enum with the setter functions actual possible operations type
    """
    DECLARATION = 1
    """
    Used in a declaration instance of a setter function procedure, for example initialization or replace
    """
    LIST = 2
    """
    Used in a list declaration instance of a setter function procedure
    """