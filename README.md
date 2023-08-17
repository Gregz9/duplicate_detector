### Duplicate detector (command line python tool)
This repo contains the code for a command line tool written in python3 (using only standard python libraries), which when provided with path to directory(-ies) will check for duplicate files within the directory, inlcuding subdirectories, and across directories, if provided with multiple paths. It will then print information about the duplicates it has found,
including the name of the files sharing the exact same content, and their respective hash-ids (generated using "sha256"). It also writes the results to a file called "meta.json", in which you'll find a dictionary containing information about which duplicate files were found, and all the files that have been checked in the provided directories. 

**You can find manually created directories used for testing in *test/test_directoires/* folder**

#### Using the tool 
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
#### Passing multiple directories
The script can also be run with multiple directories as arguments, you simply need a white space between each directory path when running the script. E.g.
```
python3 detector.py <directory_path1> <directory_path2> <directory_path3>
```

After the program has finished running, you can call the following command to check the contents of the meta.json file: 
```
cat meta.json
```
#### Passing the "--sizes" flag
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
```
#### Using the "--new" flag 
Another flag that the user may provide the script with when calling it from the command line, is the "--new" flag, which allows the user to track files which are presente in one directory, but not another. When using this flag instead of "--sizes", teh user will be required to pass at least two directory paths, as the main goal of using this flag, should be to compare the contents of directories, and not a directory with itself. When called from the command line, the command look like this
```
python3 detector.py --new <directory_path1> <directory_path2>
```
and will instruct detector to iterate through the directories one at a time. When detector starts iterating thorugh the second directory's content, it will compare it against files conatained within the duplicate directory, and if it's hash is not already present in the dictionary, this will indicate a new file. If a third directory was providedm its contents would we compared against both of the two previous ones. The message output by the command line tool, if any new files are found, will look something like this: 
```
/f.txt in .../Programs/test_dir2 is new (not found in .../Programs/test_dir)
/a.txt in .../Programs/test_dir2 is new (not found in .../Programs/test_dir)
/i/l.txt in .../Programs/test_dir2 is new (not found in .../Programs/test_dir)
/g.txt in .../Programs/test_dir3 is new (not found in .../Programs/test_dir, .../Programs/test_dir2)
Found 4 duplicates:
 /b.txt = /h/t/j.txt = /r/v.txt (1c96838eaceb20143ebeab680c96477f94c116b50a806ca4556f6d5ed8dc4b15)
 /h/y.txt = /d/a.txt (9899324b0dd5f4b60e4551877f34e63c0c30c4ddf32a0c948ac559785de7021c)
 /r/f.txt = /i/c.txt (e8e557393ac3b75519db87a65beabc43f0959694b7003cb6996fca09812c6159)
```

#### Two additional flags: "--update" and "--full_paths"
Those two flags are used in the exact same manner as the "--sizes" flag above, and do not require the user to pass multiple diretctories sucha as the "--new" flag does. The only thing the user has to do again, is to replace one of the previous flags with either "--update" or "--full_paths". Now "--update" will instruct the tool to look through the dicitonary of duplicate files and for each unique hash-id("sha256") find the name of the duplicate file that has been modified most recently. The call from the command line look like this 
```
# Example with multiple directories
python3 detector.py --new <directory_path1> <directory_path2> <directory_path3>
```
while the output will look something like this: 
```
 /b.txt = /h/t/j.txt = /r/v.txt (1c96838eaceb20143ebeab680c96477f94c116b50a806ca4556f6d5ed8dc4b15)
 /h/y.txt = /d/a.txt (9899324b0dd5f4b60e4551877f34e63c0c30c4ddf32a0c948ac559785de7021c)
 /r/f.txt = /i/c.txt (e8e557393ac3b75519db87a65beabc43f0959694b7003cb6996fca09812c6159)
Most recently modified duplicate files:
2/i/c.txt in .../Programs/test_dir is the duplicate that was modified last at Tue Aug 15 22:03:02 2023
/i/c.txt in .../Programs/test_dir is the duplicate that was modified last at Tue Aug 15 22:03:02 2023
```

"--full_paths" is called in the exact same way, with either a single or multiple paths, and will instruct the python script to print the full system paths of all the files detector has iterated over. Its output has the following format: 
```
.../Programs/test_dir/b.txt : ['1c96838eaceb20143ebeab680c96477f94c116b50a806ca4556f6d5ed8dc4b15']
.../Programs/test_dir/h/y.txt : ['9899324b0dd5f4b60e4551877f34e63c0c30c4ddf32a0c948ac559785de7021c']
.../Programs/test_dir/h/t/j.txt : ['1c96838eaceb20143ebeab680c96477f94c116b50a806ca4556f6d5ed8dc4b15']
.../Programs/test_dir/r/f.txt : ['e8e557393ac3b75519db87a65beabc43f0959694b7003cb6996fca09812c6159']
.../Programs/test_dir/r/v.txt : ['1c96838eaceb20143ebeab680c96477f94c116b50a806ca4556f6d5ed8dc4b15']
...
```

### Remarks on use and test-files
When running the this script in the command line be wary of the fact that you cannot provide the program with two flags simultanously. You will have to run the program with one flag at a time, and change flags at each call to achieve desired output. 

When it comes to the test files, these are not proper unit tests. They are more simple tests of different parts of detector.py which were tested during the development of the main program here. Hence, they will deviate storngly from the proper test that are usually written. These test also lack any form for comments, and may thus seem difficult to decode at times, therefore I strongly suggest to overlook them. If you however were to go down this path anyway, after some proper code analysis, they may give you a good intuition of how the different parts of detector behave separately by themselves. 

