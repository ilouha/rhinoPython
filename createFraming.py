"""
NOTE:
Notice the 'async:true' specifier below. This ensures this script is run
on a non-ui thread so Rhino UI does not get locked when script is running.
"""
#! python 3


import rhinoscriptsyntax as rs 
import Rhino

def createPlane(origin,curve_id,t):

    
    x_axis = rs.CurveTangent(curve_id,t)
    #y_axis = [-x_axis.X,-x_axis.Y,-x_axis.Z]
    y_axis = [0,1,0]
    plane = rs.PlaneFromFrame(origin,x_axis,y_axis)
    
    return plane

def createFramingMember(curve_id,point,height):

    t = rs.CurveClosestPoint(curve_id,point)
    plane = createPlane(point,curve_id,t)
    rec = rs.AddRectangle(plane,2,6)
    
    path = rs.AddLine([0,0,0], [0,0,height])
    extrude = rs.ExtrudeCurve(rec,path)
    brep = rs.CapPlanarHoles(extrude)

    return brep

def divideSill(line,height):

    curve_id = line
    length = 16

    points = rs.DivideCurveLength(curve_id, 
        length,
        create_points=False,
        return_points=True)

    number_points = len(points) + 1

    frame_points = rs.DivideCurve(
        curve_id,
        number_points,
        create_points = True,
        return_points = True
    )

    frames = [] 
    profiles = []

    for point in frame_points:

        rec = createFramingMember(curve_id,point,height)

        profiles.append(rec)

    return profiles


if __name__ == "__main__":

    line = rs.AddLine((0,0,0),(80,40,0))
    select_result = rs.GetCurveObject("Select curve")
    if select_result:
        height = rs.GetInteger('input height')
        divideSill(select_result[0],height)
    
    
