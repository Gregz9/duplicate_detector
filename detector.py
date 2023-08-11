import argparse
import hashlib
import sys
import os

NOT_PROVIDED_ERROR = (
    "Flag has not been passed, use -h for info on use of -dir/--directory."
)


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

print(os.listdir(args.directory))
res = []
paths = []
for dir_path, dir_names, file_names in os.walk(args.directory):
    for name in file_names:
        # print(os.path.join(dir_path, name))
        paths.append(os.path.join(dir_path, name))
    res.extend(file_names)
print(res)
print(paths)

outfile = open(paths[0], "r")
print(outfile.read())
