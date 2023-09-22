import rhinoscriptsyntax as rs
import os

# Specify the output folder where the images will be saved
output_folder = "C:\Users\ilouh\Desktop\Barclays\Views"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Get a list of all named views in the Rhino document
named_views = rs.NamedViews()

# Loop through each named view
for named_view in named_views:
    # Activate the named view
    rs.RestoreNamedView(named_view)
    
    print(named_view)
    # Define the image file path (you can customize the file format and name)
    image_file = os.path.join(output_folder, "{}.png".format(named_view))
    
    # Capture the current view as an image
    rs.Command("-ViewCaptureToFile " + image_file + " _Enter")

# Restore the previous view (optional)
rs.RestoreNamedView(None)
