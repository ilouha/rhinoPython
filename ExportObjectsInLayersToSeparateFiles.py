import rhinoscriptsyntax as rs
import os

def export_layers_to_dwg():
    # Prompt the user for a folder to export files
    folder = rs.BrowseForFolder(None, "Select Folder to Export DWG Files")
    if not folder:
        print("No folder selected. Export canceled.")
        return
    
    # Get all layers in the document
    layers = rs.LayerNames()
    if not layers:
        print("No layers found in the document.")
        return
    
    # Iterate through each layer
    for layer in layers:
        # Select all objects on the current layer
        objs_on_layer = rs.ObjectsByLayer(layer)
        if not objs_on_layer:
            print("No objects found on layer: {}".format(layer))
            continue
        
        # Export only objects on this layer
        rs.SelectObjects(objs_on_layer)
        
        # Define the file path
        layer_name = rs.LayerName(layer, fullpath=False)
        file_path = os.path.join(folder, "{}.dwg".format(layer_name))
        
        # Export the selected objects to a DWG file
        rs.Command('-_Export "{}" _Enter'.format(file_path), echo=False)
        
        # Deselect objects after exporting
        rs.UnselectObjects(objs_on_layer)
    
    print("Export completed.")

# Run the function
export_layers_to_dwg()
