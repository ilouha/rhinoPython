import rhinoscriptsyntax as rs

def change_layers_to_lowercase():
    # Get all the layers in the document
    layers = rs.LayerNames()

    if layers:
        for layer in layers:
            # Split the layer name by "::" to handle nested layers
            layer_parts = layer.split("::")
            
            # Convert only the last part of the layer name to lowercase
            layer_parts[-1] = layer_parts[-1].lower()
            
            # Join the layer parts back together to maintain hierarchy
            new_name = "::".join(layer_parts)
            
            # Rename the layer to its lowercase version
            rs.RenameLayer(layer, new_name)

# Run the function
change_layers_to_lowercase()
