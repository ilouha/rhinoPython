import rhinoscriptsyntax as rs

def is_rectangle(curve):
    # Ensure the curve is closed and a polyline
    if not rs.IsCurveClosed(curve) or not rs.IsPolyline(curve):
        return False
    
    # Get the vertices of the polyline
    points = rs.PolylineVertices(curve)
    
    # Ensure there are exactly 5 points (4 corners + start point repeated)
    if len(points) != 5:
        return False
    
    # Check if opposite sides are equal and if all angles are 90 degrees
    def are_equal(p1, p2, p3, p4):
        return rs.Distance(p1, p2) == rs.Distance(p3, p4)

    def is_right_angle(p1, p2, p3):
        vec1 = rs.VectorCreate(p2, p1)
        vec2 = rs.VectorCreate(p2, p3)
        return abs(rs.VectorDotProduct(vec1, vec2)) < 1e-6

    if (are_equal(points[0], points[1], points[2], points[3]) and
        are_equal(points[1], points[2], points[3], points[0]) and
        is_right_angle(points[0], points[1], points[2]) and
        is_right_angle(points[1], points[2], points[3]) and
        is_right_angle(points[2], points[3], points[4]) and
        is_right_angle(points[3], points[4], points[0])):
        return True
    return False

def offset_line(p1, p2, distance, layer_name):
    vector = rs.VectorCreate(p2, p1)
    vector = rs.VectorUnitize(vector)
    perp_vector = rs.VectorRotate(vector, 90, [0, 0, 1])
    offset_p1 = rs.PointAdd(p1, rs.VectorScale(perp_vector, distance))
    offset_p2 = rs.PointAdd(p2, rs.VectorScale(perp_vector, distance))
    line = rs.AddLine(offset_p1, offset_p2)
    if line:
        rs.ObjectLayer(line, layer_name)
    return line

def ensure_layer_exists(layer_name):
    if not rs.IsLayer(layer_name):
        rs.AddLayer(layer_name)
    if rs.IsLayer(layer_name):
        return True
    return False

def offset_rectangle_edges():
    # Select a rectangle curve
    rectangle = rs.GetObject("Select a rectangle", rs.filter.curve)
    if not rectangle:
        return
    
    # Ensure the selected curve is a rectangle
    if not is_rectangle(rectangle):
        rs.MessageBox("The selected curve is not a rectangle.")
        return

    # Get offset distances
    x_offset = rs.GetReal("Enter the offset distance for the shortest edge")
    y_offset = rs.GetReal("Enter the offset distance for the opposite short edge")
    z_offset = rs.GetReal("Enter the offset distance for the long edges")

    if x_offset is None or y_offset is None or z_offset is None:
        rs.MessageBox("Invalid input for offset distances.")
        return

    # Ensure the layer '01_Setbacks' exists
    layer_name = '01_Setbacks'
    if not ensure_layer_exists(layer_name):
        rs.MessageBox("Layer '01_Setbacks' could not be created.")
        return
    
    # Get the rectangle corners
    corners = rs.PolylineVertices(rectangle)
    if len(corners) != 5:
        rs.MessageBox("The selected curve is not a valid rectangle.")
        return

    # Determine the shortest and longest edges
    edges = [(corners[i], corners[i+1], rs.Distance(corners[i], corners[i+1])) for i in range(4)]
    edges.sort(key=lambda edge: edge[2])
    shortest_edge = edges[0]
    opposite_short_edge = edges[1]
    long_edge1 = edges[2]
    long_edge2 = edges[3]

    # Offset the shortest edge by x_offset
    if not offset_line(shortest_edge[0], shortest_edge[1], x_offset, layer_name):
        rs.MessageBox("Failed to offset the shortest edge.")

    # Offset the opposite short edge by y_offset
    if not offset_line(opposite_short_edge[0], opposite_short_edge[1], y_offset, layer_name):
        rs.MessageBox("Failed to offset the opposite short edge.")

    # Offset the long edges by z_offset
    if not offset_line(long_edge1[0], long_edge1[1], z_offset, layer_name):
        rs.MessageBox("Failed to offset the first long edge.")
    if not offset_line(long_edge2[0], long_edge2[1], z_offset, layer_name):
        rs.MessageBox("Failed to offset the second long edge.")

    rs.MessageBox("Successfully offset the rectangle edges and placed them on the '01_Setbacks' layer.")

if __name__ == "__main__":
    offset_rectangle_edges()
