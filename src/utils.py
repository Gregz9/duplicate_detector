import os
import sys
import time
import hashlib

"""
File holding helper methods used for printing, and others for dict and list manipulation
"""


def pprint_duplicates(dict_print: dict) -> None:
    """
    Prints the hash and name of duplicate files found in directory(-ies) passed
    as arguments:

    Args:
        dict_print (dict): Dictionary with hash of duplicates as key and list duplicate
                        filenames as values sharing the same hash.

    Returns:
        Nothing
    """
    for k, v in dict_print.items():
        print(f" {k} ({v}) ")


def pprint_new_files(new_files: dict) -> None:
    """
    When multiple dicitonaries are passed as arguments together with "--new"
    to detector, it prints the new files not found in the dictionaries already
    iterated thorugh.


    Args:
        new_files (dict{str : [str]): Dictionary containing filename as key and
                            list of previous directories it was not present in.

    Returns:
        Nothing

    Example:
        E.g. if ./a/ and ./b/ are the directories passed, and c.txt
        is found in ./b/ but not in ./a/ which was iterated over first,
        c.txt will be included in the print.
    """
    for k, v in new_files.items():
        print(f"{k} in {v[-1]} is new (not found in {', '.join(v[:-1])})")


def pprint_mod_time(duplicates_n_time: dict, paths: dict) -> None:
    """
    Iterates over keys and values of dictionary containing names of duplicate files and
    the timestamp of when they were modified last time, and prints out that information.

    Args:
        duplicate_n_time (dict): Dictionary with name of duplicate file as key and the timestamp
                                of when it was modified last time as value.

        paths (dict{str : [str]}): Dictionary with directory paths passed as arguments to detector as keys,
                    and list of paths of files conatined within each of the directories as values.

    Returns:
        Nothing
    """
    idx = 0
    directories = list(paths.keys())
    for duplicate, time_ in duplicates_n_time.items():
        print(
            f"{duplicate} in {directories[0]} is the duplicate that was modified last at {time_}"
        )
        idx += 1


def find_file_size(duplicate_dict: dict, paths: dict) -> list[dict]:
    """
    Finds the sizes of duplicate files found across directories passed as arguments
    to detector.

    Args:
        duplicate_dict (dict {str: [str]}) : Dictionary with hash of duplicates as key and list duplicate
                            filenames as values sharing the same hash.

        paths (dict{str : [str]}): Dictionary with directory paths passed as arguments to detector as keys,
                    and list of paths of files conatined within each of the directories as values.

    Returns:
        file_size (list[dict]) : List of dictionaries containing name of the first duplicate found
                                across directories, and their respective sizes in KB.

    """
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
    """
    Returns A dictionary containing the name of the newest duplicate
    for each of the hash-ids found in duplicate_dict, which is the
    dictionary containing name of all duplicate files, and the timestamp
    of last modification to the file.

    Args:
        full_path_hash (dict{str: [str]}) : Dictionary of full paths to
                                        all files found in all directories
                                        and their respective hash-ids.

        duplicate_dict (dict {str: [str]}) : Dictionary with hash of duplicates as key and list duplicate
                            filenames as values sharing the same hash.

        paths (dict{str : [str]}): Dictionary with directory paths passed as arguments to detector as keys,
                            and list of paths of files conatined within each of the directories as values.

    Returns:
        file_n_time (dict {str: timestamp}) : Dictionary with filename and timestamp
    """

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
    """
    Contructs the string used for the main output of detector
    when any duplicate files are detected. If file_sizes are passed,
    the string inlcudes size of files measured in KB.

    Args:
        duplicate_dict (dict {str: [str]}) : Dictionary with hash of duplicates as key and list duplicate
                            filenames as values sharing the same hash.

        file_sizes (list[dict]) : List of dictionaries containing name of the first duplicate found
                                across directories, and their respective sizes in KB.
    Returns:
        dup_strings (dict{str: str}) : Dictionary containing string for print as key, and hash-id
                                    of duplicate files as value.
    """
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
    """
    Custom Error class for when no directory is provided as argument to detector
    """

    def __init__(self, message):
        super().__init__(message)


class NoArgumentProvidedError(Exception):
    """
    Custom Error class for when no argument is provided as argument to detector
    """

    def __init__(self, message):
        super().__init__(message)
