import sys
import os


dir_path_top = os.path.dirname(
    os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
)
print(dir_path_top)
exit()
dir_list = os.listdir(dir_path_top)

test_path = str(dir_path_top) + "/" + str(dir_list[0])
print(test_path)
paths = []
for dir_path, dir_names, file_names in os.walk(test_path):
    for name in file_names:
        file_path = os.path.join(dir_path, name)
        if os.path.islink(file_path):
            continue
        paths.append(file_path)

for path in paths:
    print(path)
