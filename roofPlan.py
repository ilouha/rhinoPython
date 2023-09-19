#create a function for a gabled roof 

def roof(point,w,l,h):

    x = point[0]
    y = point[1]
    z = point[2]

    #first horizontal row, left to right
    pt1 = (x,y,z)
    pt2 = (x + 1/4*w,y,z+h)
    pt3 = (x + 1/2*w,y,z)

    #second horizontal row, left to right
    pt4 = (x+1/2*w,y+1/2*l,z)
    pt5 = (x+3/4*w,y+1/2*l,z+h)
    pt6 = (x+w,y+1/2*l,z)

    #third horizontal row, left to right
    pt7 = (x +1/4*w,y+3/4*l,z+h)
    pt8 = (x + 3/4*w,y+3/4*l,z+h)
    pt9 = (x+w, y+3/4*l,z+h)

    #fourth horizontal row, left to right
    pt10 = (x,y+l,z)
    pt11 = (x + 1/4*w, y+l,z+h)
    pt12 = (x+ 1/2*w, y+l,z)
    pt13 = (x+w,y+l,z)

    Outerline = [

        pt1,
        pt2,
        pt3,
        pt4,
        pt5,
        pt6,
        pt9,
        pt13,
        pt12,
        pt11,
        pt10,
        pt1

    ]

    ridges = [
        [pt2,pt11],
        [pt7,pt9],
        [pt5,pt8]
    ]
    

    hips = [

        [pt7,pt4],
        [pt8,pt4],
        [pt8,pt6],
        [pt7,pt12]

    ]
    
    return Outerline

roof((0,0,0),50,30,5)