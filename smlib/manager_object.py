from config import APP_ROUTES, FONTS, PROMPT_ON_STARTUP, DEFAULT_ENVIRONMENT, MANUAL_SETUP, MANUAL_DATA
from dataclasses import dataclass, field
from json import dump, load, dumps
from environment_object import Environment
from group_object import Group
from app_object import App
from copy import deepcopy

@dataclass
class Manager:
    """
    The startup manager class.

    Attributes:
        environments (list[Environment]): The list of environments the manager has.
    """
    environments: list[Environment] = field(default_factory=list)
    
    def load_manager(self, env_list: list):
        for env_data in env_list:
            _Groups = []
            for group_data in env_data["groups"]:
                _Apps = []
                for app_data in group_data["applications"]:
                    _Apps.append(App(app_data))
                group_data["applications"] = _Apps
                _Groups.append(Group(**group_data))
            env_data["groups"] = _Groups
            self.environments.append(Environment(**env_data))
    
    def initialize(self, json: bool = False):
        if json:
            with open("json/data.json") as file:
                self.load_manager(load(file))
        elif MANUAL_SETUP:
            self.load_manager(deepcopy(MANUAL_DATA))
    
    def __iter__(self):
        return [environment.__dict__() for environment in self.environments]