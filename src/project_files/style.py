"""
file for terminal text coloring
"""

from typing import NewType, Final

# style types
style = NewType('style', str)
type styleBundle = list[style]


class Style:
    # text style codes
    BOLD: Final[style] = "\033[1m"
    UNDERLINE: Final[style] = "\033[4m"

    END_C: Final[style] = "\033[39;49m" # reset colour
    END: Final[style] = "\033[0m" # reset all


def set_style(text: str, *styles: style, style_bundle: styleBundle = None) -> str:
    codes = ""

    for code in styles:
        codes += code

    if style_bundle is not None:
        for code in style_bundle:
            codes += code

    return codes + text + Style.END


"""
Displays all 256 8-bit ANSI escape code colours in an 8 by 8 matrix.

[testing use only]
"""
def colour_test8bit() -> None:
    for i in range(256):
        print(f"\033[38;5;{i}m {i: >3} {Style.END}", end="")

        if i % 16 == 15:
            print()

    print(Style.END)

    return None
