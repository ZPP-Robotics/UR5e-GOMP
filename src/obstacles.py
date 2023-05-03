from math import inf

class Obstacle:
    def __init__(self, ref_point: tuple[float, float, float]):
        self.ref_point = ref_point
    
    def convert(self):
        pass

class HorizontalLine:
    def __init__(self, point3d: tuple[float, float, float], vector3d: tuple[float, float, float], from_top: bool):
        self.point3d = point3d
        self.vector3d = vector3d
        self.from_top = from_top

    def convert(self):
        # return (self.point3d, self.vector3d, self.from_top)
        return (self.vector3d, self.point3d, self.from_top)

class BoxParallelXYZ(Obstacle):
    def __init__(self, ref_point: tuple[float, float, float], height: float, width: float, depth: float):
        super().__init__(ref_point)
        self.depth = depth

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

        lineAB = HorizontalLine(self.vertexA, vectorAB, False)
        lineBC = HorizontalLine(self.vertexB, vectorBC, False)
        lineDC = HorizontalLine(self.vertexD, vectorAB, False)
        lineAD = HorizontalLine(self.vertexA, vectorBC, False)

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

        minz = self.vertexA[2] - self.depth

        return (result, (-inf, -inf, minz), (inf, inf, inf))
    
class TwoBoxSetup(Obstacle):
    def __init__(self, ref_point1: tuple[float, float, float], height1: float, width1: float, depth1: float,
                 ref_point2: tuple[float, float, float], height2: float, width2: float, depth2: float):
        self.box1 = BoxParallelXYZ(ref_point1, height1, width1, depth1)
        self.box2 = BoxParallelXYZ(ref_point2, height2, width2, depth2)

    def convert(self):
        (vertexA1, vertexB1, vertexC1, vertexD1) = self.box1.get_vertices()
        (vertexA2, vertexB2, vertexC2, vertexD2) = self.box2.get_vertices()
        
        vectorBC = tuple(vertexC1[i] - vertexB1[i] for i in range(3))
        lineBC = HorizontalLine(vertexB1, vectorBC, False)

        minx = vertexA1[0]
        maxx = vertexC2[0]

        miny = vertexC2[1]
        maxy = vertexA1[1]

        minz = min(vertexA1[2] - self.box1.depth, vertexA2[2] - self.box2.depth)

        return ([lineBC.convert()], (minx, miny, minz), (maxx, maxy, inf))

class CameraBox(Obstacle):
    def __init__(self, ref_point: tuple[float, float, float], height: float):
        super().__init__(ref_point)
        self.height = height

    def convert(self):

        return ([], (-inf, -inf, -inf), (inf, inf, self.height))
    
class Camera(Obstacle):
    def __init__(self, ref_point: tuple[float, float, float], height: float, width: float):
        super().__init__(ref_point)
        self.height = height

                #       (width)
        # D ------K-------- C                   ^ x
        # |       |         |                   |
        # |       |         | (height)          |
        # |       |         |           y <------------
        # |       |         |                   |
        # |       L         |
        # A - ref_point --- B
        #  (x, y, z)

        x, y, z = ref_point[0], ref_point[1], ref_point[2]

        self.A = ref_point
        self.B = (x, y - width, z)
        self.C = (x + height, y - width, z)
        self.D = (x + height, y, z)
        self.K = (x + height, y - width / 2, z)
        self.L = (x, y - width / 2, z )

    def get_points(self):
        return (self.A, self.B, self.C, self.D, self.K, self.L)
    
    def to_HorizontalLines(self):
        vectorAD = tuple(self.D[i] - self.A[i] for i in range(3))
        vectorBC = tuple(self.C[i] - self.B[i] for i in range(3))
        vectorLK = tuple(self.K[i] - self.L[i] for i in range(3))

        lineAD = HorizontalLine(self.vertexA, vectorAD, False)
        lineBC = HorizontalLine(self.vertexB, vectorBC, False)
        lineLK = HorizontalLine(self.vertexD, vectorLK, False)

        lines = []
        lines.append(lineAD)
        lines.append(lineBC)
        lines.append(lineLK)

        return lines

    def convert(self):
        lines = self.to_HorizontalLines()
        result = []
        for line in lines:
            result.append(line.convert())

        return (result, (-inf, -inf, -int), (inf, inf, inf))
    