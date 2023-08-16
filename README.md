### Duplicate detector (command line python tool)
This repo contains the code for a command line tool written in python, which when provided with path to directory(-ies) will check for duplicate files within the directory, inlcuding subdirectories, and across directories, if provided with multiple paths. It will then print information about the duplicates it has found,
including the name of the files sharing the exact same content, and their respective hash-ids. It also writes the results to a file called "meta.json", in which you'll a dictionary conataining information about which duplicate files were found, and all the files that have been checked in the provided directories. 

Now in order to use the commandline tool, you need to run the following command followed by a directory path: 
```
python3 detector.py <directory_path>
```

If any duplicated are detected, the command line tool will print a message in the terminal window that will look something like this:

{
Found 3 duplicates:
 b.txt = h/t/j.txt = r/v.txt (1c96838eaceb20143ebeab680c96477f94c116b50a806ca4556f6d5ed8dc4b15)
 h/y.txt = d/a.txt (9899324b0dd5f4b60e4551877f34e63c0c30c4ddf32a0c948ac559785de7021c)
 }
