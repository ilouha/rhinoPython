import rhinoscriptsyntax as rs
import os

def export_selected_groups_to_files():
    # Prompt user to select objects
    selected_objects = rs.GetObjects("Select objects to export by groups", group=True, preselect=True)
    if not selected_objects:
        print("No objects selected.")
        return

    # Collect unique group names from the selected objects
    groups = set()
    for obj in selected_objects:
        group_list = rs.ObjectGroups(obj)
        if group_list:
            groups.update(group_list)

    if not groups:
        print("No groups found in the selection.")
        return

    # Prompt user to specify a folder for export
    folder_path = rs.BrowseForFolder(None, "Select folder to save exported group files")
    if not folder_path:
        print("No folder selected.")
        return

    # Iterate over each group and export it as a separate file
    for i, group in enumerate(groups):
        # Select objects in the current group
        group_objects = rs.ObjectsByGroup(group)
        if not group_objects:
            continue

        rs.UnselectAllObjects()
        rs.SelectObjects(group_objects)

        # Create a file path for the exported group
        file_name = "building no {}.3dm".format(i + 1)
        file_path = os.path.join(folder_path, file_name)

        # Export selected group to file
        rs.Command('-_Export "{}" _Enter _Enter'.format(file_path), echo=False)

        print("Group {} exported to: {}".format(group, file_path))

    print("Export completed.")

# Run the function
export_selected_groups_to_files()
