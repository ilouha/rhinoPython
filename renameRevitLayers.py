import rhinoscriptsyntax as rs

def rename_and_group_layers():
    # Mapping for layer abbreviations to full descriptions and categories
    layer_categories = {
        'A-WALL': ('Architectural', 'Wall'),
        'A-FLOR': ('Architectural', 'Floor'),
        'I-WALL': ('Interior', 'Wall'),
        'C-TOPO': ('Civil', 'Topography'),
        'I-FURN': ('Interior', 'Furniture'),
        'P-SANR-FIXT': ('Plumbing', 'Sanitary Fixtures'),
        'A-AREA': ('Architectural', 'Area'),
        'A-DOOR-FRAM': ('Architectural', 'Door Frame'),
        'A-DOOR': ('Architectural', 'Door'),
        'A-DOOR-GLAZ': ('Architectural', 'Door Glazing'),
        'A-FLOR-HRAL': ('Architectural', 'Floor Handrail'),
        'A-ROOF': ('Architectural', 'Roof'),
        'A-GLAZ': ('Architectural', 'Glazing'),
        'Q-SPCQ': ('Equipment', 'Specialty Casework'),
        'Q-CASE': ('Equipment', 'Casework'),
        'I-FURN-PNLS': ('Interior', 'Furniture Panels'),
        'A-FLOR-OTLN': ('Architectural', 'Floor Outline'),
        'A-CLNG': ('Architectural', 'Ceiling'),
        'M-EQPM': ('Mechanical', 'Equipment'),
        'A-DETL': ('Architectural', 'Detail'),
        'S-STRS': ('Structural', 'Stairs'),
        'E-ELEC-FIXT': ('Electrical', 'Fixtures'),
        'E-ELEC-EQPM': ('Electrical', 'Equipment'),
        'E-LITE-EQPM': ('Electrical', 'Lighting Equipment'),
        'E-FIRE': ('Electrical', 'Fire Protection'),
        'A-GENM': ('Architectural', 'General'),
        'A-ROOF-OTLN': ('Architectural', 'Roof Outline'),
        'G-ANNO-SYMB': ('General', 'Annotations and Symbols'),
        '0': ('Default', 'Default Layer'),
        # Newly added layers
        'A-FLOR-LEVL': ('Architectural', 'Floor Level'),
        'A-DOOR-HDLN': ('Architectural', 'Door Headline'),
        'A-GLAZ-CURT': ('Architectural', 'Curtain Glazing'),
        'A-GLAZ-CWMG': ('Architectural', 'CW Metal Glazing'),
        'S-COLS': ('Structural', 'Columns'),
        'S-BEAM': ('Structural', 'Beams')
    }
        
    # Helper function to update layer names inside blocks
    def update_block_layers(block_name):
        # Explode the block to modify its contents
        block_objects = rs.BlockObjects(block_name)
        if block_objects:
            for obj in block_objects:
                obj_layer = rs.ObjectLayer(obj)
                # Check if the object's layer is in the layer_categories dictionary
                if obj_layer in layer_categories:
                    category, descriptive_name = layer_categories[obj_layer]
                    new_layer_name = "{}::{}".format(category, descriptive_name)
                    if not rs.IsLayer(new_layer_name):
                        rs.AddLayer(new_layer_name)
                    rs.ObjectLayer(obj, new_layer_name)
    
    # Get all layers in the document
    layers = rs.LayerNames()
    
    if layers:
        for layer in layers:
            # Get the category and descriptive name from the mapping
            category, descriptive_name = layer_categories.get(layer, ('Unknown', 'Unknown Layer'))
            
            # Ensure we're not working with unknown categories
            if category != 'Unknown' and descriptive_name != 'Unknown Layer':
                # Create the full new layer name as "Category::Descriptive Layer Name"
                new_layer_name = "{}::{}".format(category, descriptive_name)
                
                # Check if the new layer already exists
                if not rs.IsLayer(new_layer_name):
                    # Create the new layer
                    rs.AddLayer(new_layer_name)
                
                # Move the objects from the old layer to the new layer
                objects = rs.ObjectsByLayer(layer)
                if objects:
                    for obj in objects:
                        rs.ObjectLayer(obj, new_layer_name)
                
                # Update blocks that may be using the old layer names
                block_definitions = rs.BlockNames()
                if block_definitions:
                    for block in block_definitions:
                        update_block_layers(block)
                
                # Optionally, delete the old layer if it's empty
                if rs.IsLayerEmpty(layer):
                    rs.DeleteLayer(layer)

# Run the function to rename and group layers, including updating blocks
rename_and_group_layers()
