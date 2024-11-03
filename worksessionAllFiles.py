import rhinoscriptsyntax as rs
import os

def attach_worksessions_from_folder():
    # Prompt user to select a folder
    folder_path = rs.BrowseForFolder(None, "Select folder containing .3dm files for worksessions")
    if not folder_path:
        print("No folder selected.")
        return

    # Get all .3dm files in the folder
    files = [f for f in os.listdir(folder_path) if f.endswith(".3dm")]
    if not files:
        print("No .3dm files found in the selected folder.")
        return

    # Attach each .3dm file as a worksession
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        rs.Command('-_Worksession _Attach "{}" _Enter'.format(file_path), echo=False)
        print("Attached worksession for: {}".format(file_name))

    print("All .3dm files in the folder have been attached as worksessions.")

# Run the function
attach_worksessions_from_folder()
