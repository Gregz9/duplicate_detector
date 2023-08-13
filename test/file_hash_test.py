import hashlib

data_file = open("random_data1.txt", "r")

print(data_file.name)

data = data_file.read()

file_hash = hashlib.sha256(data.encode("utf-8")).hexdigest()
print(file_hash)
