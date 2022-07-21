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
        # type index.ts
        (0x000020, 'index', ['index.ts']),
        # run yarn dev
        (0x000020, 'run', ['yarn dev', Keycode.ENTER]),
        # run yarn type-check
        (0x000020, 'tsc', ['yarn type-check', Keycode.ENTER]),

        # 2nd row ----------
        # git add .
        (0x000020, 'add', ['git add .', Keycode.ENTER]),
        # git commit
        (0x000020, 'commit', ['git commit', Keycode.ENTER]),
        # git push
        (0x000020, 'push', ['git push', Keycode.ENTER]),

        # 3rd row ----------
        # select all occuring words command + shift + l
        (0x000020, 'all', [Keycode.COMMAND, Keycode.SHIFT, 'l']),
        # move window to the left pane: ctrl: command + left arrow
        (0x000020, '<<<', [Keycode.CONTROL, Keycode.COMMAND,
         Keycode.LEFT_ARROW, -Keycode.COMMAND, -Keycode.CONTROL]),
        # move window to the right pane: ctrl: command + right arrow
        (0x000020, '>>>', [Keycode.CONTROL, Keycode.COMMAND,
         Keycode.RIGHT_ARROW, -Keycode.COMMAND, -Keycode.CONTROL]),

        # 4th row ----------
        # split: command + \
        (0x000020, 'split', [Keycode.COMMAND, '\\']),
        # Go to matching bracket: command + shift + \
        (0x000020, 'bracket', [Keycode.COMMAND, Keycode.SHIFT, '\\']),
        (0x000020, '#', [Keycode.COMMAND, Keycode.SHIFT, '']),

        # Encoder button ---
        # toggle windows
        (0x000020, 'windows', [Keycode.COMMAND, '`'])
    ]
}
