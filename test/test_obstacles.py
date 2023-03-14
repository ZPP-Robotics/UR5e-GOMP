from obstacles import Obstacle, BoxParallelXYZ, HorizontalLine
import random
import pytest

@pytest.mark.parametrize("box, expected_result", [
    #         w
    # D --------------- C                   ^ x
    # |                 |  h                |
    # |                 |              y <------
    # A --------------- B

    (BoxParallelXYZ((0, 10, 10), 20, 20, 10), 
     ((0, 10, 10), (0, -10, 10), (20, -10, 10), (20, 10, 10))),
    (BoxParallelXYZ((7, 6, 5), 8, 20, 20), 
     ((7, 6, 5), (7, -14, 5), (15, -14, 5), (15, 6, 5))),
])
def test_BoxParallelXYZ_vertices_calculation_simple(box, expected_result):
    (A, B, C, D) = box.get_vertices()
    assert (A, B, C, D) == expected_result 

    assert A[0] == B[0]
    assert A[1] == D[1]
    assert B[1] == C[1]
    assert C[0] == D[0]

    assert A[2] == B[2]
    assert B[2] == C[2]
    assert C[2] == D[2]

def test_BoxParallelXYZ_vertices_calculation_random():
    ref_point = (random.randint(-200,200), random.randint(-200,200), random.randint(-200,200))
    height = random.randint(0, 500)
    width = random.randint(0, 500)
    depth = random.randint(0, 500)
    box = BoxParallelXYZ(ref_point=ref_point, height=height, width=width, depth=depth)

    (A, B, C, D) = box.get_vertices()

    assert A[0] == B[0]
    assert A[1] == D[1]
    assert B[1] == C[1]
    assert C[0] == D[0]

    assert A[2] == B[2]
    assert B[2] == C[2]
    assert C[2] == D[2]

def test_BoxParallelXYZ_to_HorizontalLine_calculation():
    pass
