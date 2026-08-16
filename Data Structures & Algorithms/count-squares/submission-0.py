class CountSquares:

    def __init__(self):
        self.ptsc = defaultdict(int)
        self.pl = []
    def add(self, point: List[int]) -> None:
        self.ptsc[tuple(point)] += 1
        self.pl.append(point)
    def count(self, point: List[int]) -> int:
        f = 0
        px, py = point
        for x, y in self.pl:
            if abs(py - y) != abs(px - x) or x == px or y == py:
                continue
            f += self.ptsc[(x, py)] * self.ptsc[(px, y)]
        return f
        
