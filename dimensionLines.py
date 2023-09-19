import rhinoscriptsyntax as rs 
import Rhino

#definitions

def createAlignedDimension(line):

    startPoint = rs.CurveStartPoint(line)
    endPoint = rs.CurveEndPoint(line)
    #offset_direction = #calculate the normal of the line

    offset_curve = rs.OffsetCurve(line,
        [0,1,0],
        5,
        normal=None,
        style=1)

    midPoint = rs.CurveMidPoint(offset_curve)

    #returns the function 
    dim = rs.AddAlignedDimension(startPoint,endPoint,midPoint)

    #sets the dimensions on a certain layer

    if rs.LayerId(('Dims')):
        
        rs.ObjectLayer(dim,'Dims')
    
    else:

        rs.AddLayer(name='Dims', color=None, visible=True, locked=False, parent=None)
        rs.ObjectLayer(dim,'Dims')

    return dim
    #deletes the objects that were used for creating the lines. 

    rs.DeleteObjects(

        startPoint,
        endPoint,
        offset_curve,
        midPoint,

    )

def dimensionGrids():
    pass

def dimensionPlotPlan():
    pass

#execution code

if __name__ == "__main__":

    selectedCurve = rs.GetCurveObject("Select Line")[0] 
    lines = rs.ExplodeCurves(selectedCurve)

    for line in lines: 
        createAlignedDimension(line)