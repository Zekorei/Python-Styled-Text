"""
file for all colour constants
"""

from src.project_files.style import style


def hex_to_rgb(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")

    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def rgb(r: int, g: int, b: int) -> style:
    return style(f"\033[38;2;{r};{g};{b}m")
