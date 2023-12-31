import json
import hashlib

DIRECTORY = "test_files/"

data_file = open("test_files/random_data1.txt", "r")

data = data_file.read()
data_hash = hashlib.sha256(data.encode("utf-8")).hexdigest()
data_file.close()

files = {}
files[data_hash] = [data_file.name.split("/")[-1]]

file_name = data_file.name.replace(DIRECTORY, "")
files[file_name] = data_hash

outfile = open("meta.json", "w")
json.dump(files, outfile, indent=4, separators=(", ", ": "))
outfile.write("\n")

outfile.close()
