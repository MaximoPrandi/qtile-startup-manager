from dataclasses import dataclass, field
from group_object import Group

@dataclass
class Environment:
    """
    A class representing a Qtile environment.

    Attributes:
        Manager (Manager)
        groups (list[Group]): The list of Groups the environment has.
        name (str): The environment name.
        label (str): The environment label.
        default (bool): If is the default environment to load.
    """
    _groups: list[Group] = field(default_factory=list)
    _name: str = f"Default"
    _label: str = r"\udb80\udce5"
    _default: bool = False

    def __del__(self):
        for group in self._groups:
            del group
    
    @property
    def groups(self) -> list[Group]:
        """
        Return the groups the environment has.

        Returns:
            List[Group]: A groups list.
        """
        return self._groups

    @property
    def name(self) -> str:
        """
        Return the environment name

        Returns:
            str: The environment name
        """
        return self._name

    @property
    def label(self) -> str:
        """
        Return the environment label

        Returns:
            str : The environment label
        """
        return self._label
    
    @property
    def default(self) -> bool:
        """
        Return if the environment is the default one to load on startup

        Returns:
            bool : The environment default boolean
        """
        return self._default

    @name.setter
    def name(self, name: str):
        self._name = name
            
    @label.setter
    def label(self, label: str):
        self._label = label
            
    @groups.setter
    def groups(self, groups: list[Group]):
        if any(group in self._apps for group in groups):
            raise ValueError("There's already at least one of the declared groups in the environment")
        self._groups = self._groups + groups
            
    @default.setter
    def default(self, default: bool):
        self._default = default
        
    @name.deleter
    def name(self):
        self._name = "Default"

    @label.deleter
    def label(self):
        self._label = r"\udb80\udce5"
            
    @groups.deleter
    def groups(self):
        self._groups = []
            
    @default.deleter
    def default(self):
        self._default = False