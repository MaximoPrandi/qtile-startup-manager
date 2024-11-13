# The routes where applications '.desktop' will be searched for
APP_ROUTES = [
    "/usr/share/applications/",
    "/usr/local/share/applications/",
    "/var/lib/snapd/desktop/applications",
    "/var/lib/flatpak/exports/share/applications"
]

# The built-in fonts
FONTS = [
    "Nerd Font",
]

# Decides if a prompt to decide the environment on startup
#
# Default: True
PROMPT_ON_STARTUP = True

# Decides the default environment to initialize
#
# Default: 0 (first environment)
DEFAULT_ENVIRONMENT = 0

# Decides between manual configuration or in-app configuration
# 
# Default: False
MANUAL_SETUP = True

# Environments initialization data
ENVIRONMENTS = [
    ""
]

# Groups initialization data
GROUPS = [
    ""
]

# Apps initialization data
APPS = [
    ""
]
