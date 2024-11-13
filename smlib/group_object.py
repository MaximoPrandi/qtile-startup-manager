from dataclasses import dataclass, field
from os import system, path
from app_object import App

@dataclass
class Group:
    """
    A class representing a Qtile group.

    Attributes:
        applications (list[App]): The list of applications or the sole app that the group has.
        name (str): The group name.
        label (str): The group label.
        exclusive (bool): If the group applications are exclusive.
        exclusive (bool): If the group applications spawn on startup.
    """
    applications: list[App] = field(default_factory=list)
    name: str
    label: str = "\ueea8"
    exclusive: bool = False
    spawn: bool = True

    def __del__(self):
        for application in self._applications:
            del(application.groups, [self])
    
    def __dict__(self) -> dict:
        """
        Return the group info ready to be used by Qtile

        Returns:
            dict: A dictionary with all the group information.
        """
        _info = {
            "name":self,
            "label":self.label,
            "matches":map(App.match,self.applications),
            "exclusive":self.exclusive,
            "spawn":map(App.spawn,self.applications)
        }

    @property
    def applications(self) -> list[App]:
        """
        Return a list of the group applications

        Returns:
            list[App]: A list of the group applications.
        """
        return self._applications

    @property
    def name(self) -> str:
        """
        Return the group name

        Returns:
            str : The group name
        """
        return self._name
    
    @property
    def label(self) -> str:
        """
        Return the group label, the UTF16 code of an icon, used for example in GroupBox()

        Returns:
            str : The group label
        """
        return self._label

    @property
    def exclusive(self) -> bool:
        """
        Return if the app or applications are of exclusive use in the group

        Returns:
            bool : Exclusive boolean
        """
        return self._exclusive
    
    @property
    def spawn(self) -> bool:
        """
        Return if the app or applications are spawned on startup

        Returns:
            str : Spawn boolean
        """
        return self._spawn
    
    @applications.setter
    def applications(self, applications: list[App], replace: bool = False):
        if any(app in self._applications for app in applications):
            raise ValueError("There's already at least one of the list app\'s in the group")
        self._applications = self._applications + applications
    
    @name.setter
    def name(self, name: str):
            self._name = name
            
    @label.setter
    def label(self, label: str):
        self._label = label
            
    @exclusive.setter
    def exclusive(self, exclusive: bool):
        self._exclusive = exclusive
            
    @spawn.setter
    def spawn(self, spawn: bool):
        self._spawn = spawn
        
    @applications.deleter
    def applications(self, applications: list[App]):
        self._applications = filter(lambda x: (x not in applications) ,self._applications)

    @name.deleter
    def name(self):
        self._name = f"Default {self.environment.free_group_number()}"
            
    @label.deleter
    def label(self):
        self._label = "\ueea8"
            
    @exclusive.deleter
    def exclusive(self):
        self._exclusive = False
            
    @spawn.deleter
    def spawn(self):
        self._spawn = False