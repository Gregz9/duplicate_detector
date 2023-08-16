import hashlib
import sys
import os
import json
import time
from utils import *

# List of available commands that can be passed to the script via terminal
commands = ["--sizes", "--new", "--update", "--full_paths"]

if __name__ == "__main__":
    # Checking the order of arguments passed from terminal
    if len(sys.argv) < 2:
        raise NoArgumentProvidedError("No command has been passed! Program extiting.")
    elif len(sys.argv) == 2:
        directory = [sys.argv[1]]
    # if more than one argument, check if the first argument is a flag/command
    elif len(sys.argv) > 2:
        if str(sys.argv[1]) in commands:
            directory = sys.argv[2:]
        else:
            directory = sys.argv[1:]

    # Generating dictionary with dicts provided as arguments as keys, and list of all paths within
    # directory as values.
    paths = {}
    for direct in directory:
        p = []
        for dir_path, dir_names, file_names in os.walk(str(direct)):
            for name in file_names:
                file_path = os.path.join(dir_path, name)
                if os.path.islink(file_path):
                    continue
                p.append(file_path)
        paths[direct] = p

    hashed_files = {}
    duplicate_files = {}

    # If "--new" is passed, create necessary containers
    if str(sys.argv[1]) == "--new":
        new_files = {}
        key_path = list(paths.keys())
    # Counter for comparison when "--new" is passed as argument
    cnt = 0

    if str(sys.argv[1]) == "--update" or str(sys.argv[1]) == "--full_paths":
        modified_duplicate = {}

    for k, v in paths.items():
        for path in v:
            # Reading files in binary
            with open(path, "rb") as data:
                # Hasing the content of file
                data_hash = hashlib.sha256(data.read()).hexdigest()
                # Removing directory part of path from full path to file
                file_name = data.name.replace(str(k), "")
                hashed_files[file_name] = [data_hash]

                if "--update" in sys.argv or "--full_paths" in sys.argv:
                    filename = data.name
                    modified_duplicate[filename] = [data_hash]

                # In order ot generate the part of dict which tracks duplicate files,
                # we flip the original dict
                if data_hash not in duplicate_files:
                    if cnt > 0 and "--new" in sys.argv:
                        new_files[file_name] = key_path[:cnt]
                    duplicate_files[data_hash] = [file_name]
                else:
                    duplicate_files[data_hash].append(file_name)

        if "--new" in sys.argv:
            cnt += 1

    # Filtering out files which do not have duplicates
    duplicate_files = {k: v for k, v in duplicate_files.items() if len(v) > 1}
    # Copy of duplicate dict for later usage with utils functions
    duplicate_copy = duplicate_files.copy()
    # Total number of duplicates found across directory(-ies)
    sum_duplicates = sum([len(v) - 1 for k, v in duplicate_copy.items()])
    # Final dictionary
    duplicate_files.update(hashed_files)

    # Cheking which command has been passed to print correctly
    if str(sys.argv[1]) == "--new":
        pprint_new_files(new_files)

    if sum_duplicates == 1:
        print(f"Found {sum_duplicates} duplicates:")
    else:
        print(f"Found {sum_duplicates} duplicates:")

    if str(sys.argv[1]) == "--sizes":
        print_dict = construct_string(
            duplicate_copy, find_file_size(duplicate_copy, paths)
        )
    else:
        print_dict = construct_string(duplicate_copy)

    pprint_duplicates(print_dict)
    if "--update" in sys.argv:
        print("Most recently modified duplicate files:")
        pprint_mod_time(
            get_newest_duplicate(modified_duplicate, duplicate_copy, paths), paths
        )

    if "--full_paths" in sys.argv:
        print("Full paths of all files checked by command-line tool and their hash:")
        for full_path, file_hash in modified_duplicate.items():
            print(f"{full_path} : {file_hash}")

    # Writing the dicitionary to meta.json file
    outfile = open("meta.json", "w")
    json.dump(duplicate_files, outfile, indent=4, separators=(", ", ": "))
    outfile.write("\n")
    outfile.close()
