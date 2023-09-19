"""
NOTE:

- Reference to RhinoCommmon.dll is added by default

- You can specify your script requirements like:

    # r: <package-specifier> [, <package-specifier>]
    # requirements: <package-specifier> [, <package-specifier>]

    For example this line will ask the runtime to install
    the listed packages before running the script:

    # requirements: pytoml, keras

    You can install specific versions of a package
    using pip-like package specifiers:

    # r: pytoml==0.10.2, keras>=2.6.0
"""
#! python3

import rhinoscriptsyntax as rs
import scriptcontext as sc

import System
import System.Collections.Generic
import Rhino

import Rhino.Geometry as rg

#function to create a lot in Rhino by dimensions
def createLot(x,y,z,width, length):
    
    plane = rs.WorldXYPlane()
    plane = rs.MovePlane(plane,(x,y,z))
    lot = rs.AddRectangle( plane, width, length )

    return lot 

#function to create setbacks
def createSetbacks(lot):

    lot_lines = rs.ExplodeCurves(lot)

    frontYard = 20
    rearYard = 15 
    sideYard = 5

    #create the moving distances for the objects
    movingDistances = [frontYard,sideYard,-rearYard,-sideYard]

    frontYard = rs.MoveObject(lot_lines[0],[0,frontYard,0])
    rearYard = rs.MoveObject(lot_lines[2],[0,-rearYard,0])
    sideYard01 = rs.MoveObject(lot_lines[1],[-sideYard,0,0])
    sideYard02 = rs.MoveObject(lot_lines[3],[sideYard,0,0])

    pass 

#function to create a building
def createBasicBuilding(buildingWidth,BuildingLength,BuildingHeight,lotWidth,LotLength):

    plane = rs.WorldXYPlane()

    footprint = rs.AddRectangle(plane,buildingWidth,BuildingLength)
    footprint = rs.MoveObject(footprint,[lotWidth/4,lotLength/4,0])

    guid_line = rs.AddLine([0,0,0],[0,0,BuildingHeight])
    bldg = rs.ExtrudeCurve(footprint,guid_line)
    bldg = rs.CapPlanarHoles(bldg)

    rs.DeleteObject(guid_line)
    
    pass

#function to create a gabled roof building
def createGabledBuilding(x,y,z,width,length,height,ridge):

    #point = rs.GetPoint("select a point")

    #x = point.X
    #y = point.Y
    #z = point.Z

    pt1 = [x,y,z]
    pt2 = [x+width,y,z]
    pt3 = [x+width,y,z+height]
    pt4 = [x+width/2,y,z+height+ridge]
    pt5 = [x,y,z+height]
    
    list_pt = [pt1,pt2,pt3,pt4,pt5,pt1]

    buildingProfile = rs.AddPolyline(list_pt)

    guid_curve = rs.AddLine(
        [0,0,0],[0,length,0]
    )

    building_Envelope = rs.ExtrudeCurve(buildingProfile,guid_curve)
    building_Envelope = rs.CapPlanarHoles(building_Envelope)

    rs.DeleteObject(guid_curve)



if __name__ ==  "__main__":
    

    lotWidth = 50 
    lotLength = 150 
    numberLots = 5

    for i in range(0,numberLots):

        lot = createLot(lotWidth*i,0,0,lotWidth,lotLength)
        yards = createSetbacks(lot)

        x = (i * lotWidth) + 5
        y = 0
        z = 0

        #create the buildings on the lot

        frontStructure = createGabledBuilding(
            x,20,0,
            width = 25,
            length = 30,
            height = 15,
            ridge = 10
        )

        rearStructure = createGabledBuilding(
            x,70,0,
            width = 35,
            length = 45,
            height = 25,
            ridge = 15
        )

   