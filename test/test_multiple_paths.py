import os
import sys

directories = sys.argv[1:]
print(directories)

paths = []
for directory in directories:
    for dir_path, dir_names, file_names in os.walk(str(directory)):
        for name in file_names:
            file_path = os.path.join(dir_path, name)
            if os.path.islink(file_path):
                continue
            paths.append(file_path)

print(paths)
# for path in paths:
# print(path)
