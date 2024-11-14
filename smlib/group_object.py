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
    name: str = "Default"
    label: str = "\ueea8"
    exclusive: bool = False
    spawn: bool = True
    
    def qtile_dict(self):
        """
        Return the group info ready to be used by Qtile

        Returns:
            dict: A dictionary with all the group information.
        """
        _info = {
            "name":self,
            "label":self.label,
            "matches":map(App.match, self.applications),
            "exclusive":self.exclusive,
            "spawn":map(App.spawn, self.applications)
        }
    
    def __dict__(self):
        return {
            "applications":[app.__repr__() for app in self.applications],
            "name":self.name,
            "label":self.label,
            "exclusive":self.exclusive,
            "spawn":self.spawn
        }