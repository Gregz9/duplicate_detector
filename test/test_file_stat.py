import sys
import os
import json
import time

full_duplicates = {
    "/home/gregz/Programs/test_dir/b.txt": [
        "1c96838eaceb20143ebeab680c96477f94c116b50a806ca4556f6d5ed8dc4b15"
    ],
    "/home/gregz/Programs/test_dir/h/y.txt": [
        "9899324b0dd5f4b60e4551877f34e63c0c30c4ddf32a0c948ac559785de7021c"
    ],
    "/home/gregz/Programs/test_dir/h/t/j.txt": [
        "1c96838eaceb20143ebeab680c96477f94c116b50a806ca4556f6d5ed8dc4b15"
    ],
    "/home/gregz/Programs/test_dir/r/f.txt": [
        "e8e557393ac3b75519db87a65beabc43f0959694b7003cb6996fca09812c6159"
    ],
    "/home/gregz/Programs/test_dir/r/v.txt": [
        "1c96838eaceb20143ebeab680c96477f94c116b50a806ca4556f6d5ed8dc4b15"
    ],
    "/home/gregz/Programs/test_dir/d/a.txt": [
        "9899324b0dd5f4b60e4551877f34e63c0c30c4ddf32a0c948ac559785de7021c"
    ],
    "/home/gregz/Programs/test_dir/d/c.txt": [
        "6d3e371e47eac260af9c3ff4cda64ff812f2e315b971f53c11d5b8527f8577fa"
    ],
    "/home/gregz/Programs/test_dir2/f.txt": [
        "cf75d395a60e0c34ee06705f35d0e27b0b9ac32decc5d5458258a389f90dc50a"
    ],
    "/home/gregz/Programs/test_dir2/a.txt": [
        "e06f9cbf017ee910c22e753ef6c11208771c508329ba42c78723f0cfbca28b23"
    ],
    "/home/gregz/Programs/test_dir2/i/c.txt": [
        "e8e557393ac3b75519db87a65beabc43f0959694b7003cb6996fca09812c6159"
    ],
    "/home/gregz/Programs/test_dir2/i/l.txt": [
        "c7bb6cd9f3d56e7e3eb2df7042d76fec66eb0a5262d40969f348ddfa5bf17590"
    ],
    "/home/gregz/Programs/test_dir3/g.txt": [
        "f3bbf81e51dacc198d14d9f1399550e6d4c456949fcea17a8c897e9083957b22"
    ],
}

duplicates_dict = {
    "1c96838eaceb20143ebeab680c96477f94c116b50a806ca4556f6d5ed8dc4b15": [
        "b.txt",
        "h/t/j.txt",
        "r/v.txt",
    ],
    "9899324b0dd5f4b60e4551877f34e63c0c30c4ddf32a0c948ac559785de7021c": [
        "h/y.txt",
        "d/a.txt",
    ],
    "e8e557393ac3b75519db87a65beabc43f0959694b7003cb6996fca09812c6159": [
        "r/f.txt",
        "i/c.txt",
    ],
}

paths = {
    "/home/gregz/Programs/test_dir/": [
        "/home/gregz/Programs/test_dir/b.txt",
        "/home/gregz/Programs/test_dir/h/y.txt",
        "/home/gregz/Programs/test_dir/h/t/j.txt",
        "/home/gregz/Programs/test_dir/r/f.txt",
        "/home/gregz/Programs/test_dir/r/v.txt",
        "/home/gregz/Programs/test_dir/d/a.txt",
        "/home/gregz/Programs/test_dir/d/c.txt",
    ],
    "/home/gregz/Programs/test_dir2/": [
        "/home/gregz/Programs/test_dir2/f.txt",
        "/home/gregz/Programs/test_dir2/a.txt",
        "/home/gregz/Programs/test_dir2/i/c.txt",
        "/home/gregz/Programs/test_dir2/i/l.txt",
    ],
    "/home/gregz/Programs/test_dir3/": ["/home/gregz/Programs/test_dir3/g.txt"],
}

duplicates_moded_date = {}
duplicates_moded_date2 = {}
for hash1, file_names in duplicates_dict.items():
    file_n_time = {}
    file_n_time2 = {}
    for full_path, hash2 in full_duplicates.items():
        if hash1 == hash2[0]:
            mod_time = os.path.getmtime(full_path)
            file_n_time[full_path] = mod_time
            file_n_time2[full_path] = time.ctime(mod_time)
    duplicates_moded_date.update(file_n_time)
    duplicates_moded_date2.update(file_n_time2)


# for k,v in paths.items():
#     for file_ in

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

print(file_n_time)


for file, time_mod in duplicates_moded_date2.items():
    print(file, time_mod)

# for full_path, hash2 in full_duplicates.items():
