class Obstacle:
    def __init__(self, ref_point: tuple):
        self.ref_point = ref_point
    
    def convert(self):
        pass

class HorizontalLine:
    def __init__(self, point3d: tuple, vector3d: tuple):
        self.point3d = point3d
        self.vector3d = vector3d

    def convert(self):
        return (self.point3d, self.vector3d)

class BoxParallelXYZ(Obstacle):
    def __init__(self, ref_point, height, width, depth):
        super().__init__(ref_point)

        #       (width)
        # D --------------- C                   ^ x
        # |                 |                   |
        # |                 | (height)          |
        # |                 |           y <------------
        # |                 |                   |
        # A - ref_point --- B
        #  (x, y, z)

        x, y, z = ref_point[0], ref_point[1], ref_point[2]

        self.vertexA = ref_point
        self.vertexB = (x, y - width, z)
        self.vertexC = (x + height, y - width, z)
        self.vertexD = (x + height, y, z)

    def get_vertices(self):
        return (self.vertexA, self.vertexB, self.vertexC, self.vertexD)
    
    def to_HorizontalLines(self):
        vectorAB = tuple(self.vertexB[i] - self.vertexA[i] for i in range(3))
        vectorBC = tuple(self.vertexC[i] - self.vertexB[i] for i in range(3))

        lineAB = HorizontalLine(self.vertexA, vectorAB)
        lineBC = HorizontalLine(self.vertexB, vectorBC)
        lineDC = HorizontalLine(self.vertexD, vectorAB)
        lineAD = HorizontalLine(self.vertexA, vectorBC)

        lines = []
        lines.append(lineAB)
        lines.append(lineBC)
        lines.append(lineDC)
        lines.append(lineAD)

        return lines

    def convert(self):
        lines = self.to_HorizontalLines()
        result = []
        for line in lines:
            result.append(line.convert())

        return result

