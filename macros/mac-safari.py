# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Safari web browser for Mac

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name': 'Mac Safari',  # Application name
    'macros': [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x004000, '< Back', [Keycode.COMMAND, '[']),
        (0x004000, 'Fwd >', [Keycode.COMMAND, ']']),
        (0x400000, 'Up', [Keycode.SHIFT, ' ']),      # Scroll up
        # 2nd row ----------
        (0x202000, '< Tab', [Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB]),
        (0x202000, 'Tab >', [Keycode.CONTROL, Keycode.TAB]),
        (0x400000, 'Down', ' '),                     # Scroll down
        # 3rd row ----------
        (0x000040, 'Reload', [Keycode.COMMAND, 'r']),
        (0x000040, 'Home', [Keycode.COMMAND, 'H']),
        (0x000040, 'Private', [Keycode.COMMAND, 'N']),
        # 4th row ----------
        (0x000000, 'Github', [Keycode.COMMAND, 'n', -Keycode.COMMAND,
                              'www.github.com\n']),   # github in new window
        (0x800000, 'Local:3000', [Keycode.COMMAND, 'n', -Keycode.COMMAND,
                                  'localhost:3000\n']),   # localhost:3000 in new window
        (0x101010, 'Hacks', [Keycode.COMMAND, 'n', -Keycode.COMMAND,
                             'www.hackaday.com\n']),  # Hack-a-Day in new win
        # Encoder button ---
        (0x000000, '', [Keycode.COMMAND, 'w'])  # Close window/tab
    ]
}
