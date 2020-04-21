#Simple: Find The Distance Between Two Points

def distance(x1, y1, x2, y2):
    x=x1-x2
    y=y1-y2
    return round((x**2+y**2)**0.5, 2)