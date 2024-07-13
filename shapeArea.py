import rhinoscriptsyntax as rs

def add_area_text():
    # Select the shape
    shape = rs.GetObject("Select a shape to calculate the area", rs.filter.curve | rs.filter.surface | rs.filter.polysurface)
    if not shape:
        print("No shape selected.")
        return
    
    # Calculate the area
    if rs.IsCurve(shape):
        area = rs.CurveArea(shape)
    elif rs.IsSurface(shape):
        area = rs.SurfaceArea(shape)[0]
    elif rs.IsPolysurface(shape):
        area = rs.SurfaceArea(shape)[0]
    else:
        print("Selected object is not a valid shape.")
        return
    
    if area is None:
        print("Could not calculate the area.")
        return
    
    # Find the centroid of the shape
    if rs.IsSurface(shape) or rs.IsPolysurface(shape):
        centroid = rs.SurfaceAreaCentroid(shape)
    else:
        centroid = rs.CurveAreaCentroid(shape)
        
    if not centroid:
        print("Could not determine the centroid.")
        return
    
    # Create the text with the area
    print(area[0])
    area_text = "AREA: {}SF".format(round(area[0],2))
    text_height = 0.25  # Adjust the text height as needed
    text_point = centroid[0]  # Extracting the point from the centroid result
    
    # Add text to the document
    rs.AddText(area_text, text_point, height=text_height)
    print(f"Added text: {area_text} at point: {text_point}")

# Run the function
if __name__ == "__main__":
    add_area_text()
