# SPDX-FileCopyrightText: 2021 Emma Humphries for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {                # REQUIRED dict, must be named 'app'
    'name': 'VS code react',  # Application name
    'macros': [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        # run yarn dev
        (0x202000, 'run', ['yarn dev', Keycode.ENTER]),
        # type index.ts
        (0x202000, 'index', ['index.ts']),
        # run yarn type-check
        (0x202000, 'type-check', ['yarn type-check', Keycode.ENTER]),

        # 2nd row ----------
        # git add .
        (0x202000, 'git add', ['git add .', Keycode.ENTER]),
        # git commit
        (0x202000, 'git comm', ['git commit', Keycode.ENTER]),
        # git push
        (0x202000, 'git push', ['git push', Keycode.ENTER]),

        # 3rd row ----------
        # select all occuring words command + shift + l
        (0x202000, 'word all', [Keycode.COMMAND, Keycode.SHIFT, 'l']),
        # move window to the left pane: ctrl: command + left arrow
        (0x202000, '<< pane', [Keycode.COMMAND, Keycode.LEFT_ARROW]),
        # move window to the right pane: ctrl: command + right arrow
        (0x202000, 'pane >>', [Keycode.COMMAND, Keycode.RIGHT_ARROW]),

        # 4th row ----------
        # split: command + \
        (0x101010, 'split', [Keycode.COMMAND, '\\']),  
         # Go to matching bracket: command + shift + \
        (0x800000, 'end bracket', [Keycode.COMMAND, Keycode.SHIFT, '\\']),  
        (0x101010, '#', [Keycode.COMMAND, Keycode.SHIFT, '']),
        
        # Encoder button ---
        # toggle windows
        (0x000000, 'windows', [Keycode.COMMAND, '`'])
    ]
}
