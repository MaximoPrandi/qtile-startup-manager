from xdg.DesktopEntry import DesktopEntry
from dataclasses import dataclass
from os import system, path

@dataclass
class App:
    """
    A class representing an user App.

    Attributes:
        groups (list[Group]): The group or groups where the app belongs.
        name (DesktopEntry): The app DesktopEntry instance.
    """
    _app: DesktopEntry
        
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

    @app.setter
    def app(self, dir: str):
        try:
            if path.isfile(dir):
                system(f"cp {dir} apps/{path.basename(str)}")
                _desktop_entry = DesktopEntry(f"apps/{path.basename(str)}")
                if _desktop_entry.getName:
                    self._app = DesktopEntry(f"apps/{path.basename(str)}")
            else:
                raise ValueError("Invalid application path")
        except Exception:
            raise Exception