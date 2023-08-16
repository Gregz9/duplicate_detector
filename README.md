### Duplicate detector (command line python tool)
This repo contains the code for a command line tool written in python, which when provided with path to directory(-ies) will check for duplicate files within the directory, inlcuding subdirectories, and across directories, if provided with multiple paths. It will then print information about the duplicates it has found,
including the name of the files sharing the exact same content, and their respective hash-ids (generated using "sha256"). It also writes the results to a file called "meta.json", in which you'll a dictionary conataining information about which duplicate files were found, and all the files that have been checked in the provided directories. 

Now in order to use the commandline tool, you need to run the following command followed by a directory path: 
```
python3 detector.py <directory_path>
```

Directory path may look something like this: 
```
<directory_path> = ./files/folder_a/
```
or 
```
<directory_path> = ~/Files/folder_a/
```

If any duplicated are detected, the command line tool will print a message in the terminal window that will look something like this:

```
Found 3 duplicates:
 b.txt = h/t/j.txt = r/v.txt (1c96838eaceb20143ebeab680c96477f94c116b50a806ca4556f6d5ed8dc4b15)
 h/y.txt = d/a.txt (9899324b0dd5f4b60e4551877f34e63c0c30c4ddf32a0c948ac559785de7021c)
```

The script can also be run with multiple directories as arguments, you simply need a white space between each directory path when running the script. E.g.
```
python3 detector.py <directory_path1> <directory_path2> <directory_path3>
```

In addition to directory paths, the user may provide the program with flags to get additional information about the files found. The first of this flags is "--sizes", and makes the program print the size of the all the duplicate files found. The call of "detector.py" using this flag will look like this: 
```
python3 detector.py --sizes <directory_path>
```
or
```
python3 detector.py --sizes <directory_path1> <directory_path2>
```

when running the script for multiple directories. The output will have the following format: 
```
Found 3 duplicates:
 (0.032 KB) b.txt = h/t/j.txt = r/v.txt (1c96838eaceb20143ebeab680c96477f94c116b50a806ca4556f6d5ed8dc4b15)
 (0.047 KB) h/y.txt = d/a.txt (9899324b0dd5f4b60e4551877f34e63c0c30c4ddf32a0c948ac559785de7021c)
``


