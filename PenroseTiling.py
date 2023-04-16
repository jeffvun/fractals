import math

phi = (1 + math.sqrt(5)) / 2  # golden ratio

# Define rhombus r1
r1_p1 = (0, 0)
r1_p2 = (1, 0)
r1_p3 = (1/2, (math.sqrt(5)-1)/2)
r1_p4 = ((1-phi)/2, phi/2-1)
r1 = [r1_p1, r1_p2, r1_p3, r1_p4]

# Define rhombus r2
r2_p1 = (0, 0)
r2_p2 = (1/2, (math.sqrt(5)-1)/2)
r2_p3 = (phi/2-1, (1-phi)/2)
r2_p4 = (0, 1)
r2 = [r2_p1, r2_p2, r2_p3, r2_p4]

def penrose_tiling(order, polygon_list):
    if order == 0:
        return polygon_list

    new_polygon_list = []
    for polygon in polygon_list:
        if polygon == r1:
            # Divide r1 into five smaller rhombuses
            s = (polygon[0][0] + polygon[1][0] + polygon[2][0] + polygon[3][0])/5
            t = (polygon[0][1] + polygon[1][1] + polygon[2][1] + polygon[3][1])/5
            a = polygon[0]
            b = ((2*polygon[0][0] + polygon[1][0])/3, (2*polygon[0][1] + polygon[1][1])/3)
            c = ((polygon[0][0] + 2*polygon[1][0])/3, (polygon[0][1] + 2*polygon[1][1])/3)
            d = polygon[1]
            e = ((2*polygon[1][0] + polygon[2][0])/3, (2*polygon[1][1] + polygon[2][1])/3)
            f = ((polygon[1][0] + 2*polygon[2][0])/3, (polygon[1][1] + 2*polygon[2][1])/3)
            g = polygon[2]
            h = ((2*polygon[2][0] + polygon[3][0])/3, (2*polygon[2][1] + polygon[3][1])/3)
