import sys
import os


dir_path_top = os.path.dirname(
    os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
)
print(dir_path_top)

dir_list = os.listdir(dir_path_top)

test_path = str(dir_path_top) + "/" + str(dir_list[0])
print(test_path)
paths = []
# for dir_path, dir_names, file_names in os.walk(
