import os
import sys
import hashlib
import json


def find_file_size():
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


def pprint_new_files(new_files):
    print("\n")
    for k, v in new_files.items():
        print(f"{k} in {v[-1]} is new (not found in {', '.join(v[:-1])})")

    print("\n")


directories = sys.argv[1:]

paths = {}
for directory in directories:
    p = []
    for dir_path, dir_names, file_names in os.walk(str(directory)):
        for name in file_names:
            file_path = os.path.join(dir_path, name)
            if os.path.islink(file_path):
                continue
            p.append(file_path)
    paths[directory] = p

# for k, v in paths.items():
#     for path in v:
#         print(path)

hashed_files = {}
duplicate_files = {}
hashed_full_path = {}
new_files = {}

cnt = 0
key_path = list(paths.keys())
# print(key_path)
for k, v in paths.items():
    for path in v:
        data = open(path, "rb")
        data_hash = hashlib.file_digest(data, "sha256").hexdigest()
        file_name = data.name
        # print(file_name)
        assert file_name == path
        hashed_full_path[file_name] = [data_hash]
        file_name = data.name.replace(str(k), "")
        # print(file_name)
        hashed_files[file_name] = [data_hash]
        if not data_hash in duplicate_files:
            if cnt > 0:
                new_files[file_name] = key_path[: cnt + 1]
            duplicate_files[data_hash] = [file_name]
        else:
            duplicate_files[data_hash].append(file_name)

    cnt += 1


pprint_new_files(new_files)

exit()
print(json.dumps(duplicate_files, indent=4, separators=(", ", ": ")))
print(json.dumps(new_files, indent=4, separators=(", ", ": ")))


duplicate_files = {k: v for k, v in duplicate_files.items() if len(v) > 1}
duplicate_copy = duplicate_files.copy()
sum_duplicates = sum([len(v) - 1 for v in duplicate_copy.items()])
duplicate_files.update(hashed_files)


print(json.dumps(duplicate_files, indent=4, separators=(", ", ": ")))
