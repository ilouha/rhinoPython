import rhinoscriptsyntax as rs

def create_layers():
    # Create the parent layer
    parent_layer = "05_Drafting"
    if not rs.IsLayer(parent_layer):
        rs.AddLayer(parent_layer, (255, 255, 255))  # Set color to white for the parent layer
    
    # Layer definitions with names, colors, linetypes, print widths, and print colors (Greyscale)
    layers_data = [
        {"name": "05_Dashed", "color": (0, 0, 255), "linetype": "Overhead", "print_width": 0.09, "print_color": (200, 200, 200)},
        {"name": "05_Lw00", "color": (255, 128, 128), "linetype": "Continuous", "print_width": 0.04, "print_color": (230, 230, 230)},
        {"name": "05_Lw01", "color": (255, 0, 0), "linetype": "Continuous", "print_width": 0.04, "print_color": (0, 0, 0)},
        {"name": "05_Lw02", "color": (255, 255, 0), "linetype": "Continuous", "print_width": 0.09, "print_color": (100, 100, 100)},
        {"name": "05_Lw03", "color": (255, 0, 255), "linetype": "Continuous", "print_width": 0.12, "print_color": (150, 150, 150)},
        {"name": "05_Lw04", "color": (255, 255, 255), "linetype": "Continuous", "print_width": 0.18, "print_color": (180, 180, 180)},
        {"name": "05_Lw05", "color": (0, 255, 255), "linetype": "Continuous", "print_width": 0.25, "print_color": (50, 50, 50)},
        {"name": "05_Lw06", "color": (255, 128, 255), "linetype": "Continuous", "print_width": 0.35, "print_color": (80, 80, 80)},
        {"name": "05_Lw07", "color": (255, 255, 255), "linetype": "Continuous", "print_width": 0.53, "print_color": (40, 40, 40)},
        {"name": "05_Hatch_01", "color": (0, 0, 0), "linetype": "Default", "print_width": 0, "print_color": (0, 0, 0)},
        {"name": "05_Hatch_02", "color": (0, 0, 0), "linetype": "Default", "print_width": 0, "print_color": (0, 0, 0)},
        {"name": "05_Annotation", "color": (255, 255, 255), "linetype": "Continuous", "print_width": 0.09, "print_color": (200, 200, 200)},
        {"name": "05_Dimensions", "color": (255, 255, 255), "linetype": "Default", "print_width": 0, "print_color": (100, 100, 100)},
        {"name": "05_Lw03 - Landscape", "color": (0, 255, 0), "linetype": "Continuous", "print_width": 0.01, "print_color": (150, 150, 150)},
    ]
    
    # Loop through each sub-layer and create it under the parent
    for layer_data in layers_data:
        # Generate the full name for the nested layer
        full_layer_name = parent_layer + "::" + layer_data["name"]
        
        # Create the nested layer if it doesn't exist
        if not rs.IsLayer(full_layer_name):
            rs.AddLayer(full_layer_name, layer_data["color"])
        
        # Set layer print width, linetype, and print color
        rs.LayerPrintWidth(full_layer_name, layer_data["print_width"])
        rs.LayerLinetype(full_layer_name, layer_data["linetype"])
        rs.LayerPrintColor(full_layer_name, layer_data["print_color"])

# Call the function to create the layers
create_layers()
