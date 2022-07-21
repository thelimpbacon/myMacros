# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Safari web browser for Mac

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name': 'Brave browser',  # Application name
    'macros': [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000020, '< Back', [Keycode.COMMAND, '[']),
        (0x000020, 'Fwd >', [Keycode.COMMAND, ']']),
        (0x000020, 'Up', [Keycode.SHIFT, ' ']),      # Scroll up
        # 2nd row ----------
        (0x3c005a, '< Tab', [Keycode.CONTROL, Keycode.SHIFT, Keycode.TAB]),
        (0x3c005a, 'Tab >', [Keycode.CONTROL, Keycode.TAB]),
        (0x3c005a, 'Down', ' '),                     # Scroll down
        # 3rd row ----------
        (0x000020, 'Reload', [Keycode.COMMAND, 'r']),
        (0x000020, 'Home', [Keycode.COMMAND, 'H']),
        (0x000020, 'Priv', [Keycode.COMMAND, 'N']),
        # 4th row ----------
        (0x3c005a, 'Git', [Keycode.COMMAND, 't', -Keycode.COMMAND,
                           'www.github.com\n']),   # github in new tab
        (0x3c005a, 'Local', [Keycode.COMMAND, 't', -Keycode.COMMAND,
                             'localhost:3000\n']),  # localhost:3000 in new tab
        (0x3c005a, 'FB', [Keycode.COMMAND, 't', -Keycode.COMMAND,
                          'www.fb.com\n']),  # fb
        # Encoder button ---
        (0x000000, '', [Keycode.COMMAND, 'w'])  # Close window/tab
    ]
}
