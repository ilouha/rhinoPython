import rhinoscriptsyntax as rs
import os

def export_saved_views():
    # Prompt the user to select a folder
    folder_path = rs.BrowseForFolder(None, "Select Folder to Save Views")
    
    # If the user cancels the selection, exit the function
    if not folder_path:
        print("No folder selected. Exiting.")
        return
    
    # Ensure the folder exists (it should, since the user selected it, but check anyway)
    if not os.path.exists(folder_path):
        print("Invalid folder path.")
        return

    # Get a list of all named views
    views = rs.NamedViews()

    if views:
        # Loop through each named view
        for view in views:
            try:
                # Restore the view
                rs.RestoreNamedView(view)
                
                # Set the file path and name for each view
                file_path = os.path.join(folder_path, "{0}.png".format(view))
                
                # Capture the view to file
                rs.Command("-ViewCaptureToFile \"{0}\" _Enter".format(file_path))

            except Exception as e:
                print("Error capturing view {0}: {1}".format(view, e))
        
        print("Exported {0} views to {1}".format(len(views), folder_path))
    else:
        print("No saved views found.")

# Run the function
export_saved_views()
