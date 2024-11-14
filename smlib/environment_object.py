from dataclasses import dataclass, field
from group_object import Group

@dataclass
class Environment:
    """
    A class representing a Qtile environment.

    Attributes:
        groups (list[Group]): The list of Groups the environment has.
        name (str): The environment name.
        label (str): The environment label.
        default (bool): If is the default environment to load.
    """
    groups: list[Group] = field(default_factory=list)
    name: str = f"Default"
    label: str = r"\udb80\udce5"
    default: bool = False
    
    def __dict__(self):
        return {
            "groups":[group.__dict__() for group in self.groups],
            "name":self.name,
            "label":self.label,
        }

    def __del__(self):
        for group in self.groups:
            del group