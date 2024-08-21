import rhinoscriptsyntax as rs
import random

def assign_material_to_layer():
    # Get all layers in the document
    layers = rs.LayerNames()
    
    if layers:
        for layer in layers:
            # Create a new material and get its index
            material_index = rs.AddMaterialToLayer(layer)
            
            # Check if material creation was successful
            if material_index != -1:
                # Set the material name based on the layer name
                rs.MaterialName(material_index, layer)
                
                # Optionally set material properties (color, etc.)
                # Example: Set the material color to a random color
                random_color = rs.CreateColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                rs.MaterialColor(material_index, random_color)
                
                # Assign the material to the layer
                rs.LayerMaterialIndex(layer, material_index)
                
                # Update the document to reflect changes
                rs.Redraw()
                
        print("Materials have been assigned to the layers based on their names.")
    else:
        print("No layers found in the document.")

# Run the function
assign_material_to_layer()
