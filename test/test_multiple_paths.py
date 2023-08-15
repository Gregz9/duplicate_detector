import os
import sys
import hashlib
import json

directories = sys.argv[1:]
print(directories)

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

# print(paths)

hashed_files = {}
duplicate_files = {}
for k, v in paths.items():
    for path in v:
        data = open(path, "rb")
        data_hash = hashlib.file_digest(data, "sha256").hexdigest()
        file_name = data.name
        print(file_name)
        assert file_name == path
        file_name = data.name.replace(str(k), "")
        # print(file_name)
        hashed_files[file_name] = [data_hash]
        if not data_hash in duplicate_files:
            duplicate_files[data_hash] = [file_name]
        else:
            duplicate_files[data_hash].append(file_name)

duplicate_files = {k: v for k, v in duplicate_files.items() if len(v) > 1}
duplicate_copy = duplicate_files.copy()
sum_duplicates = sum([len(v) - 1 for v in duplicate_copy.items()])
duplicate_files.update(hashed_files)

print(json.dumps(duplicate_files, indent=4, separators=(", ", ": ")))


# print(paths)
# for path in paths:
# print(path)
