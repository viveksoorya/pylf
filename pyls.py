"""
requirements/ criteria for done-ness


# *general instructions*
* docstrings for each function (this will take care of the --help switch)
* we need two files, one the bundle of software that implements pylf and then test_pylf.py, a test module/file
* use only function, no python classes .
* mark issue as resolved once the feature is fully implemented.

# *tests, assets, decomposition*
* test must be *meaningful* and *test extremities* of what your functions might encounter.
* ? assert statements at the start of the funciton are recommended to assert that the things assumed about the input do indeed hold.
* use assert a lot
* write test cases for outputs of all functions. Asserts for outputs are not necessary (for they would be redundant, given we write the tests for outputs and asserts for inputs)
* for each function written, there has to be an associated test-function in test_pylf.py. This also means
* Decompose each function into more functions to the level of granularity where each function can be tested as a unit.
* there may be expectations that are not explicitly stated. Glean this out and make it part of the issue set. Assumptions may need to be made. In such cases, explicitly state the assumptions in the corresponding functions' docstrings. 

# *commits, issues*
* commit messages must be meaningful. This also means
* commit after every issue is resolved. Meaning decomposing the whole problem into discrete meaningful issues is necessary.
* Record of Issues, serves as documentation for people who want to use your tool. Write issues accordingly.
* while committing mention issue id that is resovled. Commit after an issue is resolved. As many commits as there are issues.
* use function skeleton structure to first write the documentation and the dummy output to get a feel for the function's contents. Commit after function skeleton is written.
* lean towards (err on the side of) commiting frequently in meaningful chunks.



* Optional: if you are using a library, write and/or run tests to check your understanding of it.
* Note: being well-tested is to be among the criteria used when considering the use of library in your code.
"""

"""
?

issues: are they like flag-wise problem factoring or are they more-abstractly decomposed units?

"This will let you later on switch between issues and editable notes you add there and the immutable commits that address them." why would I want this?

Tip is unclear (point 4)

do we commit and push after each function skeleton or after we write all function skeletons?
"""

import argparse
import os

parser = argparse.ArgumentParser(prog='argparseTinkerTool', description='testing out argparser', epilog='end')

parser.add_argument('-F', '--filetype', help = 'displays file type', action = 'store_true')
parser.add_argument('-a', '--all', help = 'displays all files including hidden ones', action = 'store_true')
parser.add_argument('-l', '--long', help = 'displays metadata of files', action = 'store_true')
parser.add_argument('foldername')

args = parser.parse_args()

#def main(args):
 #   results = getDescriptionsOfFilesInDir(args)
  #  displayResults(results, args)

def getDescriptionsOfFilesInDir(directory):
    """
    define input:

    Lists the files and folders in the given directory and constructs a list of dicts with the required info.
    flags is a structure with the following fields -
    . dirname = The directory whhose contents are to be listed
    .long_format = True if the user has asked for the long format.
    .filetype = True if the user has asked for a file type info as well.

    define output:

    The return value is a list of dictionaries each with the following fields -
    "filename" = The name of the file.
    "filetype" = "d", "f", or "x" indicating "directory", "plain file", or "executable file", respectively.
    "modtime" = Last modified time of the file as a 'datetime' object
    "filesize" = Number of bytes in the file.
    """
    
    
    # [\check]: using os library extract the file names

        

    assert (isinstance(directory,str)) # asserts that the input is a string
    #directory = "pylf"
    #print(directory)
    #print(1)
    listOfEntriesInTheDirectory = []
    for inode in os.listdir(directory):
       filepath = os.path.join(directory, inode)

       if os.path.isfile(filepath):
          metadata = os.stat(filepath)

          listOfEntriesInTheDirectory.append({
              "filename": inode,
              "size": metadata.st_size,
              "last modified": metadata.st_mtime
          }) 
          #print(1) testing to see if this branch is entered 
       else:
           listOfEntriesInTheDirectory.append({
               "foldername": inode,
               "size": 0,
               "last modified": metadata.st_mtime
        })
           #print(2) testing to see if this branch is entered 
    #print(listOfEntriesInTheDirectory) asserting non-emptiness of list
    
    return listOfEntriesInTheDirectory

    

def displayResults(results, flags):
    """
    Takes a list of file descriptions and display control flags and prints to the standard output.

    Inpts -
    results = List of dictionaries, like returned by getDescriptionOfFilesInDir()
    controls = Object with attributes .long_format and .filetype indicating how to show the information.

    Outputs:
    To standard output. Returns None.
    """
    print()

getDescriptionsOfFilesInDir(args.foldername)
#main(args)
