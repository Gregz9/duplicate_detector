import sys
import os
import json


def file_size(dir_path, files_dict) -> list[dict]:
    file_sizes = []
    for v in files_dict.values():
        file_sizes.append({v[0]: os.path.getsize(str(dir_path + v[0])) / 1000})
    return file_sizes


paths = {
    "/home/gregz/Programs/test_dir/": [
        "/home/gregz/Programs/test_dir/b.txt",
        "/home/gregz/Programs/test_dir/h/y.txt",
        "/home/gregz/Programs/test_dir/h/t/j.txt",
        "/home/gregz/Programs/test_dir/r/f.txt",
        "/home/gregz/Programs/test_dir/r/v.txt",
        "/home/gregz/Programs/test_dir/d/a.txt",
        "/home/gregz/Programs/test_dir/d/c.txt",
    ]
}
#     "/home/gregz/Programs/test_dir2/": [
#         "/home/gregz/Programs/test_dir2/f.txt",
#         "/home/gregz/Programs/test_dir2/i/c.txt",
#         "/home/gregz/Programs/test_dir2/i/l.txt",
#     ],
# }

duplicate_dict = {
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
print(file_sizes)
