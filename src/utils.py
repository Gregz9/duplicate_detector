import os
import sys
import time
import hashlib

"""
File holding helper methods used for printing, and others for dict and list manipulation
"""


def pprint_duplicates(dict_print):
    """ """
    for k, v in dict_print.items():
        print(f" {k} ({v}) ")


def pprint_new_files(new_files):
    for k, v in new_files.items():
        print(f"{k} in {v[-1]} is new (not found in {', '.join(v[:-1])})")


def pprint_mod_time(duplicates_n_time, paths):
    idx = 0
    directories = list(paths.keys())
    for duplicate, time_ in duplicates_n_time.items():
        print(
            f"{duplicate} in {directories[0]} is the duplicate that was modified last at {time_}"
        )
        idx += 1


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


def get_newest_duplicate(full_path_hash, duplicate_dict, paths):
    duplicates_moded_date = {}
    for hash1, file_names in duplicate_dict.items():
        file_n_time = {}
        for full_path, hash2 in full_path_hash.items():
            if hash1 == hash2[0]:
                mod_time = os.path.getmtime(full_path)
                file_n_time[full_path] = mod_time
        duplicates_moded_date.update(file_n_time)

    file_n_time = {}
    for directory in paths.keys():
        max_time = 0
        file_name = ""
        for file_path, mod_time in duplicates_moded_date.items():
            if directory in file_path:
                if mod_time > max_time:
                    max_time = mod_time
                    file_name = file_path.replace(directory, "")

        file_n_time[file_name] = time.ctime(max_time)

    file_n_time = {k: v for k, v in file_n_time.items() if k != ""}

    return file_n_time


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


class PathNotFoundError(Exception):
    def __init__(self, message):
        super().__init__(message)


class NoArgumentProvidedError(Exception):
    def __init__(self, message):
        super().__init__(message)
