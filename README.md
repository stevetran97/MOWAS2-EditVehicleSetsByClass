# MOWAS2-EditVehicleSetsByClass
Can be used to format large blocks of vehicle.set configuration files using comments as classification blocks.

## Use
  - Place all of the txt/set files that you want to edit in the FilestoEdit Folder
  - The input takes a set of searched regular expression patterns (To be Replaced in set/txt files)
  - Comments — which match the strings in the vehicleClassHash table — are to be added in the txt document following the commentTrigger (default of ';')
  - The commentTriggers trigger a state change to the array set of strings used to replace the patterns
  - When the algorithm encounters a commentTrigger, it will find its new state in the vehicleClassHash by cross referencing each entry in the hash table to strings in that line
  - Run main.py in the console to edit-in-place the files in the Editting Folder

## Algorithm
  - Loops through patterns that need to be editted
  - Loops through each set (equivalent to txt) file in the Editting Folder
  - Looping through the file will return each line in a string format
  - The Algorithm check if first string key in the line is == to the commentTrigger set in main.py
  - The Algorithm uses the comment trigger to change state according to a hash table of replacement strings 
  - If the current pattern is found on the same line, replace it with the replacement string set (determined by the CURRENT state)


## Current Intrinsic Issues
  - When a state is triggered, the corresponding replacement set is used for the rest of the txt file. Anything that you do not want to be replaced needs to be replaced by a string copy of itself. In other words, the algorithm is rewriting the entire document with changes rather than just editting.

  - The algorithm will always try to replace the input pattern with the current state on EVERY line. 
