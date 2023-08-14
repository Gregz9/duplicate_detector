import argparse
import hashlib
import sys
import os
import json


def pprint(p_list):
    for path in p_list:
        print(path)


class PathNotFoundError(Exception):
    def __init__(self, message):
        super().__init__(message)


class NoArgumentProvided(Exception):
    def __init__(self, message):
        super().__init__(message)


if len(list(sys.argv)) < 2:
    raise NoArgumentProvided("No command has been passed! Program extiting.")

paths = []
for dir_path, dir_names, file_names in os.walk(str(sys.argv[1])):
    for name in file_names:
        file_path = os.path.join(dir_path, name)
        if os.path.islink(file_path):
            continue
        paths.append(file_path)

hashed_files = {}
duplicate_files = {}
for path in paths:
    data = open(path, "rb")
    data_hash = hashlib.file_digest(data, "sha256").hexdigest()
    file_name = data.name.replace(str(sys.argv[1]), "")
    hashed_files[file_name] = [data_hash]
    if not data_hash in duplicate_files:
        duplicate_files[data_hash] = [file_name]
    else:
        duplicate_files[data_hash].append(file_name)
duplicate_files = {k: v for k, v in duplicate_files.items() if len(v) > 1}
duplicate_files.update(hashed_files)

print(json.dumps(duplicate_files, indent=4, separators=(", ", ": ")))

outfile = open("meta.json", "w")
json.dump(duplicate_files, outfile, indent=4, separators=(", ", ": "))
outfile.write("\n")
outfile.close()
