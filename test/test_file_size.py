import os

dir_path_top = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
)

# print(os.path.getsize(dir_path_top + "/Files/CNN/src/Layers.py") / 1000**2)


def file_size(dir_path, files_dict) -> list[dict]:
    file_sizes = []
    for v in files_dict.values():
        file_sizes.append(
            {
                v[i]: os.path.getsize(str(dir_path + v[i])) / 1000**2
                for i in range(len(v))
            }
        )
    return file_sizes


dir_path = dir_path_top + "/Programs/test_dir/"

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
}

print(file_size(dir_path, duplicate_dict))
