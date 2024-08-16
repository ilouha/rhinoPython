import rhinoscriptsyntax as rs

def slice_and_pipe_shape():
    # Select the object to contour
    obj_id = rs.GetObject("Select the surface or polysurface to contour", rs.filter.surface | rs.filter.polysurface)
    if not obj_id:
        return
    
    # Get the base point and a second point to define the direction
    base_point = rs.GetPoint("Pick a base point for contouring")
    second_point = rs.GetPoint("Pick a second point to define the direction")
    if not base_point or not second_point:
        return
    
    # Calculate the direction vector
    direction = rs.VectorCreate(second_point, base_point)
    
    # Get the spacing between contours
    contour_spacing = rs.GetReal("Enter contour spacing", 1.0)
    if not contour_spacing:
        return
    
    # Get the pipe radius
    input_radius = rs.GetReal("Enter pipe radius", 0.1)
    if not input_radius:
        return
    
    # Normalize the direction vector to ensure consistent spacing
    direction = rs.VectorUnitize(direction)
    
    # Find the bounding box of the object to determine the extent of contouring
    bbox = rs.BoundingBox(obj_id)
    if not bbox:
        return
    
    # Calculate the total length of the contouring path
    total_length = rs.Distance(bbox[0], bbox[2])
    
    # Initialize a list to store all contours
    all_contours = []
    
    # Move a plane along the direction vector, generating contours at each step
    for i in range(int(total_length / contour_spacing)):
        # Calculate the contour plane position
        contour_plane_origin = rs.PointAdd(base_point, rs.VectorScale(direction, i * contour_spacing))
        contour_plane = rs.PlaneFromNormal(contour_plane_origin, direction)
        
        # Generate contours
        contours = rs.AddSrfContourCrvs(obj_id, contour_plane)
        if contours:
            all_contours.extend(contours)
    
    if all_contours:
        pipes = []
        for contour in all_contours:
            # Pipe each contour line with the given radius
            pipe = rs.AddPipe(contour, 0, input_radius)
            if pipe:
                pipes.append(pipe)
                
        # Optionally delete the original contours
        rs.DeleteObjects(all_contours)
        
        rs.Redraw()
        print(f"Created {len(pipes)} pipes from contour lines.")
    else:
        print("No contours generated.")
        
if __name__ == "__main__":
    slice_and_pipe_shape()
