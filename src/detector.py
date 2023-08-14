import argparse
import hashlib
import sys
import os
import json

NOT_PROVIDED_ERROR = (
    "Flag has not been passed, use -h for info on use of -dir/--directory."
)


def pprint(p_list):
    for path in p_list:
        print(path)


class PathNotFoundError(Exception):
    def __init__(self, message):
        super().__init__(message)


class MyArgumentParser(argparse.ArgumentParser):
    def exit(self, status=0, message=None):
        if status:
            print(NOT_PROVIDED_ERROR)
        exit(status)

    def error(self, message):
        # self.print_help(sys.stderr)
        self.exit(1, f"ERROR: {self.prog, message}")


ap = MyArgumentParser()
ap.add_argument(
    "-dir",
    "--directory",
    type=str,
    required=True,
    help="Path of directory containing files to be checked by detector",
)
args = ap.parse_args()

if not os.path.exists(args.directory):
    raise PathNotFoundError("Invalid path! No existing directory with such name found!")
else:
    print(args.directory)

# print(os.listdir(args.directory))
res = []
paths = []
for dir_path, dir_names, file_names in os.walk(args.directory):
    for name in file_names:
        # print(os.path.join(dir_path, name))
        file_path = os.path.join(dir_path, name)
        if os.path.islink(file_path):
            continue
        paths.append(file_path)
    res.extend(file_names)
# print(res)
# pprint(paths)

data0 = open(paths[0], "rb")
data0_hash = hashlib.file_digest(data0, "sha256").hexdigest()
# print(paths[0])
# print(data0_hash)

hashed_files = {}
duplicate_files = {}
for path in paths:
    data = open(path, "rb")
    data_hash = hashlib.file_digest(data, "sha256").hexdigest()
    file_name = data.name.replace(str(args.directory + "/"), "")
    hashed_files[file_name] = [data_hash]


print(json.dumps(hashed_files, indent=4, separators=(", ", ": ")))

# outfile = open(paths[0], "r")
# print(outfile.read())
