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

MANUAL_DATA = [
    # First list entities are Environment-instance data
    {
        "groups":[
            {
                "applications":[
                    "/usr/share/applications/google-chrome.desktop"
                ],
                "name":"Chrome",
                "label":r"\uf268",
                "exclusive":False,
                "spawn":True
            },
            {
                "applications":[
                    "/usr/share/applications/code.desktop"
                ],
                "name":"Code",
                "label":r"\ue70c",
                "exclusive":False,
                "spawn":True
            },
            {
                "applications":[
                    "/usr/share/applications/code.desktop"
                ],
                "name":"Code 2",
                "label":r"\ue70c",
                "exclusive":False,
                "spawn":True
            },
            {
                "applications":[
                    "/usr/share/applications/Alacritty.desktop"
                ],
                "name":"Terminal",
                "label":r"\uf120",
                "exclusive":False,
                "spawn":True
            },
            {
                "applications":[
                    "/usr/share/applications/com.discordapp.Discord.desktop",
                    "/usr/share/applications/slack.desktop"
                ],
                "name":"Social",
                "label":r"\uf198",
                "exclusive":False,
                "spawn":False
            },
            {
                "applications":[
                    "/usr/share/applications/spotify.desktop"
                ],
                "name":"Spotify",
                "label":r"\uf1bc",
                "exclusive":False,
                "spawn":True
            },
            {
                "applications":[
                    "/usr/share/applications/Alacritty.desktop"
                ],
                "name":"Terminal",
                "label":r"\uf120",
                "exclusive":False,
                "spawn":True
            },
            {
                "applications":[
                    "/usr/share/applications/google-chrome.desktop"
                ],
                "name":"Chrome",
                "label":r"\uf268",
                "exclusive":False,
                "spawn":True
            },
            {
                "applications":[
                    "/usr/share/applications/org.gnome.Nautilus.desktop"
                ],
                "name":"Files",
                "label":r"\uea83",
                "exclusive":False,
                "spawn":True
            },
        ],
        "name":"Work",
        "label":r"\udb80\udce5",
    }
]