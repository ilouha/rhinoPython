import rhinoscriptsyntax as rs

def resetLayerStructure():
    # Get all layers in the Rhino document
    layers = rs.LayerNames()
    dic = {}

    for layer in layers:
        
        print(layer)
        layer_id = rs.LayerId(layer)

        layer_name = rs.LayerName(layer_id)
        layer_color = rs.LayerColor(layer_id)
        layer_linetype = rs.LayerLinetype(layer_id)
        layer_print_color = rs.LayerPrintColor(layer)
        layer_print_width = rs.LayerPrintWidth(layer)


        dic[layer_name] = {

            'layer color' : layer_color,
            'layer linetype' : layer_linetype,
            'layer print color' : layer_print_color,
            'layer print width' : layer_print_width,
        }
        
    
    print(dic)

if __name__ == "__main__":
    print('hello world')
