import hashlib
import sys
import os
import json


def pprint_duplicates(dict_print):
    for k, v in dict_print.items():
        print(f" {k} ({v}) ")


def pprint_new_files(new_files):
    for k, v in new_files.items():
        print(f"{k} in {v[-1]} is new (not found in {', '.join(v[:-1])})")


def find_file_size(duplicate_dict, paths):
    file_sizes = []
    for k, v in duplicate_dict.items():
        for file_name in v:
            for k2, v2 in paths.items():
                for path in v2:
                    if file_name in path:
                        file_size = {v[0]: os.path.getsize(str(path)) / 1000}
                    if file_size in file_sizes:
                        continue
                    file_sizes.append(file_size)
    return file_sizes


class PathNotFoundError(Exception):
    def __init__(self, message):
        super().__init__(message)


class NoArgumentProvidedError(Exception):
    def __init__(self, message):
        super().__init__(message)


def construct_string(duplicate_dict, file_sizes=[]):
    dup_strings = {}
    i = 0
    for k, v in duplicate_dict.items():
        if len(file_sizes) > 0:
            file_string = f"({file_sizes[i][v[0]]} KB) " + " = ".join(v)
            i += 1
        else:
            file_string = " = ".join(v)

        dup_strings[file_string] = k

    return dup_strings


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise NoArgumentProvidedError("No command has been passed! Program extiting.")
    elif len(sys.argv) == 2:
        directory = [sys.argv[1]]
    elif len(sys.argv) > 2:
        if str(sys.argv[1]) == "--sizes" or str(sys.argv[1]) == "--new":
            directory = sys.argv[2:]
        else:
            directory = sys.argv[1:]

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

    if str(sys.argv[1]) == "--new":
        new_files = {}
        key_path = list(paths.keys())
    cnt = 0

    for k, v in paths.items():
        for path in v:
            with open(path, "rb") as data:
                data_hash = hashlib.sha256(data.read()).hexdigest()
                file_name = data.name.replace(str(k), "")
                hashed_files[file_name] = [data_hash]

                if data_hash not in duplicate_files:
                    if cnt > 0 and "--new" in sys.argv:
                        new_files[file_name] = key_path[:cnt]
                    duplicate_files[data_hash] = [file_name]
                else:
                    duplicate_files[data_hash].append(file_name)

        if "--new" in sys.argv:
            cnt += 1

    duplicate_files = {k: v for k, v in duplicate_files.items() if len(v) > 1}
    duplicate_copy = duplicate_files.copy()
    sum_duplicates = sum([len(v) - 1 for k, v in duplicate_copy.items()])
    duplicate_files.update(hashed_files)

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

    outfile = open("meta.json", "w")
    json.dump(duplicate_files, outfile, indent=4, separators=(", ", ": "))
    outfile.write("\n")
    outfile.close()
