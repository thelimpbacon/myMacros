# SPDX-FileCopyrightText: 2021 Emma Humphries for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {                # REQUIRED dict, must be named 'app'
    'name': 'terminal',  # Application name
    'macros': [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        # open terminal
        (0x202000, 'open', []),
        # new pane
        (0x202000, 'new pane', [Keycode.COMMAND,'d']),
        # new tab
        (0x202000, 'new tab', [Keycode.COMMAND, 't']),

        # 2nd row ----------
        # git add .
        (0x202000, 'git add', ['git add .', Keycode.ENTER]),
        # git commit
        (0x202000, 'git comm', ['git commit', Keycode.ENTER]),
        # git push
        (0x202000, 'git push', ['git push', Keycode.ENTER]),

        # 3rd row ----------
        # run yarn dev
        (0x202000, 'run', ['yarn dev', Keycode.ENTER]),
        # run yarn build
        (0x202000, 'build', ['yarn build', Keycode.ENTER]),
        # run yarn type-check
        (0x202000, 'type-check', ['yarn type-check', Keycode.ENTER]),

        # 4th row ----------
        # go to left pane
        (0x101010, '<< pane', [Keycode.COMMAND, '[']),  
        # go to right pane
        (0x800000, 'pane >>', [Keycode.COMMAND, ']']),  
        # go to cora directory
        (0x101010, 'Cora', ['cd /Users/vaughn/Documents/upwork_related/Cora', Keycode.ENTER]),
        
        # Encoder button ---
        # run yarn dev
        (0x000000, 'windows', ['yarn dev', Keycode.ENTER])
    ]
}
