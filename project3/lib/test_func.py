import numpy as np
from sympy import *

points = {
    "p0": (0, 0), 
    "p1": (-41.52, -5.1),
    "p2": (-397.41, -42.50),
    "p3": (17.68, 111.69),
    "p4": (-3.2, 154.98),
    "p5": (89, 201.72), 
    "lf": (-12.72, -63.05)
}
radius = {"lf_r": 105.16/2, "p2_r": 85.56/2}


def line_func(point1: tuple, point2: tuple):
    # ax + b = y
    A = np.array([
        [point1[0], 1],
        [point2[0], 1]
    ])
    
    B = np.array([point1[1], point2[1]]).reshape(2, 1)
    A_inv = np.linalg.inv(A)
    ans = A_inv.dot(B)
    lcoe = (ans[0][0], ans[1][0])
    # a = lcoe[0][0], b = lcoe[1][0]
    return lcoe
    
    
def intersection(p1: tuple, p2: tuple, p3=None, p4=None, lcoe=None):
    # ax - y = -b
    l1 = line_func(p1, p2)
    if p3 != None and p4 != None:
        # l1 = line_func(p1, p2)
        l2 = line_func(p3, p4)
    elif lcoe != None:
        # l1 = line_func(p1, p2)
        l2 = lcoe
    A = np.array([
        [l1[0], -1],
        [l2[0], -1]
    ]) 
    B = np.array([-l1[1], -l2[1]]).reshape(2, 1)
    A_inv = np.linalg.inv(A)
    ans = A_inv.dot(B)
    p_ans = (ans[0][0], ans[1][0])
    # print(p_ans)
    return p_ans


def out_tanglin(p1: tuple, p2: tuple, r1: float, r2: float):
    k, b = symbols("k, b")
    func_c1 = (p1[1] - k*p1[0] - b) + r1*(1+k**2)**0.5
    func_c2 = -(p2[1] - k*p2[0] - b) - r2*(1+k**2)**0.5
    tang = solve([func_c1, func_c2], [k, b])
    # print(tang[0][1])
    p_tang = (float(tang[0][0]), float(tang[0][1]))
    """
    ttt = tang[0][0] * (-396) + tang[0][1]
    print(ttt)
    """
    return p_tang

    
if __name__ == "__main__":
    # line_func(points["p3"], points["p4"])
    IC = intersection(points["p0"], points["p1"], points["p3"], points["p4"])
    #print(IC)
    
    aa = out_tanglin(points["lf"], points["p2"], radius["lf_r"], radius["p2_r"])
    IFC = intersection(points["p2"], IC, lcoe=aa)
    print(IFC)