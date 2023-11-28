import math
import numpy as np


def sgn(num):
    if num >= 0:
        return 1
    else:
        return -1


def Check_intersection(circle_origin, pt1, pt2, radius):
    origin_x = circle_origin[0]
    origin_y = circle_origin[1]
    x1 = pt1[0]
    y1 = pt1[1]
    x2 = pt2[0]
    y2 = pt2[1]

    x1_offset = x1 - origin_x
    y1_offset = y1 - origin_y
    x2_offset = x2 - origin_x
    y2_offset = y2 - origin_y

    dx = x2_offset - x1_offset
    dy = y2_offset - y1_offset
    dr = math.sqrt(dx**2 + dy**2)
    D = x1_offset*y2_offset - x2_offset*y1_offset
    discriminant = (radius**2) * (dr**2) - D**2

    if discriminant >= 0:
        sol_x1 = (D * dy + sgn(dy) * dx * np.sqrt(discriminant)) / dr**2
        sol_x2 = (D * dy - sgn(dy) * dx * np.sqrt(discriminant)) / dr**2
        sol_y1 = (- D * dx + abs(dy) * np.sqrt(discriminant)) / dr**2
        sol_y2 = (- D * dx - abs(dy) * np.sqrt(discriminant)) / dr**2

        sol1 = [sol_x1 + origin_x, sol_y1 + origin_y]
        sol2 = [sol_x2 + origin_x, sol_y2 + origin_y]

        minX = min(x1, x2)
        maxX = max(x1, x2)
        minY = min(y1, y2)
        maxY = max(y1, y2)

        if (minX <= sol1[0] <= maxX and minY <= sol1[1] <= maxY) or (minX <= sol2[0] <= maxX and minY <= sol2[1] <= maxY):
            return True
    return False


def get_Acollision_heading(origin, heading, radius, obstacle_pos, obs_radius, num_rays=30):
    points = []
    offset = 360/num_rays
    left_heading = heading - offset
    right_heading = heading + offset

    point_heading = (origin[0] + (radius * np.cos(np.radians(heading))),
                    origin[1] + (radius * np.sin(np.radians(heading))))
    points.append(point_heading)

    if Check_intersection(obstacle_pos, origin, point_heading, obs_radius):
        for counter in range(num_rays - 1):
            point_left = (origin[0] + (radius * np.cos(np.radians(left_heading))),
                            origin[1] + (radius * np.sin(np.radians(left_heading))))
            point_right = (origin[0] + (radius * np.cos(np.radians(right_heading))),
                            origin[1] + (radius * np.sin(np.radians(right_heading))))
            left_heading -= offset
            right_heading += offset
            points.append(point_left)
            points.append(point_right)
            if Check_intersection(obstacle_pos, origin, point_left, obs_radius) == False:
                points.append(point_left)
                break
            elif Check_intersection(obstacle_pos, origin, point_right, obs_radius) == False:
                points.append(point_right)
                break
    return points
