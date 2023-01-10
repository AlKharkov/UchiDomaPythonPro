class Polygon:
    def set_vertices_count(self, count):
        self.count = count

    def set_coordinates(self, coords):
        self.coords = coords
        self.coords.append(self.coords[0])

    def get_side_length(self, n):
        a, b = self.coords[n - 1], self.coords[n]
        return round(((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5)


n = int(input())
coords = [tuple(map(lambda x: (int(x[0]), int(x[1])), input().split()))]

pl = Polygon()
pl.set_vertices_count(n)
pl.set_coordinates(coords)

a = int(input())
print(pl.get_side_length(a))
