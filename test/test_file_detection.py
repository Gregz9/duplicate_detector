import argparse
import hashlib
import sys
import os

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
pprint(paths)

# outfile = open(paths[0], "r")
# print(outfile.read())
