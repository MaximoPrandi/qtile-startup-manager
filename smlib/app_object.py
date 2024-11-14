from xdg.DesktopEntry import DesktopEntry
from dataclasses import dataclass
from os import system, path

@dataclass
class App:
    """
    A class representing an user App.

    Attributes:
        app (DesktopEntry): The app DesktopEntry instance.
        path (DesktopEntry): The DesktopEntry file path.
    """
    _app: DesktopEntry
    _path: str
    
    def __init__(self, path: str):
        self.app = path
        self.path = path
    
    def __repr__(self):
        return self.path
    
    def match(self) -> str:
        """
        Return the application match ready to be used by Qtile

        Returns:
            str: String with the match necessary to identify de application.
        """
        return f'Match(wm_class=re.compile(r".*{self.app.getName}"))'
    
    def spawn(self):
        """
        Return the application spawn command ready to be used by Qtile

        Returns:
            str: String with the spawn command necessary to spawn the application.
        """
        return f'spawn("{self.app.getExec}"))'
    
    @property
    def app(self) -> DesktopEntry:
        """
        Return the DesktopEntry instance with the app '.Desktop' information.

        Returns:
            DesktopEntry: A DesktopEntry instance.
        """
        return self._app

    @property
    def path(self) -> str:
        """
        Return the DesktopEntry instance with the app '.Desktop' information.

        Returns:
            DesktopEntry: A DesktopEntry instance.
        """
        return self._path

    @path.setter
    def path(self, dir: str):
        self._path = dir

    @app.setter
    def app(self, dir: str):
        try:
            if path.isfile(f"applications/{path.basename(dir)}"):
                _desktop_entry = DesktopEntry(f"applications/{path.basename(dir)}")
                if _desktop_entry.getName:
                    self._app = DesktopEntry(f"applications/{path.basename(dir)}")
            elif path.isfile(dir):
                system(f"cp {dir} applications/{path.basename(dir)}")
                _desktop_entry = DesktopEntry(f"applications/{path.basename(dir)}")
                if _desktop_entry.getName:
                    self._app = DesktopEntry(f"applications/{path.basename(dir)}")
            else:
                raise ValueError(f"Invalid application path '{dir}'")
        except Exception as error:
            raise Exception