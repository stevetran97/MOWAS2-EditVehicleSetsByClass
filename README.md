# MOWAS2-EditVehicleSetsByClass
Can be used to format large blocks of vehicle.set configuration files using comments as classification blocks.

# Use
  - The input takes in a regular expression of what is searched in the editted File
  - The output replaces that exact text with new text
  - Place the files you want to edit in the FilestoEdit Folder
  - Run main.py in the console to edit-in-place the files in the Editting Folder

# Algorithm
  - Loops through each set file in the Editting Folder
  - Looping through the file will return each line in a string format to be worked with
  - The Algorithm searches the line and searches for a pattern
  - The Algorithm will only edit the line if there is a pattern match, otherwise, it rewrites what is already there
