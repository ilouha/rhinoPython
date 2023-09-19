import rhinoscriptsyntax as rs

def flatten_layers():
    # Get all layers in the Rhino document
    layers = rs.LayerNames()
    
    for layer in layers:
        
        objects_in_layer = rs.ObjectsByLayer(layer)
        
        if objects_in_layer:
            
            layer_name = layer.replace(':','_')
            
            layer_id = rs.LayerId(layer)
            layer_color = rs.LayerColor(layer_id)
            layer_material = rs.LayerMaterialIndex(layer_id)
            
            
            new_layer = rs.AddLayer(layer_name)
            new_layer_id = rs.LayerId(new_layer)
            new_layer_color = rs.LayerColor(new_layer_id,layer_color)
            new_layer_material = rs.LayerMaterialIndex(new_layer_id,layer_material)
            
            rs.ObjectLayer(objects_in_layer,new_layer_id)
            
        
        else:
            
            print('false')
            
if __name__ == "__main__":
    flatten_layers()
