# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Safari web browser for Mac

from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name': 'Apps',  # Application name
    'macros': [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        # Discord
        (0x202000, 'Disc', [Keycode.SHIFT, Keycode.OPTION, Keycode.CONTROL,
                            Keycode.F1, -Keycode.SHIFT, -Keycode.OPTION, -Keycode.CONTROL]),
        # Messenger
        (0x202000, 'Msgr', [Keycode.SHIFT, Keycode.OPTION, Keycode.CONTROL,
                            Keycode.F2, -Keycode.SHIFT, -Keycode.OPTION, -Keycode.CONTROL]),
        # Docker
        (0x202000, 'Dock', [Keycode.SHIFT, Keycode.OPTION, Keycode.CONTROL,
                            Keycode.F3, -Keycode.SHIFT, -Keycode.OPTION, -Keycode.CONTROL]),
        # 2nd row ----------
        # Facetime
        (0x202000, 'Face', [Keycode.SHIFT, Keycode.OPTION, Keycode.CONTROL,
                            Keycode.F4, -Keycode.SHIFT, -Keycode.OPTION, -Keycode.CONTROL]),
        # Brave
        (0x202000, 'Brave', [Keycode.SHIFT, Keycode.OPTION, Keycode.CONTROL,
                             Keycode.F5, -Keycode.SHIFT, -Keycode.OPTION, -Keycode.CONTROL]),
        # Figma
        (0x202000, 'Fig', [Keycode.SHIFT, Keycode.OPTION, Keycode.CONTROL,
                           Keycode.F6, -Keycode.SHIFT, -Keycode.OPTION, -Keycode.CONTROL]),
        # 3rd row ----------
        # Messages
        (0x000020, 'Mess', [Keycode.SHIFT, Keycode.OPTION, Keycode.CONTROL,
                            Keycode.F7, -Keycode.SHIFT, -Keycode.OPTION, -Keycode.CONTROL]),
        # Spotify
        (0x000020, 'Spot', [Keycode.SHIFT, Keycode.OPTION, Keycode.CONTROL,
                            Keycode.F8, -Keycode.SHIFT, -Keycode.OPTION, -Keycode.CONTROL]),
        (0x000020, 'H', [Keycode.COMMAND, 'h']),
        # 4th row ----------
        (0x3c005a, '<-', [Keycode.COMMAND, Keycode.OPTION, Keycode.CONTROL,
                          Keycode.LEFT_ARROW, -Keycode.COMMAND, -Keycode.OPTION, -Keycode.CONTROL]),
        (0x3c005a, '->', [Keycode.COMMAND, Keycode.OPTION, Keycode.CONTROL,
                          Keycode.RIGHT_ARROW, -Keycode.COMMAND, -Keycode.OPTION, -Keycode.CONTROL]),
        (0x3c005a, 'X', [Keycode.COMMAND, 'w']),
        # Encoder button ---
        (0x000000, '', [Keycode.COMMAND, 'w'])  # Close window/tab
    ]
}
