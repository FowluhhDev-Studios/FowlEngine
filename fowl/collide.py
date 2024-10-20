import pyray as pr

def collide_rect_point(rectPos: tuple, rectSize: tuple, pointPos: tuple):
    return pr.check_collision_point_rec(pr.Vector2(pointPos[0], pointPos[1]), pr.Rectangle(rectPos[0], rectPos[1], rectSize[0], rectSize[1]))

def collide_rects(rect1Pos: tuple, rect1Size: tuple, rect2Pos: tuple, rect2Size: tuple):
    return pr.check_collision_recs(pr.Rectangle(rect1Pos[0], rect1Pos[1], rect1Size[0], rect1Size[1]), pr.Rectangle(rect2Pos[0], rect2Pos[1], rect2Size[0], rect2Size[1]))

def collide_circ_point(pointPos: tuple, circPos: tuple, circRadius: float):
    return pr.check_collision_point_circle(pr.Vector2(pointPos[0], pointPos[1]), pr.Vector2(circPos[0], circPos[1]), circRadius)

def collide_circs(circ1Pos: tuple, circ1Radius: float, circ2Pos: tuple, circ2Radius: float):
    return pr.check_collision_circles(pr.Vector2(circ1Pos[0], circ1Pos[1]), circ1Radius, pr.Vector2(circ2Pos[0], circ2Pos[1]), circ2Radius)

def collide_circ_rect(rectPos: tuple, rectSize: tuple, circPos: tuple, circRadius: float):
    return pr.check_collision_circle_rec(pr.Vector2(circPos[0], circPos[1]), circRadius, pr.Rectangle(rectPos[0], rectPos[1], rectSize[0], rectSize[1]))