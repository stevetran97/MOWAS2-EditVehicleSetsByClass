# Documentation

#Imports
  # re is for all regular expressions uses
  # fileinput is for opening files and editting the lines
  # os is for looping through file directories


# Use
  # The input takes in a regular expression of what is searched in the editted File
  # The output replaces that exact text with new text
  # Place the files you want to edit in the FilestoEdit Folder
  # Run main.py in the console to edit-in-place the files in the Editting Folder


#Algorithm
  # Looping through the file will return each line in a string format to be worked with
  # Algorithm will only edit the line if there is a pattern match, otherwise, it rewrites what is already there

#Learning
  # print(line, end='')
  # end='' forces printing to not create a new line

  # The r prefix allows you to include \( and other unsupported metacharacters
  # text_to_search = r'c\([0-9]+\)'  