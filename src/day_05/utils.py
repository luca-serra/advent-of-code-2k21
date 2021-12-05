from typing import List, Tuple


def get_coordinates_between(
    x: int, y: int, a: int, b: int, simplified: bool = True
) -> List[Tuple[int, int]]:
    if x == a:
        return [(x, min(y, b) + t) for t in range(max(y, b) - min(y, b) + 1)]
    if y == b:
        return [(min(x, a) + t, y) for t in range(max(x, a) - min(x, a) + 1)]
    if simplified:
        return
    alpha = -1 + 2 * (x < a)
    betha = -1 + 2 * (y < b)
    return [(x + alpha * t, y + betha * t) for t in range(max(x, a) - min(x, a) + 1)]
