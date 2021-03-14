# # Imports
import fileinput
import re
import os


# Inputs
# What to search for
text_to_search = r'c\([0-9]+\)'
replacement_text = "REPLACED"

# Helpers


def getFilePath(fileDirectory, fileName):
    return r'{filePath}\{fileName}'.format(filePath=fileDirectory, fileName=fileName)


# Variables
fileToEditDirectory = r'.\FilesToEdit'
print('File Directory Found')

# Loop through filesToEdit Folder
for fileName in os.listdir(fileToEditDirectory):
    # Open one of the files
    # filePath = r'{filePath}\{fileName}'.format(
    #     filePath=fileToEditDirectory, fileName=fileName)
    # print('Editting: ', filePath)
    filePath = getFilePath(fileToEditDirectory, fileName)
    print('Editting: ', filePath)

    with fileinput.FileInput(filePath, inplace=True) as file:
        # For each line
        for line in file:
            # Find pattern in the current line
            pattern_match = re.findall(text_to_search, line)
            # Replace with desired if pattern matches
            if pattern_match:
                print(line.replace(pattern_match[0], replacement_text), end='')
            else:
                # else rewrite unchanged line
                print(line, end='')
